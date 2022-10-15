from distutils.command.config import config
import boto3
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