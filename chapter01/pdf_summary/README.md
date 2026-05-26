## 概要

これはPDFの要約アプリの作成演習用のコードです。
Ollamaを用いているため本で紹介されているライブラリをちょっと変えたような気がします。
たぶん気にしなくて大丈夫です、動いているので。

## 📋 前提条件 (Prerequisites)

このプロジェクトは、以下の環境で動作確認を行っています。

- **OS**: macOS (M1/M2/M3 シリーズ推奨、Windows/Linuxでも動作可)
- **Python**: `3.12.x` (推奨)
- **Ollama**: 最新版 (アプリ版を起動しておいてください)

## 🚀 セットアップと起動方法

このプロジェクトは、高速な Python パッケージマネージャーである `uv` を使用しています。

### 仮想環境（.venv）を作成

`uv venv`

### 仮想環境をアクティベート（Mac / Linux）

`source .venv/bin/activate`

### ライブラリのインストール

`uv pip install -e '.[dev]'`

### 埋め込み用モデルの取得

`ollama pull bge-m3`

### チャット・要約用モデルの取得

`ollama pull qwen2.5:1.5b`

### 実行

`chapter01/pdf_summary`に移動してから`uv run python app.py`
またはプロジェクト直下で `uv run --package pdf-summary python chapter01/pdf_summary/app.py`

### 🛠️ 開発者向け：コードの整形 (Ruff)

```bash
# コードのチェックと自動修正
ruff check --fix

# コードのフォーマット（見た目の整形）
ruff format
```

### 追記

- 環境変数はconfig.pyにまとめているので適宜変えてください
- gr.State で履歴を管理するようにするかも（実験用だったので今回は入れてない）
