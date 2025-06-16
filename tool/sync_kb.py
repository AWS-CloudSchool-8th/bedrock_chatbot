#tool/sync_kb.py
import boto3
from config.aws_config import AWS_REGION, BEDROCK_KB_ID
def sync_kb():
    kb_client = boto3.client("bedrock-agent", region_name=AWS_REGION)
    response = kb_client.start_ingestion_job(
        knowledgeBaseId=BEDROCK_KB_ID,
        dataSourceId="JMG9NFQW5H",  # 연결된 Data Source ID
    )