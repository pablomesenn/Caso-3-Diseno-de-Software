import boto3
import snowflake.connector
from app.config.config import (
    S3_BUCKET,
    SNOWFLAKE_ACCOUNT,
    SNOWFLAKE_USER,
    SNOWFLAKE_PASSWORD,
    SNOWFLAKE_WAREHOUSE,
)

class DataRepository:
    def __init__(self):
        self.s3_client = boto3.client('s3')
        self.snowflake_conn = snowflake.connector.connect(
            user=SNOWFLAKE_USER,
            password=SNOWFLAKE_PASSWORD,
            account=SNOWFLAKE_ACCOUNT,
            warehouse=SNOWFLAKE_WAREHOUSE
        )

    def upload_to_s3(self, bucket, key, data):
        try:
            self.s3_client.put_object(Bucket=bucket, Key=key, Body=data)
        except Exception as e:
            raise ValueError(f"Failed to upload to S3: {str(e)}")

    def query_snowflake(self, query):
        cursor = self.snowflake_conn.cursor()
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except snowflake.connector.Error as e:
            raise ValueError(f"Snowflake query failed: {str(e)}")
        finally:
            cursor.close()