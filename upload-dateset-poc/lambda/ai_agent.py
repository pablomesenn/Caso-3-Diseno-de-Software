import os
import boto3
import json

def handler(event, context):
    print("Lambda triggered by Glue job completion!")
    print(f"Event: {json.dumps(event, indent=2)}")
    
    s3 = boto3.client('s3')
    bucket = os.environ['PROCESSED_DATA_BUCKET']
    
    try:
        # List processed data files
        response = s3.list_objects_v2(Bucket=bucket, Prefix='processed_data/')
        
        if 'Contents' in response:
            print(f"Found {len(response['Contents'])} processed files:")
            for obj in response['Contents']:
                print(f"  - {obj['Key']} (Size: {obj['Size']} bytes)")
        else:
            print("No processed files found yet.")
            
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Data processed successfully',
                'files_found': len(response.get('Contents', []))
            })
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }