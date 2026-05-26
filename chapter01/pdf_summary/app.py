import gradio as gr

from llm_bot import respond
from pdf_loader import load_pdf


def main():
    with gr.Blocks(title="Chat with Your PDF") as demo:
        gr.Markdown("# Chat with Your PDF")
        gr.Markdown("PDFファイルをアップロードし、質問して内容を要約してもらいましょう")

        with gr.Row():
            with gr.Column(scale=1):
                pdf_upload = gr.File(
                    label="PDFをアップロード",
                    file_types=[".pdf"],
                    type="filepath",
                    file_count="single",
                )
                upload_status = gr.Textbox(label="ステータス", interactive=False)
                pdf_upload.change(fn=load_pdf, inputs=[pdf_upload], outputs=[upload_status])

            with gr.Column(scale=2):
                chatbot = gr.Chatbot(label="チャット", height=500)

                with gr.Row():
                    msg = gr.Textbox(
                        label="PDFへの質問を入力してください",
                        placeholder="このPDFの重要なポイントを3つで要約して？",
                        show_label=True,
                        scale=4,
                    )

                with gr.Row():
                    submit_btn = gr.Button("送信", variant="primary", scale=1)
                    clear_btn = gr.Button("クリア", variant="secondary", scale=1)

                msg.submit(fn=respond, inputs=[msg, chatbot], outputs=[chatbot]).then(
                    fn=lambda: "", outputs=[msg]
                )

                msg.submit(fn=lambda: "", inputs=None, outputs=[msg])

                submit_btn.click(fn=respond, inputs=[msg, chatbot], outputs=[chatbot]).then(
                    fn=lambda: "", outputs=[msg]
                )

                submit_btn.click(fn=lambda: "", inputs=None, outputs=[msg])

                clear_btn.click(fn=lambda: [], inputs=None, outputs=[chatbot])

    demo.launch(server_name="0.0.0.0", server_port=7860, share=False, theme=gr.themes.Soft())


if __name__ == "__main__":
    main()
