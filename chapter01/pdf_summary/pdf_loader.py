from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

import config
from vector_store import save_to_vector_store


def load_and_split(file_path: str) -> list:
    """
    PDFを読み込み、チャンクに分割したドキュメントリストを返す
    """
    try:
        loader = PyPDFLoader(file_path)
        raw_document = loader.load()

        if not raw_document:
            print("警告：PDFからテキストを抽出できませんでした")
            return []

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=config.PDF_CHUNK_SIZE,
            chunk_overlap=config.PDF_CHUNK_OVERLAP,
            length_function=len,
            separators=["\n\n", "\n", "。", "、", " ", ""],
        )

        chunks = text_splitter.split_documents(raw_document)

        print(f"成功: {len(chunks)} 個のチャンクに分割されました。")
        return chunks

    except Exception as e:
        print(f"PDF読み込みエラー: {str(e)}")
        return []


def load_pdf(file_path: str) -> str:
    if not file_path:
        return "ファイルパスが無効です。"

    chunks = load_and_split(file_path)

    if chunks:
        success = save_to_vector_store(chunks)

        if success:
            return f"成功: {len(chunks)} 個のチャンクに分割され、ベクトルストア(Ollama: bge-m3)に格納されました！"
        else:
            return "PDFの分割はできましたが、ベクトルストアへの保存に失敗しました。"
    else:
        return "PDFの読み込みまたは分割に失敗しました。"
