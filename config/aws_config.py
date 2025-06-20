# config/aws_config.py
import os
AWS_REGION = "us-west-2"
YOUTUBE_LAMBDA_NAME = "aws8"
BEDROCK_KB_ID = os.environ.get("BEDROCK_KB_ID","8LPGWWQYCM")
BEDROCK_DS_ID = os.environ.get("BEDROCK_DS_ID","E33HDTF9XZ")
BEDROCK_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
S3_BUCKET = "s3-aws8"
S3_PREFIX = "transcripts/"
VIDCAP_API_KEY = "ab5b5ae2-ef1d-4ee8-bddc-b0099158391e"

#최강조 iam
# AWS_REGION = "us-west-2"
# YOUTUBE_LAMBDA_NAME = "lambda-aws8-yungee"
# BEDROCK_KB_ID = "UHK7B3B5ER" #오레곤 kb 이름 = "knowledge-base-quick-start-1ilvu"
# BEDROCK_DS_ID = "PEXU5NDGMU"
# BEDROCK_MODEL_ID = "anthropic.claude-3-5-sonnet-20241022-v2:0"
# S3_BUCKET = "s3-aws8-yungee"
# S3_PREFIX = "transcripts/"
# VIDCAP_API_KEY = "ab5b5ae2-ef1d-4ee8-bddc-b0099158391e"