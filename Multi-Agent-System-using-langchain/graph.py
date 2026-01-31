from langgraph.graph import StateGraph, END
from state import SportsState
from agents import scout_node, analyst_node, gatekeeper_node # Make sure to add gatekeeper_node to agents.py

# 1. Initialize the Graph
workflow = StateGraph(SportsState)

# 2. Add the Workers (Nodes)
workflow.add_node("gatekeeper", gatekeeper_node) # New Gatekeeper node
workflow.add_node("scout", scout_node)
workflow.add_node("analyst", analyst_node)

# 3. Define the Workflow Logic

# Start -> Gatekeeper
workflow.set_entry_point("gatekeeper")

# Define the branching logic
def decide_to_scout(state: SportsState):
    """
    This function looks at the 'is_valid' flag set by the gatekeeper
    to decide whether to continue or stop.
    """

    print('state.get:',state.get("is_valid"))
    if state.get("is_valid"):
        return "scout"
    
    
    return END # Exit immediately if input is random/invalid

# Add the Conditional Edge (The Decision point)
workflow.add_conditional_edges(
    "gatekeeper",
    decide_to_scout
)

# Scout -> Analyst (Only happens if gatekeeper passed)
workflow.add_edge("scout", "analyst")

# Analyst -> End
workflow.add_edge("analyst", END)

# 4. Compile the App
app = workflow.compile()