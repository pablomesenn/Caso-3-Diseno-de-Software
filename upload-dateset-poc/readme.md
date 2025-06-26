## Dataset Upload POC

This Proof of Concept (POC) demonstrates a serverless data processing pipeline on AWS that automatically processes raw data through a data lake architecture. The system uses AWS Glue for ETL operations and Lambda functions for post-processing automation, all orchestrated through EventBridge.

## Architecture

The solution implements a modern data lake pattern with the following components:

- **Raw Data Storage**: S3 bucket for ingesting unprocessed data
- **Processed Data Storage**: S3 bucket for cleaned and transformed data
- **Data Discovery**: AWS Glue Crawler for schema detection
- **ETL Processing**: AWS Glue Job for data transformation
- **Automation**: Lambda function triggered by Glue job completion
- **Event Orchestration**: EventBridge for workflow coordination

## System Components

### 1. Storage Layer
- **Raw Data Bucket**: Stores incoming JSON files in `raw_data/` prefix
- **Processed Data Bucket**: Contains Parquet files partitioned by year/month/day
- **Script Storage**: Houses the Glue ETL script

### 2. Data Processing Layer
- **Glue Database**: `processed_data_db` - catalog for processed data schemas
- **Glue Crawler**: `user-data-crawler` - discovers and catalogs raw data schemas
- **Glue Job**: `data-pura-vida-load` - transforms JSON to Parquet format

### 3. Automation Layer
- **Lambda Function**: `AIAgentFunction` - post-processing automation
- **EventBridge Rule**: Triggers Lambda when Glue job completes successfully

## Data Flow
```
1. Raw JSON data → Raw Data S3 Bucket
2. Glue Crawler → Discovers schema → Updates Glue Catalog
3. Glue Job → Reads raw data → Transforms → Writes Parquet files
4. EventBridge → Detects job completion → Triggers Lambda
5. Lambda → Lists processed files → Logs results
```

## File Structure
```
upload-dateset-poc/
├── app.py                     # CDK application entry point
├── requirements.txt           # Python dependencies
├── readme.md                 # Setup instructions
├── sample_data.json          # Sample data for testing
├── glue_etl_script.py        # ETL transformation logic
├── lambda/
│   └── ai_agent.py           # Lambda function code
└── cdk.out/                  # CDK synthesized outputs
    ├── DataLakeAIAgentStack.template.json
    └── ...
```

## Key Features

### Data Transformation
- **Input Format**: JSON files with user data
- **Output Format**: Parquet files (columnar, compressed)
- **Data Cleaning**: Removes unnecessary fields (`unnecessary_field1`, `unnecessary_field2`)
- **Partitioning**: Organizes data by year/month/day for efficient querying

### Infrastructure as Code
- **AWS CDK**: Python-based infrastructure definition
- **Auto-scaling**: Serverless components scale automatically
- **Resource Cleanup**: Automatic deletion of S3 objects on stack destruction

### Event-Driven Architecture
- **Asynchronous Processing**: Glue jobs run independently
- **Automatic Triggers**: Lambda executes only after successful ETL completion
- **Error Handling**: Failed jobs don't trigger downstream processing


## Setup Instructions

### Prerequisites
```bash
# Install AWS CDK
npm install -g aws-cdk

# Bootstrap CDK (replace with your account/region)
cdk bootstrap aws://ACCOUNT-NUMBER/REGION

# Install Python dependencies
pip install -r requirements.txt
```

### Deployment
```bash
# Deploy the infrastructure
cdk deploy --app "app.py"
```

### Post-Deployment Setup
```bash
# Upload the Glue ETL script
aws s3 cp glue_etl_script.py s3://[PROCESSED-BUCKET-NAME]/scripts/glue_script.py

# Upload sample data
aws s3 cp sample_data.json s3://[RAW-BUCKET-NAME]/raw_data/sample_data.json

# Start the ETL job
aws glue start-job-run --job-name data-pura-vida-load
```

Note: S3 buckets are configured with `auto_delete_objects=True` for easy cleanup in this demo environment.



## Results

```bash
npm install -g aws-cdk
cdk bootstrap aws://ACCOUNT-NUMBER/REGION


cdk deploy --app "app.py"
```

![Screenshot 2025-06-24 165449](https://github.com/user-attachments/assets/b978bae8-15c9-4365-8bc9-668a7d907a30)

```bash
aws s3 cp glue_etl_script.py s3://[PROCESSED-BUCKET-NAME]/scripts/glue_script.py
```
![Screenshot 2025-06-24 165820](https://github.com/user-attachments/assets/5a088e8a-d9f6-44bd-a0ae-c1aff444be08)

```bash
aws s3 cp sample_data.json s3://[RAW-BUCKET-NAME]/raw_data/sample_data.json
```
![Screenshot 2025-06-24 165920](https://github.com/user-attachments/assets/9f4d46a1-50e8-47a9-be12-7c3dddf5c8fb)
![Screenshot 2025-06-24 165934](https://github.com/user-attachments/assets/cfe8c486-932b-49ba-bd1f-063af0b7b74f)

```bash
aws glue start-job-run --job-name data-pura-vida-load
```
![Screenshot 2025-06-24 170014](https://github.com/user-attachments/assets/4f4febff-6796-4124-8551-657c413effac)
![Screenshot 2025-06-24 170032](https://github.com/user-attachments/assets/7283882e-1f22-4941-934d-f64342b79c8f)

```
# Check if Lambda was triggered
aws logs describe-log-groups --log-group-name-prefix "/aws/lambda/DataLakeAIAgentStack-AIAgentFunction"
```
![Screenshot 2025-06-24 170117](https://github.com/user-attachments/assets/2a2dbce4-65b7-467d-8447-2a0e616be0cd)

```
# Confirm job success
aws glue get-job-run --job-name data-pura-vida-load --run-id jr_a129a8dc3a0df6c83e7db11972e4e60aa18585915ef542b53f5bde023217a9b5
```
![Screenshot 2025-06-24 170135](https://github.com/user-attachments/assets/8df6bf6a-6328-4662-88b3-f38ae188d2d9)
