import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext

args = getResolvedOptions(sys.argv, ['input_bucket', 'output_bucket'])
sc = SparkContext()
glueContext = GlueContext(sc)

# Read raw data from S3
raw_data = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths": [f"s3://{args['input_bucket']}/raw_data/"],
        
    },
    format= "json",
)

# Transform data
processed_data = raw_data.drop_fields(["unnecessary_field1", "unnecessary_field2"])

# Write processed data back to S3
glueContext.write_dynamic_frame.from_options(
    processed_data,
    "s3",
    {
        "path": f"s3://{args['output_bucket']}/processed_data/",
        "partitionKeys": ["year", "month", "day"]
    },
    format="parquet"
)