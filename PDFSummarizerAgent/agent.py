import nest_asyncio
nest_asyncio.apply()

from config import API_KEY
from llama_index.llms.openrouter import OpenRouter
from llama_index.core import Settings
from llama_index.agent.introspective import (
    SelfReflectionAgentWorker,
    IntrospectiveAgentWorker
)
from llama_index.core.llms import ChatMessage, MessageRole
from llama_index.readers.file import PyMuPDFReader
import asyncio

# ----------------------------------------------------
# Setup LLM = OpenRouter GPT-OSS 20B (free tier)
# ----------------------------------------------------
Settings.llm = OpenRouter(
    api_key=API_KEY,
    max_tokens=256,
    context_window=4096,
    model="openai/gpt-oss-20b:free"
)

# ----------------------------------------------------
# Build Introspective Agent
# ----------------------------------------------------
def build_agent():
    reflection_worker = SelfReflectionAgentWorker.from_defaults(
        llm=Settings.llm,
        verbose=True,
    )

    introspection_worker = IntrospectiveAgentWorker.from_defaults(
        reflective_agent_worker=reflection_worker,
        main_agent_worker=None,
        verbose=True,
    )

    system_prompt = """
    You are a Product Specification Summarizer.
    Summarize the input text in **less than 50 words**.
    Focus strictly on:
    - performance specifications
    - safety features
    Do NOT add anything outside the given content.
    """

    chat_history = [
        ChatMessage(content=system_prompt, role=MessageRole.SYSTEM)
    ]

    agent = introspection_worker.as_agent(
        chat_history=chat_history,
        verbose=True
    )
    return agent


# ----------------------------------------------------
# PDF Summarization Function
# ----------------------------------------------------
async def summarize_pdf(pdf_path):
    loader = PyMuPDFReader()
    docs = loader.load(file_path=pdf_path)

    text = docs[0].text                   # first page
    agent = build_agent()

    response = await agent.achat(text)
    return response.response
