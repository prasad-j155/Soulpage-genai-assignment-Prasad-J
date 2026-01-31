\# 🤖 Multi-Agent AI Suite



A collection of advanced AI agents and conversational bots built with \*\*LangChain\*\*, \*\*LangGraph\*\*, and \*\*Streamlit\*\*. This repository contains two distinct projects showcasing different agentic architectures.



---



\## 📂 Project Directory



Multi-Agent-System/

  app.py              - Streamlit UI \& Entry Point

  agents.py           - Logic for Gatekeeper, Scout, and Analyst nodes

  graph.py            - LangGraph workflow definition and state machine

  state.py            - TypedDict defining the shared agent memory

  tools.py            - Search tools for real-time data retrieval

  requirements.txt    - Python dependencies

  README.md           - Project documentation

  sports\_analysis.ipynb - Reproducibility notebook







Conversational-Knowledge-Bot/

&nbsp; main.py           - Streamlit UI \& Application Logic 

&nbsp; bot.py            - Agent Factory, LLM configuration, and Tools

&nbsp; requirements.txt  - Python dependencies with versions

&nbsp; README.md         - Documentation (Architecture, Setup, Usage)

&nbsp;









\### 1.  Sports Intelligence System

A multi-agent workflow that validates, researches, and analyzes sports entities in real-time

\* \*\*Architecture:\*\* Hierarchical (Gatekeeper -> Scout -> Analyst).

\* \*\*Key Tech:\*\* LangGraph, Groq Llama 3, DuckDuckGo Search.

\* \*\*\[Go to Project Folder](./SPORTS-AGENT-PROJECT)\*\*



\### 2.  Conversational Knowledge Bot

A persistent chat agent with long-term memory and web-searching capabilities.

\* \*\*Architecture:\*\* Stateful Agent Executor with Checkpointing.

\* \*\*Key Tech:\*\* Cohere, LangGraph Memory, DuckDuckGo.

\* \*\*\[Go to Project Folder](./CHATBOT-AI)\*\*



---



\##  Quick Start (Root Setup)



\### Prerequisites

\- Python 3.9+

\- API Keys: Groq, Cohere, or Google (depending on the project you run)



\### Global Installation

To install the dependencies for both projects at once:

```bash

pip install -r SPORTS-AGENT-PROJECT/requirements.txt

pip install -r CHATBOT-AI/requirements.txt

