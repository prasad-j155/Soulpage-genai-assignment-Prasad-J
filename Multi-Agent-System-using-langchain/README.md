#  Sports Intelligence System



A multi-agent AI workflow that validates, researches, and analyzes sports entities (teams/athletes) in real-time. Built using LangGraph,LangChain, and Streamlit, powered by Groq Llama-3 models.

---

##  Architecture \& Flow



The system operates as a directed acyclic graph (DAG) where state is passed between specialized agents:



1\.  Gatekeeper (Llama-3.1-8b): Validates if the input is a legitimate sports entity.

2\.  Router: A conditional edge that terminates the process if the input is invalid or proceeds to the Scout.

3\.  Scout (DuckDuckGo Search): Performs real-time web scraping for latest match stats, injuries, and performance data.

4\.  Analyst (Llama-3.3-70b): Processes raw scout data to produce a concise 3-point performance report.



---

##  Getting Started

### Prerequisites

\- Python 3.9+

\- A Groq API Key (Get one at (https://console.groq.com/))

### Installation
To clone this repo: 
```bash
git clone https://github.com/prasad-j155/Soulpage-genai-assignment-Prasad-J.git
```

```bash

pip install -r Multi-Agent-System-using-langchain/requirements.txt

