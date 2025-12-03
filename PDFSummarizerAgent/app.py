import gradio as gr
import asyncio
from agent import summarize_pdf

async def run_summary(pdf):
    if pdf is None:
        return "Please upload a PDF file."

    return await summarize_pdf(pdf.name)

def interface(pdf):
    return asyncio.run(run_summary(pdf))

demo = gr.Interface(
    fn=interface,
    inputs=gr.File(label="Upload Product Specification PDF"),
    outputs=gr.Textbox(label="Summarized Output"),
    title="Introspective Summarizer (OpenRouter GPT-OSS)",
    description="Upload a PDF; it will extract the first page, introspect, reflect, and summarize in < 50 words."
)

demo.launch()
