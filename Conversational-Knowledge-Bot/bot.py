import os
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_cohere import ChatCohere
# --- 1. Define the Search Tool ---
@tool
def web_search(query: str) -> str:
    """
    Search the web for current factual information, news, or people.
    Use this tool when you don't know the answer or need real-time data.
    """
    search_tool = DuckDuckGoSearchRun()
    print(f"\n[Tool Call] Searching DuckDuckGo for: '{query}'...")
    return search_tool.run(query)

# --- 2. Agent Factory ---
def get_knowledge_agent(api_key: str):
    """
    Creates a Conversational Knowledge Bot that can search and remember.
    """
    if not api_key:
        raise ValueError("Groq API Key is missing")

    # Switched to ChatCohere due to Groq rate limits.
    # Note: Groq (llama-3.3-70b) currently has tool-calling issues, 
    # returning incorrectly formatted tags (e.g., < >) in the output(we can handle that as well).


    """
    model = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key,
        max_retries=2
    )

    llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash", 
    google_api_key=api_key,
    max_retries=6,
    timeout=60
    )
"""
    

    llm = ChatCohere(
    model="command-a-03-2025", 
    cohere_api_key=api_key
    )

# 3. For even better results, wrap it in the .with_retry() method
# This uses a more sophisticated exponential backoff algorithm

    
    
    # Initialize Memory (The "Checkpointer")
    checkpointer = InMemorySaver()

    # Define System Prompt
    # Crucial for Llama 3 to use tools correctly without XML errors
    system_prompt = (
        "You are a smart Conversational Knowledge Bot. "
        "You have access to a 'web_search' tool. "
        "1. If the user asks a factual question (e.g., 'Who is CEO of X?'), call the tool. "
        "2. If the user asks a follow-up (e.g., 'Where did he study?'), use your memory to understand who 'he' is. "
        "3. Do NOT output XML tags like <function>. Call the tool directly."
    )

    # Create the Agent using strictly 'create_agent'
    agent = create_agent(
        model=llm,
        tools=[web_search],
        checkpointer=checkpointer,
        system_prompt=system_prompt
    )

    return agent