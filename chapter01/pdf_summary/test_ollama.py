from langchain_ollama import ChatOllama

import config


def test_connection():
    print("=== Ollama 疎通確認テスト開始 ===")

    # 1. お使いのモデル名を指定（先ほどpullした正確な名前）
    # ※もし "qwen2.5:1.5b" であればそれに合わせてください
    model_name = config.LLM_MODEL

    print(f"1. ChatOllama を初期化中... (モデル: {model_name})")
    try:
        llm = ChatOllama(
            base_url=config.OLLAMA_BASE_URL,
            model=model_name,
            temperature=0,
            num_ctx=2048,
            think=False,
        )
    except Exception as e:
        print(f"❌ 初期化に失敗しました: {e}")
        return

    print(
        "2. Ollamaへメッセージを送信中...（ここで止まる場合はOllamaアプリが未起動かフリーズしています）"
    )
    try:
        # シンプルに一言だけ投げる
        for chunk in llm.stream("こんにちは"):
            print(chunk.content, end="", flush=True)

        print("================================")

    except Exception as e:
        print("\n❌ 通信エラーが発生しました！")
        print(f"エラー詳細: {e}")
        print("\n💡 【チェックポイント】")
        print("・Macの右上にラマのアイコン（Ollamaアプリ）は出ていますか？")
        print(f"・ターミナルで `ollama list` を叩いたとき、{model_name} は存在しますか？")
        print("================================")


if __name__ == "__main__":
    test_connection()
