from retrievers.kb_retriever import get_kb_retriever, get_llm
from langchain.chains import RetrievalQA

if __name__ == "__main__":
    retriever = get_kb_retriever()
    llm = get_llm()

    chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    query = input("❓ 질문을 입력하세요: ")
    result = chain.invoke({"query": query})
    print("\n🧠 답변:", result["result"])
    print("\n📚 참고 문서:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source"))