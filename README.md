<p align = "center" draggable="false" ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>

## <h1 align="center" id="heading">TMLS 2025: AI Engineering Workshop Day</h1>

Welcome to AI Makerspace's comprehensive AI Engineering workshop! Today we'll explore three critical areas of modern AI development: **RAG in Practice**, **Agents with LangGraph**, and **Model Context Protocol (MCP)**.

## 🚀 Day Overview

This workshop is designed to take you from foundational concepts to production-ready implementations across three key AI engineering domains:

### 📚 Session 1: [RAG In Practice](./01_RAG_In_Practice/)
**Production-Ready RAG Applications for 2025**

While 2025 might be the year of agents for AI Engineers, it's the year of practical RAG for enterprise and AI Engineering leaders. We'll cover the minimum viable production-ready LLM app stack:

- **Two Implementation Tracks:**
  - [**RAG-In-Practice-2025**](./01_RAG_In_Practice/RAG-In-Practice-2025/) - Our recommended enterprise stack
  - [**RAG-In-Practice-2025-OSS**](./01_RAG_In_Practice/RAG-In-Practice-2025-OSS/) - Open-source focused implementation

**Key Technologies:**
- 🎺 **Orchestration**: LangChain's LangGraph
- ↗️ **Vector Database**: QDrant
- 📊 **Reranking**: Cohere's Rerank
- 📐 **Evaluation**: RAGAS

### 🤖 Session 2: [Agents](./02_Agents/)
**Building Intelligent Agents with LangGraph**

Dive deep into agentic AI systems with hands-on LangGraph development:

#### [01_Our_First_Agent_with_LangGraph](./02_Agents/01_Our_First_Agent_with_LangGraph/)
Create your first agentic RAG application covering:
- Tool belt creation
- State management
- Graph compilation and execution
- LangSmith evaluation

#### [02_Multi_Agent_with_LangGraph](./02_Agents/02_Multi_Agent_with_LangGraph/)
Advanced multi-agent systems and coordination patterns

### 🔌 Session 3: [MCP (Model Context Protocol)](./03_MCP/)
**Extending AI Capabilities with Custom Tools**

Learn to build custom MCP servers for enhanced AI interactions:

#### [MCP-Session-Code](./03_MCP/MCP-Session-Code/)
- Web search integration with Tavily API
- Custom tool development
- MCP server configuration in Cursor

## ⚡ Environment Setup Instructions

### 🔧 **IMPORTANT: UV Environment Usage**

Each session directory contains its own isolated `uv` environment. **You MUST navigate to each specific subdirectory and use its environment** for that session:

```bash
# For RAG sessions
cd 01_RAG_In_Practice/RAG-In-Practice-2025/
# or
cd 01_RAG_In_Practice/RAG-In-Practice-2025-OSS/

# For Agent sessions  
cd 02_Agents/01_Our_First_Agent_with_LangGraph/
# or
cd 02_Agents/02_Multi_Agent_with_LangGraph/

# For MCP session
cd 03_MCP/MCP-Session-Code/
```

### 🐍 Environment Activation

In each directory, you can:
- **Sync the environment**: `uv sync`

## 📋 Prerequisites

- **Python**: 3.11+ (3.13+ recommended for MCP)
- **UV Package Manager**: [Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)
- **API Keys**: You'll need various API keys (OpenAI, Cohere, Tavily, etc.) - check individual session READMEs

### Windows Users
For the MCP session specifically, ensure you have:
- `winget install astral-sh.uv`
- `winget install --id Git.Git -e --source winget`

## 🗓️ Suggested Schedule

1. **Morning**: RAG In Practice (Choose your track)
2. **Midday**: First Agent with LangGraph
3. **Afternoon**: Multi-Agent Systems or MCP Integration

## 🔗 Quick Navigation

| Session | Directory | Focus |
|---------|-----------|-------|
| RAG (Enterprise) | [`01_RAG_In_Practice/RAG-In-Practice-2025/`](./01_RAG_In_Practice/RAG-In-Practice-2025/) | Production RAG stack |
| RAG (OSS) | [`01_RAG_In_Practice/RAG-In-Practice-2025-OSS/`](./01_RAG_In_Practice/RAG-In-Practice-2025-OSS/) | Open-source RAG |
| First Agent | [`02_Agents/01_Our_First_Agent_with_LangGraph/`](./02_Agents/01_Our_First_Agent_with_LangGraph/) | Basic agentic RAG |
| Multi-Agent | [`02_Agents/02_Multi_Agent_with_LangGraph/`](./02_Agents/02_Multi_Agent_with_LangGraph/) | Advanced agents |
| MCP Tools | [`03_MCP/MCP-Session-Code/`](./03_MCP/MCP-Session-Code/) | Custom AI tools |

## 💡 Getting Help

- Each subdirectory contains detailed setup and usage instructions
- Check individual README files for session-specific requirements
- Ensure you're using the correct uv environment for each session

## 🎯 Learning Outcomes

By the end of today, you'll have:
- ✅ Built production-ready RAG applications
- ✅ Created intelligent agents with LangGraph
- ✅ Developed custom MCP tools
- ✅ Understood evaluation and monitoring strategies
- ✅ Gained hands-on experience with the latest AI engineering tools

---

**Ready to build the future of AI? Let's get started! 🚀**
