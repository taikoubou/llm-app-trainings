import os

from langchain_community.vectorstores import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings

import config


def respond(message: str, history: list) -> list:
    """
    ユーザの質問に対して、VecotrDBから情報を検索し、Qwenで回答する
    """

    user_query = message

    if not os.path.exists(config.CHROMA_PERSIST_DIRECTORY):
        history.append({"role": "user", "content": user_query})
        history.append(
            {
                "role": "assistant",
                "content": "まずは左側からPDFファイルをアップロードしてください。",
            }
        )
        return history

    try:
        # ベクトルDBに情報検索してる
        embeddings = OllamaEmbeddings(model=config.EMBEDDING_MODEL)
        vector_store = Chroma(
            persist_directory=config.CHROMA_PERSIST_DIRECTORY, embedding_function=embeddings
        )
        docs = vector_store.similarity_search(user_query, config.TOP_K)

        # ヒットした該当テキストを合体
        context_text = "\n\n".join([doc.page_content for doc in docs])

        # LLM(Qwen)に渡すプロンプト
        system_prompt = f"""あなたはアップロードされたPDFの内容を解説する優秀なAIアシスタントです。
以下の【PDFの抜粋データ】をよく読んで、ユーザーの質問に対する回答や要約を、日本語で分かりやすく作成してください。

【PDFの抜粋データ】:
{context_text}
"""
        formatted_user_query = (
            f"上記の【PDFの抜粋データ】をもとに、次の要求に答えてください：\n「{user_query}」"
        )

        print("\n===== [DEBUG] ベクトルDBからの検索結果 =====")
        print(system_prompt)
        print("===========================================\n")
        # OllamaのQwenモデルの呼び出し
        llm = ChatOllama(
            base_url=config.OLLAMA_BASE_URL, model=config.LLM_MODEL, temperature=config.TEMPERATURE
        )

        # システムプロンプト + 過去の履歴 + 最新の質問を結合
        messages = (
            [{"role": "system", "content": system_prompt}]
            + history
            + [{"role": "user", "content": formatted_user_query}]
        )

        history.append({"role": "user", "content": user_query})
        history.append({"role": "assistant", "content": ""})
        yield history

        # AIの回答生成
        response_stream = llm.stream(messages)

        for chunk in response_stream:
            history[-1]["content"] += chunk.content
            yield history
    except Exception as e:
        history.append({"role": "user", "content": user_query})
        history.append({"role": "assistant", "content": f"エラーが発生しました: {str(e)}"})
        yield history
