# import boto3

# def upload_log(bucket_name, file_name, data):
#     s3 = boto3.client('s3')
#     response = s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
#     print("Log uploaded:", response)import boto3

# def upload_log(bucket_name, file_name, data):
#     try:
#         s3 = boto3.client('s3')
#         response = s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
#         print("Log uploaded:", response)
#     except Exception as e:
#         print("Error uploading log:", str(e))

import boto3
import logging

logger = logging.getLogger(__name__)

def upload_log(bucket_name: str, file_name: str, data: str) -> None:
    """
    Upload a log to an Amazon S3 bucket.

    Args:
        bucket_name (str): The name of the S3 bucket.
        file_name (str): The name of the file to upload.
        data (str): The log data to upload.

    Returns:
        None
    """
    try:
        if not bucket_name or not file_name or not data:
            raise ValueError("Invalid input parameters")

        s3 = boto3.client('s3')
        response = s3.put_object(Bucket=bucket_name, Key=file_name, Body=data)
        logger.info("Log uploaded: %s", response)
    except botocore.exceptions.ClientError as e:
        logger.error("Error uploading log: %s", e)
    except Exception as e:
        logger.error("Unexpected error: %s", e)