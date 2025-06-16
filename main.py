#main.py
from tool.youtube_lambda import process_youtube_to_s3
from config.aws_config import S3_BUCKET, VIDCAP_API_KEY

import os

# 환경변수로 넣는 대신 직접 전달
os.environ["S3_BUCKET"] = S3_BUCKET
os.environ["VIDCAP_API_KEY"] = VIDCAP_API_KEY

if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=FWIAkfz8KhI"
    print("🚀 시작합니다...")
    try:
        s3_key = process_youtube_to_s3(youtube_url)
        print(f"✅ S3에 업로드 완료: {s3_key}")
    except Exception as e:
        print(f"❌ 실패: {str(e)}")