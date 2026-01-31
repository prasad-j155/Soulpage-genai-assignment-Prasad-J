from typing import TypedDict

# This dictionary acts as the memory for the system.
# It holds the input (entity_name) and the outputs from both agents.
class SportsState(TypedDict):
    entity_name: str    # Input: e.g., "Hardik Pandya"
    scout_data: str     # Output from Agent 1
    analyst_report: str # Output from Agent 2
    is_valid: bool  

