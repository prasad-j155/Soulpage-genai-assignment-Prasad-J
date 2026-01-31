#  Conversational Knowledge Bot



A production-ready conversational agent built with LangChain, LangGraph, and Streamlit. This bot features real-time web search capabilities and persistent conversational memory.



##  Architecture



The system follows a stateful agentic workflow:



1\.  Frontend (Streamlit):Manages user session state, chat history rendering, and secure API key handling.

2\.  Orchestration (LangGraph):Uses a pre-built agent executor that manages the loop between the LLM and its tools.

3\.  LLM (Cohere/Groq/Gemini): Configurable backend (currently set to Cohere `command-a-03-2025`).

4\.  Tools (DuckDuckGo):Enables the bot to fetch live factual data when its internal knowledge is insufficient.

5\.  Memory (InMemorySaver):Provides "Checkpointer" functionality to retain context across a single session using a `thread\_id`.





##  Getting Started



### Prerequisites

\- Python 3.9 or higher

\- API Key for your chosen provider (Cohere, Groq, or Google)



### Installation

1\. Clone the repository:


```bash
git clone https://github.com/prasad-j155/Soulpage-genai-assignment-Prasad-J.git
```

To install the dependencies for both projects at once:

```bash

pip install -r Conversational-Knowledge-Bot/requirements.txt

