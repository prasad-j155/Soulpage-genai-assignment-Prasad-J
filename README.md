#  Multi-Agent AI Suite



A collection of advanced AI agents and conversational bots built with \*\*LangChain\*\*, \*\*LangGraph\*\*, and \*\*Streamlit\*\*. This repository contains two distinct projects showcasing different agentic architectures.



---



##  Project Directory



#### Multi-Agent-System/
  - &nbsp;app.py              - Streamlit UI \& Entry Point
  - &nbsp;agents.py           - Logic for Gatekeeper, Scout, and Analyst nodes
  - &nbsp;graph.py            - LangGraph workflow definition and state machine
  - &nbsp;state.py            - TypedDict defining the shared agent memory
  - &nbsp;tools.py            - Search tools for real-time data retrieval
  - &nbsp;requirements.txt    - Python dependencies
  - &nbsp;README.md           - Project documentation
  - &nbsp;sports\_analysis.ipynb - Reproducibility notebook


#### Conversational-Knowledge-Bot/
- &nbsp; main.py           - Streamlit UI \& Application Logic 
- &nbsp; bot.py            - Agent Factory, LLM configuration, and Tools
- &nbsp; requirements.txt  - Python dependencies with versions
- &nbsp; README.md         - Documentation (Architecture, Setup, Usage)
&nbsp;

---
### 1.  Multi-Agent-System : Sports Intelligence System

- A multi-agent workflow that validates, researches, and analyzes sports entities in real-time
- Architecture: Hierarchical (Gatekeeper -> Scout -> Analyst).
- Key Tech: LangGraph, Groq Llama 3, DuckDuckGo Search.

- [Go to Project Folder](./Multi-Agent-System-using-langchain)



### 2.  Conversational Knowledge Bot

- A persistent chat agent with long-term memory and web-searching capabilities.

- Architecture: Stateful Agent Executor with Checkpointing.

- Key Tech: Cohere, LangGraph Memory, DuckDuckGo.

- [Go to Project Folder](./Conversational-Knowledge-Bot)



---



##  Quick Start (Root Setup)



### Prerequisites

- Python 3.9+

- API Keys: Groq, Cohere, or Google (depending on the project you run)



### Global Installation

To clone this repo: 
```bash
git clone https://github.com/prasad-j155/Soulpage-genai-assignment-Prasad-J.git
```

To install the dependencies for both projects at once:

```bash

pip install -r Multi-Agent-System-using-langchain/requirements.txt

pip install -r Conversational-Knowledge-Bot/requirements.txt

