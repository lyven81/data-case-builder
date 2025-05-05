
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

    def suggest_problems(self):
        return [
            "Identify top-performing product categories",
            "Detect customer churn risk",
            "Forecast future sales",
            "Compare sales by region",
            "Find customer lifetime value drivers"
        ]

    def suggest_analysis_types(self):
        return [
            "Sales trend over time",
            "Segmentation by customer type",
            "Correlation analysis",
            "Product ranking by revenue",
            "Retention rate visualization"
        ]

    def suggest_target_audience(self):
        return [
            "Marketing Team",
            "Sales Manager",
            "Executive Leadership",
            "Product Development",
            "Customer Success"
        ]

    def suggest_cleaning_steps(self):
        return [
            "Drop rows with missing values",
            "Convert date columns to datetime format",
            "Remove duplicates",
            "Standardize column names",
            "Filter outliers"
        ]

    def suggest_analysis_plan(self):
        return [
            "Use line charts to observe sales trends",
            "Apply bar charts for product comparison",
            "Use scatter plots for correlation insights",
            "Create pie charts for segment distribution",
            "Use boxplots for outlier detection"
        ]

    def suggest_insight_summaries(self):
        return [
            "Revenue is driven by a few top-selling products",
            "Customer retention correlates with loyalty program participation",
            "Sales peak around promotional campaigns",
            "Region X consistently underperforms compared to others",
            "High product return rate impacts profitability"
        ]

    def suggest_case_overviews(self):
        return [
            "This case study explores product performance across categories to identify revenue opportunities.",
            "We analyze sales trends and customer segments to guide strategic decisions.",
            "The goal is to uncover drivers of retention and customer value.",
            "We examine regional patterns and campaign effectiveness to guide marketing."
        ]

    def suggest_key_findings(self):
        return [
            "Top 3 products contribute 65% of sales",
            "Churn risk is highest among low-frequency buyers",
            "Retention is stronger in loyalty program members",
            "Sales increased by 40% during campaign periods",
            "Customer satisfaction scores drop after shipping delays"
        ]

    def suggest_case_titles(self):
        return [
            "Uncovering Revenue Drivers",
            "Predicting Churn Before It Happens",
            "The Power of Loyalty",
            "Campaigns That Convert",
            "Why Customers Leave"
        ]

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

    def suggest_case_titles_final(self, tone, titles):
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
    problem = st.selectbox("Select a business problem or goal:", agent.suggest_problems())
    ideas = st.multiselect("Select up to 3 types of analysis to recommend:", agent.suggest_analysis_types(), max_selections=3)
    target = st.selectbox("Select the target audience for these insights:", agent.suggest_target_audience())
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
    summary = st.selectbox("Summarize the problem, goals, and data approach:", agent.suggest_case_overviews())
    cleaning_steps = st.multiselect("Select data cleaning steps:", agent.suggest_cleaning_steps(), max_selections=3)
    if cleaning_steps:
        st.code(agent.cleaning_recommendations(summary, '; '.join(cleaning_steps)))

    if st.button("Generate Colab Cleaning Code"):
        st.code(agent.colab_cleaning_code())

    st.header("Step 3: Analysis Suggestions")
    analysis_plan = st.selectbox("Select an analysis plan:", agent.suggest_analysis_plan())
    if analysis_plan:
        st.success(agent.generate_analysis_summary(analysis_plan))

    st.header("Step 4: Summarize Insights & Draft Report")
    insights = st.selectbox("Select a key insight:", agent.suggest_insight_summaries())
    overview = st.selectbox("Select a case overview:", agent.suggest_case_overviews())
    findings = st.selectbox("Select key findings:", agent.suggest_key_findings())
    if insights and overview and findings:
        agent.summarize_insights(insights, overview, findings)
        st.info("Insights and case overview saved.")

    st.header("Step 5: Recommend Titles")
    tone = st.selectbox("What tone should the titles have?", ["Professional", "Attention-Grabbing", "Light and Playful"])
    titles = st.multiselect("Select up to 3 case study titles:", agent.suggest_case_titles(), max_selections=3)
    if tone and titles:
        agent.suggest_case_titles_final(tone, titles)
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
