# test_fallback.py

from agents.bedrock_agent import answer_question

def run_test():
    print("=== Claude Fallback 테스트 ===")
    print("엔터를 누르면 종료됩니다.\n")

    while True:
        question = input("❓ 질문 입력: ").strip()
        if question == "":
            print("⛔ 종료합니다.")
            break

        print("\n⏳ 응답 생성 중...\n")
        answer = answer_question(question)
        print("✅ Claude 응답:\n", answer)
        print("\n" + "-" * 50 + "\n")

if __name__ == "__main__":
    run_test()