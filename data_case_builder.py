# chat_case_builder.py

import streamlit as st
import pandas as pd
import datetime
import openai
import os

st.set_page_config(page_title="Conversational Case Builder", layout="wide")

# Secure API Key loading
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

if 'messages' not in st.session_state:
    st.session_state.messages = []
    st.session_state.dataset = None
    st.session_state.goal = ""
    st.session_state.problem = ""
    st.session_state.cleaning = ""
    st.session_state.insights = ""

# LLM-backed reply
class ConversationalCaseAgent:
    def reply(self, user_input):
        chat_history = st.session_state.messages[-6:]  # use last few messages as context
        history_messages = [
            {"role": msg["role"], "content": msg["content"]} for msg in chat_history
        ]
        prompt = {
            "role": "user",
            "content": f"Dataset columns: {st.session_state.dataset.columns.tolist() if st.session_state.dataset is not None else 'none'}\nQuestion: {user_input}"
        }
        history_messages.append(prompt)
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history_messages,
                temperature=0.7
            )
            reply_text = response.choices[0].message.content.strip()
        except Exception as e:
            reply_text = f"⚠️ LLM Error: {str(e)}"
        return reply_text

    def generate_case_report(self):
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"""
## Title: Insights that Drive Growth
**Subtitle:** A data-driven exploration to support business decisions

### Overview
{st.session_state.goal}

### Key Questions & Findings
- **What problem are we solving?**
  {st.session_state.problem}

- **How was the data prepared?**
  {st.session_state.cleaning}

- **What insights did we discover?**
  {st.session_state.insights}

### Conclusion
This case study highlights key drivers and patterns from the dataset, aligned with the business objective defined above.

### Recommendations
#### High-Risk But Valuable – Retain
Explore engagement strategies for loyal but at-risk customers.

#### High-Risk and Lower Strategic Value – Reassess Fit
Segment and evaluate re-engagement campaigns.

#### Low-Risk and High Value – Strengthen Loyalty
Increase touchpoints and personalized offers to reward this group.

*Report generated on {today}.*
"""

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

# Report Output
if st.button("📄 Generate Full Case Study Report"):
    report = agent.generate_case_report()
    st.subheader("📘 Case Study Report")
    st.markdown(report)
