# Enterprise Intelligence Nexus



```mermaid
graph TD
    User[User Query] --> LG[LangGraph Orchestrator (Client)]
    LG -- Gemini API --> LLM[Gemini 1.5 Pro]

    subgraph "MCP Layer"
        LG -- MCP Protocol --> S1[MCP Server 1: Knowledge]
        LG -- MCP Protocol --> S2[MCP Server 2: Tools]
    end

    S1 --> LI[LlamaIndex RAG Engine]
    LI --> Docs[Local PDF/Data Store]

    S2 --> Tools[Python Functions/APIs]
```