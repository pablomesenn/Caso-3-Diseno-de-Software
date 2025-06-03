## Install CDK

```
npm install -g aws-cdk
cdk bootstrap aws://ACCOUNT-NUMBER/REGION
```

## Deploy Stack
```
cdk deploy
```

## Upload Glue Script

```
aws s3 cp glue_etl_script.py s3://raw-data-bucket/scripts/
```