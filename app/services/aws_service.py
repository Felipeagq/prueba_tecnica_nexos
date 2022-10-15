from distutils.command.config import config
import boto3
from boto3 import client
from botocore.config import Config
from botocore.exceptions import ClientError

from app.settings.settings import settings

def cliente_aws(
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
    service
):
    aws_client = boto3.client(
        service,
        config = Config(signature_version="s3v4"),
        region_name="us-east-1",
        aws_access_key_id=ACCESS_KEY_ID,
        aws_secret_access_key=SECRET_ACCESS_KEY
    )
    return aws_client


def upload_to_s3(
    aws_client,
    file_data,
    bucket_name,
    file_name
):
    response = aws_client.put_object(
        # ACL="public-read",
        Body=file_data,
        Bucket=bucket_name,
        Key=file_name
    )
    return response