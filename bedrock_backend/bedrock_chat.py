import os
import boto3
from langchain_aws import ChatBedrock

def create_bedrock_client(region: str = "us-west-2"):
    return boto3.client("bedrock-runtime", region_name=region)

def main():
    bedrock_client = create_bedrock_client()

    model_id = "anthropic.claude-3-5-sonnet-20241022-v2:0"

    llm = ChatBedrock(
    client=bedrock_client,
    model_id=model_id,
    model_kwargs={"temperature": 0.7, "max_tokens": 512}
)
    print("💬 챗봇 실행 중... 종료하려면 빈 입력 후 Enter 누르세요.\n")

    while True:
        prompt = input("You: ").strip()
        if not prompt:
            print("챗봇을 종료합니다.")
            break

        # invoke() 직접 사용
        response = llm.invoke(prompt)
        print("Bot:", response.content)  # Claude는 response.content에 답변이 있어요

if __name__ == "__main__":
    main()