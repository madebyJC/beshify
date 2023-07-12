import gradio as gr


def beshify(text):
    return text.replace(" ", "🤸")


demo = gr.Interface(fn=beshify,
                    inputs="text",
                    outputs="text",
                    title="Beshify🤸",
                    allow_flagging="never")

if __name__ == "__main__":
    demo.launch(share=False)
