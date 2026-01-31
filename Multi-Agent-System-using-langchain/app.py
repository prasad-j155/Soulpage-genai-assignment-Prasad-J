import streamlit as st
import os
from graph import app  # Import compiled graph

st.set_page_config(page_title="Sports AI", page_icon="⚽")

st.title("⚽ Sports Intelligence System")
st.markdown("### Multi-Agent Workflow: Scout -> Analyst")

# Sidebar for API Key
api_key = st.sidebar.text_input("Groq API Key", type="password")
if api_key:
    os.environ["GROQ_API_KEY"] = api_key



# User Input
team = st.text_input("Enter Team/Athlete Name (e.g., Lakers, Manchester United):", "Lakers")

if st.button("Run Analysis"):
    if not os.environ.get("GROQ_API_KEY"):
        st.error("Please provide a Groq API Key in the sidebar.")
    else:
        with st.spinner("Agents are collaborating..."):
            try:
                # Invoke the Graph
                final_state = app.invoke({"entity_name": team})
                
                # Display Results
                st.success("Analysis Complete")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("📋 Scout Data")
                    st.info(final_state["scout_data"])
                    
                with col2:
                    st.subheader("🧠 Analyst Report")
                    st.markdown(final_state["analyst_report"])
                    
            except Exception as e:
                st.error(f"Error: {e}")