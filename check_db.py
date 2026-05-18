from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(model="bge-m3")
vector_store = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)

results = vector_store.get(limit=10)

print("--- 登録されているテキスト一覧 ---")
for text in results["documents"]:
    print(f"📄: {text[:100]}...")  # 最初の100文字だけ表示
