from aws_cdk import (
    App,
    Stack,
    aws_s3 as s3,
    aws_glue as glue,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    RemovalPolicy
)
from constructs import Construct

class DataLakeAIAgentStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create an S3 bucket for data storage
        raw_data_bucket = s3.Bucket(
            self, "RawDataBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True  # For demo purposes
        )
        
        # Processed data bucket
        processed_data_bucket = s3.Bucket(
            self, "ProcessedDataBucket",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True  # For demo purposes
        )
        
        # Glue Database
        glue_database = glue.CfnDatabase(
            self, "GlueDatabase",
            catalog_id=self.account,
            database_input={
                "name": "processed_data_db",
                "description": "Database for processed data"
            }
        )
        
        # IAM Role for Glue Crawler
        glue_crawler_role = iam.Role(
            self, "GlueCrawlerRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")
            ]
        )
        
        # Grant S3 permissions to crawler
        raw_data_bucket.grant_read_write(glue_crawler_role)
        processed_data_bucket.grant_read_write(glue_crawler_role)
        
        # Glue Crawler to discover data
        glue_crawler = glue.CfnCrawler(
            self, "GlueCrawler",
            name="user-data-crawler",
            role=glue_crawler_role.role_arn,
            database_name=glue_database.ref,
            targets={
                "s3Targets": [{"path": f"s3://{raw_data_bucket.bucket_name}/raw_data/"}]
            }
        )
        
        # IAM Role for Glue Job
        glue_job_role = iam.Role(
            self, "GlueJobRole",
            assumed_by=iam.ServicePrincipal("glue.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")
            ]
        )
        
        # Grant S3 permissions to job
        raw_data_bucket.grant_read_write(glue_job_role)
        processed_data_bucket.grant_read_write(glue_job_role)
        
        # Glue Job to process data
        glue_job = glue.CfnJob(
            self, "DataPuraVidaLoad",
            name="data-pura-vida-load",
            role=glue_job_role.role_arn,
            command={
                "name": "glueetl",
                "scriptLocation": f"s3://{processed_data_bucket.bucket_name}/scripts/glue_script.py",
                "pythonVersion": "3"
            },
            default_arguments={
                "--TempDir": f"s3://{processed_data_bucket.bucket_name}/temp/",
                "--job-language": "python",
                "--job-bookmark-option": "job-bookmark-enable",
                "--input_bucket": raw_data_bucket.bucket_name,
                "--output_bucket": processed_data_bucket.bucket_name
            },
            glue_version="3.0"
        )
        
        # Lambda function to process data
        lambda_agent = _lambda.Function(
            self, "AIAgentFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="ai_agent.handler",
            environment={
                "PROCESSED_DATA_BUCKET": processed_data_bucket.bucket_name,
            }
        )
        
        # Grant permissions to Lambda function
        processed_data_bucket.grant_read_write(lambda_agent)
        
        # EventBridge Rule to trigger Lambda function 
        rule = events.Rule(
            self, "GlueJobCompletionRule",
            event_pattern=events.EventPattern(
                source=["aws.glue"],
                detail_type=["Glue Job State Change"],
                detail={
                    "jobName": [glue_job.ref],
                    "state": ["SUCCEEDED"]
                }
            )    
        )
        rule.add_target(targets.LambdaFunction(lambda_agent))    
        
        # Outputs
        self.raw_data_bucket_name = raw_data_bucket.bucket_name
        self.processed_data_bucket_name = processed_data_bucket.bucket_name

app = App()
DataLakeAIAgentStack(app, "DataLakeAIAgentStack")
app.synth()
        
