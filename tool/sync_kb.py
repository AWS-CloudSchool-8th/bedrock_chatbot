# tools/sync_kb.py

import boto3
import json
from botocore.exceptions import ClientError
from config.aws_config import AWS_REGION, BEDROCK_KB_ID, BEDROCK_DS_ID

def sync_kb():
    print("===== Lambda sync_kb ENTRY =====")
    print("MODULE FILE:", __file__)
    print("BEDROCK_DS_ID current:", BEDROCK_DS_ID, type(BEDROCK_DS_ID))
    print("BEDROCK_KB_ID current:", BEDROCK_KB_ID, type(BEDROCK_KB_ID))

    kb_client = boto3.client("bedrock-agent", region_name=AWS_REGION)

    # ① 진행 중인 Job 확인
    jobs = kb_client.list_ingestion_jobs(
        knowledgeBaseId=BEDROCK_KB_ID,
<<<<<<< HEAD
        dataSourceId=BEDROCK_DS_ID
    )
    for job in jobs.get("ingestionJobSummaries", []):
        if (
            str(job.get("dataSourceId")) == str(BEDROCK_DS_ID) and
            job.get("status") in ["STARTING", "IN_PROGRESS", "COMPLETE"]
        ):
            job_id = job["ingestionJobId"]
            print(f"⚠️ 진행 중인 Job이 있습니다: {job_id} → 재사용")
            return str(job_id)

    # ② 새로 요청
    try:
        # AWS Bedrock Agent API의 정확한 파라미터명 사용 (camelCase)
        params = {
            "knowledgeBaseId": str(BEDROCK_KB_ID),
            "dataSourceId": str(BEDROCK_DS_ID)
        }
        print("🚀 새로운 Ingestion Job 시작 요청...")
        print("Calling start_ingestion_job params:", params)
        print("파라미터 타입:", {k: type(v) for k, v in params.items()})
        print("파라미터 값 확인:")
        print(f"  knowledgeBaseId: '{params['knowledgeBaseId']}' (길이: {len(params['knowledgeBaseId'])})")
        print(f"  dataSourceId: '{params['dataSourceId']}' (길이: {len(params['dataSourceId'])})")

        response = kb_client.start_ingestion_job(**params)
        job_id = response["ingestionJob"]["ingestionJobId"]
        print("✅ Job Started:", job_id)
        return str(job_id)

    except ClientError as e:
        print("❌ AWS CLIENT ERROR 발생")
        print("💥", str(e))
        print("🧪 RAW AWS RESPONSE:", json.dumps(e.response, indent=2, ensure_ascii=False))
        raise
    except Exception as e:
        print("❌ 일반 EXCEPTION 발생")
        print("💥", str(e))
        raise
=======
        dataSourceId=" ",  # 연결된 Data Source ID
    )
>>>>>>> 981a24c257b8da31c748f11863f4396c00719a2d
