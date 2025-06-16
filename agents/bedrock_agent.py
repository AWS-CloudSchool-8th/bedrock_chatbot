from chains.qa_chain import build_qa_chain
from retrievers.kb_retriever import get_kb_retriever, get_llm

# 검색 score 기준 (이하일 경우 실패로 간주)
RELEVANCE_THRESHOLD = 0.5

def answer_question(question: str):
    retriever = get_kb_retriever()
    llm = get_llm()

    docs = retriever.invoke(question)

    # Bedrock에서 반환한 score 확인
    high_quality_docs = [
        doc for doc in docs
        if doc.metadata.get("score", 1.0) >= RELEVANCE_THRESHOLD
    ]

    if high_quality_docs:
        print("📚 KB 검색 성공 → QA 체인 실행")
        qa_chain = build_qa_chain()
        response = qa_chain.invoke(question)

        # invoke 결과는 딕셔너리 -> 메타 데이터도 같이 출력
        # answer = response["result"] if isinstance(response, dict) else response

         # QA 체인은 dict 형태로 반환됨 → result만 추출
        answer = response["result"] if isinstance(response, dict) else str(response)
    else:
        print("🌐 KB 검색 실패 → Claude 단독 응답")
        # 메타 데이터도 같이 출력
        # answer = llm.invoke(question)

        response = llm.invoke(question)

        # Claude 응답 객체에서 content만 추출
        answer = response.content if hasattr(response, "content") else str(response)
        # ✅ 여기서 길이 제한 처리!
        # if len(answer) > 20:
        #     answer = answer[:20] + "..."

    return answer