import boto3
from botocore.exceptions import ClientError

class QuickSightService:
    def __init__(self):
        self.client = boto3.client('quicksight', region_name='us-east-1')

    def generate_embed_url(self, user_arn, dashboard_id):
        try:
            response = self.client.generate_embed_url_for_registered_user(
                AwsAccountId='your_aws_account_id',  # Replace with your AWS account ID
                DashboardId=dashboard_id,
                UserArn=user_arn,
                ExperienceConfiguration={
                    'Dashboard': {
                        'InitialDashboardId': dashboard_id
                    }
                },
                AllowedDomains=['http://localhost:3000']  # Add your frontend domain
            )
            return response['EmbedUrl']
        except ClientError as e:
            raise ValueError(f"Error generating embed URL: {str(e)}")