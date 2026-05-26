from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings

import config


def get_embedding_model():
    """Ollamaの埋め込みモデルを初期化して返す"""
    return OllamaEmbeddings(model=config.EMBEDDING_MODEL)


def save_to_vector_store(chunks: list) -> bool:
    """
    分割されたチャンクをChromaDBに保存する
    """

    try:
        if not chunks:
            return False

        embeddings = get_embedding_model()

        Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=config.CHROMA_PERSIST_DIRECTORY,
        )

        print(f"ChromaDBへの保存が成功しました！({len(chunks)} チャンク)")
        return True

    except Exception as e:
        print(f"ベクトルストア保存エラー: {str(e)}")
        return False
