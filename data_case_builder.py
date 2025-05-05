# data_case_builder.py

import streamlit as st
import pandas as pd

class DataCaseBuilderAgent:
    def __init__(self):
        self.dataset_description = ""
        self.problem = ""
        self.analysis_ideas = []
        self.target_group = ""
        self.business_goals = ""
        self.stakeholders = ""
        self.unknowns = ""
        self.cleaning_steps = ""
        self.colab_code_cleaning = ""
        self.analysis_summary = ""
        self.insight_summary = ""
        self.case_title_tone = ""
        self.case_study_title = []
        self.case_overview = ""
        self.key_findings = ""

    def describe_dataset(self, desc):
        self.dataset_description = desc
        return f"Dataset description received: {desc}"

    def define_problem(self, problem, ideas, target):
        self.problem = problem
        self.analysis_ideas = ideas
        self.target_group = target
        return f"Problem defined: {problem}, Target audience: {target}"

    def business_context(self, goals, stakeholders, unknowns):
        self.business_goals = goals
        self.stakeholders = stakeholders
        self.unknowns = unknowns

    def cleaning_recommendations(self, summary, steps):
        self.cleaning_steps = steps
        return f"Cleaning steps recommended: {steps}"

    def colab_cleaning_code(self):
        code = f"""
# Google Colab Cleaning Template
from google.colab import files
import pandas as pd

uploaded = files.upload()  # Upload CSV file

# Load data
raw_df = pd.read_csv('dataset.csv')

# Cleaning steps (modify as needed)
{self.cleaning_steps}

# Export cleaned data
raw_df.to_csv('cleaned_dataset.csv', index=False)
files.download('cleaned_dataset.csv')
        """
        self.colab_code_cleaning = code
        return code

    def generate_analysis_summary(self, summary):
        self.analysis_summary = summary
        return summary

    def summarize_insights(self, insights, overview, findings):
        self.insight_summary = insights
        self.case_overview = overview
        self.key_findings = findings

    def suggest_case_titles(self, tone, titles):
        self.case_title_tone = tone
        self.case_study_title = titles

# === Streamlit App ===
def main():
    st.title("📊 Data Case Builder Agent")
    st.write("Build a complete data case study report step-by-step")

    agent = DataCaseBuilderAgent()

    st.header("Step 0: Upload and Describe Dataset")
    uploaded_file = st.file_uploader("Upload a CSV file:", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.session_state['dataset_df'] = df
        st.success("✅ Dataset uploaded successfully! Here's a preview:")
        st.dataframe(df.head())

    dataset_desc = st.text_area("Describe the structure, fields, or potential use of this dataset:")
    if dataset_desc and 'dataset_df' in st.session_state:
        st.success(agent.describe_dataset(dataset_desc))

    st.header("Step 1: Define the Problem")
    problem = st.text_input("Briefly describe the business problem or goal:")
    ideas = st.text_area("What 3 types of analysis would you recommend based on this dataset? (One per line):").splitlines()
    target = st.text_input("Who would benefit most from these insights? (Target audience):")
    if problem and ideas and target:
        st.success(agent.define_problem(problem, ideas, target))

    st.subheader("Business Context")
    goals = st.text_area("1. What are the business goals?")
    stakeholders = st.text_area("2. Who are the key stakeholders and their needs?")
    unknowns = st.text_area("3. What are the major unknowns?")
    if goals and stakeholders and unknowns:
        agent.business_context(goals, stakeholders, unknowns)
        st.info("Business context saved.")

    st.header("Step 2: Data Preparation")
    summary = st.text_area("Summarize the problem, goals, and data approach:")
    cleaning_steps = st.text_area("Recommended data cleaning steps (e.g., format conversion, missing value handling):")
    if cleaning_steps:
        st.code(agent.cleaning_recommendations(summary, cleaning_steps))

    if st.button("Generate Colab Cleaning Code"):
        st.code(agent.colab_cleaning_code())

    st.header("Step 3: Analysis Suggestions")
    analysis_plan = st.text_area("Describe the planned analysis, types of charts, and purpose:")
    if analysis_plan:
        st.success(agent.generate_analysis_summary(analysis_plan))

    st.header("Step 4: Summarize Insights & Draft Report")
    insights = st.text_area("Summarize key insights focusing on business value:")
    overview = st.text_area("Write a brief case overview (background + purpose):")
    findings = st.text_area("Summarize key findings:")
    if insights and overview and findings:
        agent.summarize_insights(insights, overview, findings)
        st.info("Insights and case overview saved.")

    st.header("Step 5: Recommend Titles")
    tone = st.selectbox("What tone should the titles have?", ["Professional", "Attention-Grabbing", "Light and Playful"])
    titles = st.text_area("Suggest three case study titles (one per line):").splitlines()
    if tone and titles:
        agent.suggest_case_titles(tone, titles)
        st.write("🎯 Suggested Titles:")
        for t in titles:
            st.markdown(f"- {t}")

    st.header("Step 6: Final Report Preview")
    if st.button("Export Draft Report"):
        st.subheader("📄 Report Draft")
        st.markdown(f"**Overview:** {agent.case_overview}")
        st.markdown(f"**Business Problem:** {agent.problem}")
        st.markdown(f"**Recommended Analyses:** {'; '.join(agent.analysis_ideas)}")
        st.markdown(f"**Key Insights:** {agent.insight_summary}")
        st.markdown(f"**Conclusions & Findings:** {agent.key_findings}")
        st.markdown(f"**Suggested Titles:** {', '.join(agent.case_study_title)}")

if __name__ == "__main__":
    main()
