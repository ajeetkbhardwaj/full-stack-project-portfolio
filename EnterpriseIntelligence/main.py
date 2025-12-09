import asyncio
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.prebuilt import create_react_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv()

# Config
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

async def main():
    # 1. Initialize MCP Client to connect to BOTH servers
    # We use 'stdio' transport to run the python scripts directly
    async with MultiServerMCPClient({
        "knowledge": {
            "command": "python",
            "args": ["servers/knowledge.py"],
            "transport": "stdio"
        },
        "actions": {
            "command": "python",
            "args": ["servers/actions.py"],
            "transport": "stdio"
        }
    }) as client:

        # 2. Load all tools from connected MCP servers
        print("🔌 Connecting to MCP Servers...")
        tools = await client.get_tools()
        print(f"✅ Loaded {len(tools)} tools: {[t.name for t in tools]}")

        # 3. Initialize Gemini LLM
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

        # 4. Create LangGraph Agent
        # The agent can now "see" the RAG tool and the Math tool equally
        agent = create_react_agent(llm, tools)

        # 5. Execute Complex Query
        # Scenario: "Look up the policy for bonuses, then calculate it for an employee."
        query = (
            "According to the company policy documents, what are the criteria for a high performance score? "
            "Then, assuming an employee has a salary of $100,000 and meets those criteria (score 4.8), "
            "calculate their bonus."
        )
        
        print("\n🤖 Agent Thinking...\n")
        
        # Stream the graph events
        async for chunk in agent.astream({"messages": [HumanMessage(content=query)]}, stream_mode="values"):
            chunk["messages"][-1].pretty_print()

if __name__ == "__main__":
    asyncio.run(main())