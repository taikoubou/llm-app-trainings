# 実践LLMアプリケーション開発 演習リポジトリ

書籍「実践LLMアプリケーション開発」の演習用コードをまとめたリポジトリです。

## 📁 リポジトリ構成

```
llm-app-trainings/
├── pyproject.toml          # uvワークスペース設定
├── uv.lock                 # 依存関係ロックファイル
├── chapter01/
│   └── pdf_summary/        # PDF要約チャットボット
├── chapter02/
│   └── .../
└── .../
```

## 🛠️ 前提条件

- **Python**: 3.12.x
- **uv**: 最新版
- **Ollama**: 最新版（アプリを起動しておいてください）

## 🚀 セットアップ

### 1. uvのインストール

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. 依存関係のインストール

```bash
uv sync --all-extras
```

### 3. Ollamaモデルの取得

各演習で使用するモデルを取得してください。

```bash
# 埋め込みモデル
ollama pull bge-m3

# チャット・要約モデル
ollama pull qwen2.5:1.5b
```

## 📖 各章の内容

| 章         | テーマ                |
| ---------- | --------------------- |
| Chapter 01 | PDF要約チャットボット |
| Chapter 02 | (追加予定)            |

各章の詳細は章ごとの `README.md` を参照してください。

## ▶️ 演習の起動方法

```bash
# 演習のディレクトリに移動して起動
cd chapter01/pdf_summary
uv run python app.py
```

## 🔧 開発者向け

```bash
# コードのチェックと自動修正
ruff check --fix

# コードのフォーマット
ruff format
```

## 📝 補足

- 各演習の設定は `config.py` にまとめています。モデル名やパラメータは適宜変更してください。
- OllamaはデフォルトでHTTP `localhost:11434` で起動します。
