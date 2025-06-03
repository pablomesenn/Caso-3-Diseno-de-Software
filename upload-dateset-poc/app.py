from aws_cdk import {
    App,
    Stack,
    aws_s3 as s3,
    aws_glue as glue,
    aws_lambda as _lambda,
    aws_iam as iam,
    aws_events as events,
    aws_events_targets as targets,
    aws_sns as sns,
    aws_sns_subscriptions as subscriptions,
}
from constructs import Construct

class DataLakeAIAgentStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Create an S3 bucket for data storage
        raw_data_bucket = s3.Bucket(
            self, "RawDataBucket",
            removal_policy=s3.RemovalPolicy.DESTROY)
        
        # Processed data bucket
        processed_data_bucket = s3.Bucket(
            self, "ProcessedDataBucket",
            removal_policy=s3.RemovalPolicy.DESTROY)
        
        # GLUE
        # Glue Crawlers to discover data
        glue_crawler = glue.CfnCrawler(
            self, "GlueCrawler",
            name = "user_data_crawler",
            role = iam.Role(
                self, "GlueCrawlerRole",
                assumed_by = iam.ServicePrincipal("glue.amazonaws.com"),
                managed_policies = [iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")]
            ).role_arn,
            database_name = "processed_data_db",
            targets = {
                "s3Targets": [{"path": raw_data_bucket.bucket_arn}]
            }
        )
        # Glue Job to process data
        glue_job = glue.CfnJob(
            self, "DataPuraVidaLoad",
            name = "data_pura_vida_load",
            role = iam.Role(
                self, "GlueJobRole",
                assumed_by = iam.ServicePrincipal("glue.amazonaws.com"),
                managed_policies = [iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSGlueServiceRole")]
            ).role_arn,
            command = {
                "name": "glueetl",
                "scriptLocation": f"s3://{processed_data_bucket.bucket_name}/scripts/glue_script.py",
                "pythonVersion": "3"
            },
            default_arguments = {
                "--TempDir": f"s3://{processed_data_bucket.bucket_name}/temp/",
                "--job-language": "python",
                "--job-bookmark-option": "job-bookmark-enable",
                "--input_bucket": raw_data_bucket.bucket_name,
                "--output_bucket": processed_data_bucket.bucket_name
            }
            )
        
        # Lambda AI AGENT
        # Lambda function to process data and interact with AI Agent
        lambda_agent = _lambda.Function(
            self, "AIAgentFunction",
            runtime=_lambda.Runtime.PYTHON_3_9,
            code=_lambda.Code.from_asset("lambda"),
            handler="ai_agent.handler",
            environment={
                "PROCESSED_DATA_BUCKET": processed_data_bucket.bucket_name,
                "SNOWFLAKE_ACCOUNT": "your-snowflake-account",
                "SNOWFLAKE_USER": "your-snowflake-user",
                "SNOWFLAKE_PASSWORD": "your-snowflake-password",
            }
        )
        
        # Grant permissions to Lambda function
        processed_data_bucket.grant_read_write(lambda_agent)
        
        # EventBridge Rule to trigger Lambda function
        rule = evemts.Rule(
            self, "GlueJobCompletionRule",
            event_pattern= events.EventPattern(
                source=["aws.glue"],
                detail_type=["Glue Job State Change"],
                detail={
                    "jobName": [glue_job.name],
                    "state": ["SUCCEEDED"]
                }
            )    
        )
        rule.add_target(targets.LambdaFunction(lambda_agent))    
        
        # outputs
        self.raw_data_bucket_name = raw_data_bucket.bucket_name
        self.processed_data_bucket_name = processed_data_bucket.bucket_name

app = App()
DataLakeAIAgentStack(app, "DataLakeAIAgentStack")
app.synth()
        
        
