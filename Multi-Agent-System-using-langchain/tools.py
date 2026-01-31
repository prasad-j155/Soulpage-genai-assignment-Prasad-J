from langchain_community.tools import DuckDuckGoSearchRun

def fetch_sports_data(query: str):
    """
    Fetches real-time sports data using DuckDuckGo Search.
    No API Key required.
    """
    search = DuckDuckGoSearchRun()
    
    # We refine the query to ensure we get stats, not just news
    refined_query = f"{query} latest match stats score player performance injuries"
    
    print(f"🔎 SEARCHING WEB FOR: {refined_query}")
    
    try:
        # Run the search
        results = search.invoke(refined_query)
        return results
    except Exception as e:
        return f"Error fetching data: {e}"
    



    





def fetch_sports_data_2(query: str):
    """
    Simulates fetching live sports data.
    """
    query = query.lower()
    
    # Mock Data Responses
    if "lakers" in query or "lebron" in query:
        return """
        [SOURCE: NBA DB]
        - Status: Playoff Contention.
        - Last 5 Games: W-L-W-W-L.
        - Injuries: Anthony Davis (Probable), Vanderbilt (Out).
        - Key Stat: 2nd in League for Fast Break Points.
        """
    elif "united" in query or "manchester" in query:
        return """
        [SOURCE: PREMIER LEAGUE DB]
        - Status: mid-table struggle.
        - Recent Form: D-L-W-L-D.
        - Defense: Conceded 15 goals in last 10 games.
        - News: Manager Ten Hag facing criticism over tactics.
        """
    elif "kohli" in query or "india" in query:
        return """
        [SOURCE: CRICKET DB]
        - Form: Excellent (Avg 65.4 in 2024).
        - Recent Match: Scored 88 runs off 70 balls.
        - Fitness: cleared fitness test for upcoming tour.
        """
    else:
        return f"""
        [SOURCE: GENERAL SEARCH]
        - No deep analytics found for '{query}'.
        - General info: The entity is active but stats are hidden.
        """