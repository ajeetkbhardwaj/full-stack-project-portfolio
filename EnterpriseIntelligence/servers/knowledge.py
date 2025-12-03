from mcp.server.fastmcp import FastMCP
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.google import GooglePaLMEmbedding
import os

# 1. Setup LlamaIndex Settings (Use Gemini for RAG reasoning too!)
os.environ["GOOGLE_API_KEY"] = "YOUR_GEMINI_KEY"
Settings.llm = Gemini(model="models/gemini-1.5-pro")
Settings.embedding = GooglePaLMEmbedding(model_name="models/embedding-001")

# 2. Load Documents (Create a 'data' folder and put a PDF inside)
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()

# 3. Create MCP Server
mcp = FastMCP("KnowledgeServer")

@mcp.tool()
def query_company_policy(query: str) -> str:
    """
    Queries the internal company policy documents. 
    Use this tool when the user asks about rules, holidays, or internal documentation.
    """
    response = query_engine.query(query)
    return str(response)

if __name__ == "__main__":
    # Run as a standard server
    mcp.run(transport="stdio")