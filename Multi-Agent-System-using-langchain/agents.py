import os
from langchain_groq import ChatGroq
from state import SportsState
from tools import fetch_sports_data



# --- NEW: THE GATEKEEPER ---
def gatekeeper_node(state: SportsState):
    entity = state["entity_name"]
    api_key = os.environ.get("GROQ_API_KEY")
    
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, api_key=api_key)
    
    prompt = f"""
    Analyze the following text: "{entity}"
    Is this text a name of a sports team, a professional athlete, or a sports organization?
    Respond with ONLY 'TRUE' if it is sports-related, or 'FALSE' if it is random text, a sentence, or unrelated.
    """
    
    response = llm.invoke(prompt).content.strip().upper()
    
    if "TRUE" in response:
        #print("true")
        return {"is_valid": True}
    else:
        #print("false")
        return {
            "is_valid": False, 
            "analyst_report": "⚠️ Invalid Input: Please enter a specific team or athlete name (e.g.,'Indian cricket team', 'Virat Kohli' or 'Messi')."
        }
# --- AGENT 1: THE SCOUT ---

def scout_node(state: SportsState):
    entity = state["entity_name"]
    print(f"--- SCOUT: Gathering info for {entity} ---")
    
    # Use the tool from tools.py
    results = fetch_sports_data(entity)
    
    return {"scout_data": results}

# --- AGENT 2: THE ANALYST ---
def analyst_node(state: SportsState):
    print("--- ANALYST: analyzing patterns ---")
    
    # Check if Key is available
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        return {"analyst_report": "Error: Groq API Key is missing. Please enter it in the sidebar."}

    # --- LAZY INITIALIZATION ---
    # We create the connection HERE, only when needed
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        api_key=api_key
    )
    
    # Read data from the state
    data = state["scout_data"]
    entity = state["entity_name"]
    
    prompt = f"""
    You are a Sports Performance Analyst.
    Review this raw data for {entity}:
    {data}
    
    Write a concise 3-point report:
    1. Current Form (Good/Bad?)
    2. Major Risk Factor (Injuries/Tactics)
    3. Prediction for next match.
    """
    
    try:
        response = llm.invoke(prompt)
        return {"analyst_report": response.content}
    except Exception as e:
        return {"analyst_report": f"Error calling Groq: {e}"}