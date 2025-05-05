# chat_case_builder.py

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Conversational Case Builder", layout="wide")

if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.dataset = None
    st.session_state.goal = ""
    st.session_state.problem = ""
    st.session_state.cleaning = ""
    st.session_state.insights = ""

# Agent logic
class ConversationalCaseAgent:
    def reply(self, user_input):
        if "upload" in user_input.lower():
            return "Please upload your dataset using the uploader below."
        if "analyze" in user_input.lower():
            return "Great. Could you describe the goal of your analysis?"
        if "clean" in user_input.lower():
            return "Sure. I can recommend steps like removing nulls, formatting dates, or deduplicating rows. Do you want that now?"
        if "insight" in user_input.lower() or "summary" in user_input.lower():
            return "I’ll summarize key patterns and findings once your dataset is ready."
        if user_input.lower() in ["yes", "okay", "go ahead"] and st.session_state.dataset is not None:
            return "Let me inspect the dataset. What kind of patterns or business goals are you exploring?"
        return "Can you tell me more about your objective or what you'd like to find out from the data?"

agent = ConversationalCaseAgent()

st.title("🧠 Conversational Case Study Builder")
st.write("Talk to the agent to explore your dataset, define your problem, and generate a case study.")

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question or describe your analysis goal...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    agent_reply = agent.reply(user_input)
    st.session_state.messages.append({"role": "assistant", "content": agent_reply})
    with st.chat_message("assistant"):
        st.markdown(agent_reply)

# File upload
uploaded_file = st.file_uploader("📁 Upload your dataset (CSV only):", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state.dataset = df
    st.session_state.messages.append({"role": "assistant", "content": "✅ Dataset uploaded! Here's a preview:"})
    st.dataframe(df.head())

# Future enhancement areas:
# - Analyze and extract column suggestions
# - Support multi-turn logic (extract goal, suggest analyses, auto-generate report)
# - Enable export to markdown/pdf/html
