import streamlit as st
import uuid
from langchain_core.messages import HumanMessage
from bot import get_knowledge_agent

# --- Page Config ---
st.set_page_config(page_title="Conversational Knowledge Bot", page_icon="🧠")
st.title("🧠 Conversational Knowledge Bot")
st.caption("Task 2: LangChain + Tools + Memory")

# --- Sidebar: Setup ---
api_key = st.sidebar.text_input("Enter Cohere API Key", type="password")



if not api_key:
    st.info("Please enter your LLM API key in the sidebar to continue.")
    st.stop()

# --- Initialize Agent ---
@st.cache_resource
def load_agent(key):
    
    return get_knowledge_agent(key)

try:
    agent = load_agent(api_key)
except Exception as e:
    st.error(f"Error initializing agent: {e}")
    st.stop()

# --- Memory Management ---
if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.messages = []

# Button to clear history
if st.sidebar.button("Reset Conversation"):
    st.session_state.thread_id = str(uuid.uuid4())
    st.session_state.messages = []
    st.rerun()

# --- Chat Interface ---
# 1. Display Chat History
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["content"])
    else:
        st.chat_message("assistant").write(msg["content"])

# 2. Handle User Input
if prompt := st.chat_input("Ask me something (e.g., Who is the CEO of OpenAI?)"):
    # Display user message
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Searching & Thinking..."):
            try:
                # Config with thread_id enables the Memory
                config = {"configurable": {"thread_id": st.session_state.thread_id}}
                
                # Invoke Agent
                response_dict = agent.invoke(
                    {"messages": [HumanMessage(content=prompt)]},
                    config=config
                )
                
                # Extract final response
                final_response = response_dict["messages"][-1].content
                message_placeholder.write(final_response)
                
                # Update Chat History
                st.session_state.messages.append({"role": "assistant", "content": final_response})

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")