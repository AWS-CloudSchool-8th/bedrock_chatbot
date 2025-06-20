# config/aws_config.py
import os
AWS_REGION = "us-west-2"
YOUTUBE_LAMBDA_NAME = "aws8"
BEDROCK_KB_ID = os.environ.get("BEDROCK_KB_ID","")
BEDROCK_DS_ID = os.environ.get("BEDROCK_DS_ID","")
BEDROCK_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
S3_BUCKET = "s3-aws8"
S3_PREFIX = "transcripts/"
VIDCAP_API_KEY = ""