# chat_case_builder.py

import streamlit as st
import pandas as pd
import datetime

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
            st.session_state.goal = user_input
            return "Got it. What's the specific business problem you'd like to solve?"
        if "problem" in user_input.lower() or "goal" in user_input.lower():
            st.session_state.problem = user_input
            return "Thanks. Would you like help cleaning the dataset next?"
        if "clean" in user_input.lower():
            st.session_state.cleaning = "Remove nulls, convert dates, drop duplicates."
            return "Noted. I recommend: Remove nulls, convert date columns, drop duplicates. Shall I continue with insights?"
        if "insight" in user_input.lower() or "summary" in user_input.lower():
            st.session_state.insights = "Top products drive most revenue. Loyalty users churn less. Seasonal spike in Q4."
            return "Summary noted: Top products drive most revenue. Loyalty users churn less. Seasonal spike in Q4. Would you like me to draft your case study now?"
        if user_input.lower() in ["yes", "okay", "go ahead"] and st.session_state.dataset is not None:
            return "Let me inspect the dataset. What kind of patterns or business goals are you exploring?"
        return "Tell me more about your objective or what you'd like to discover in the data."

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
