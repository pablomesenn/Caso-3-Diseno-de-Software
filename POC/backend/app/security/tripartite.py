import secretsharing as sss
import boto3
from botocore.exceptions import ClientError

class TripartiteKeyService:
    def __init__(self):
        self.secrets_client = boto3.client('secretsmanager')

    def generate_key_shares(self, secret, shares=3, threshold=2):
        try:
            shares = sss.SecretSharer.split_secret(secret, threshold, shares)
            for i, share in enumerate(shares):
                self.secrets_client.put_secret_value(
                    SecretId=f"tripartite-share-{i}",
                    SecretString=share
                )
            return shares
        except ClientError as e:
            raise ValueError(f"Error storing shares: {str(e)}")

    def reconstruct_secret(self, shares):
        try:
            return sss.SecretSharer.recover_secret(shares)
        except Exception as e:
            raise ValueError(f"Error reconstructing secret: {str(e)}")