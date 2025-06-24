## Install CDK

```
npm install -g aws-cdk

cdk bootstrap aws://ACCOUNT-NUMBER/REGION

pip install -r requirements.txt
```

## Deploy Stack
```
cdk deploy --app "app.py"
```

## Upload Glue Script

```

aws s3 cp glue_etl_script.py s3://datalakeaiagentstack-processeddatabucket4e25d3b7-zuw9h69rjnec/scripts/glue_script.py

aws s3 cp sample_data.json s3://datalakeaiagentstack-rawdatabucket57f26c03-dx5pbjbcwyaj/raw_data/sample_data.json

# Start glue-job
aws glue start-job-run --job-name data-pura-vida-load

# Check if Lambda was triggered
aws logs describe-log-groups --log-group-name-prefix "/aws/lambda/DataLakeAIAgentStack-AIAgentFunction"

# Confirm job success
aws glue get-job-run --job-name data-pura-vida-load --run-id jr_a129a8dc3a0df6c83e7db11972e4e60aa18585915ef542b53f5bde023217a9b5

```