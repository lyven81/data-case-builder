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

    def suggest_problems(self):
        return [
            "Identify top-performing products",
            "Predict customer churn",
            "Understand sales trends",
            "Evaluate campaign performance",
            "Analyze customer satisfaction"
        ]

    def suggest_analysis_types(self):
        return [
            "Trend analysis",
            "Customer segmentation",
            "Correlation heatmap",
            "Top products by revenue",
            "Churn prediction model"
        ]

    def suggest_target_audience(self):
        return [
            "Marketing team",
            "Sales department",
            "Executive team",
            "Customer support",
            "Product development"
        ]

    def suggest_cleaning_steps(self):
        return [
            "Drop null values",
            "Convert date strings to datetime",
            "Remove duplicate records",
            "Normalize column headers",
            "Filter outliers in numeric columns"
        ]

    def suggest_case_overviews(self):
        return [
            "This case explores how product performance varies by category.",
            "We examine churn risk factors in customer segments.",
            "The dataset reveals how marketing campaigns influenced sales.",
            "This analysis uncovers retention patterns across product lines."
        ]

    def suggest_analysis_plan(self):
        return [
            "Use line charts for trends, bar plots for category comparison, and heatmaps for correlation.",
            "Combine clustering with revenue metrics to segment customers.",
            "Visualize customer demographics vs. churn with scatter plots and box plots."
        ]

    def suggest_insight_summaries(self):
        return [
            "Sales are seasonal, peaking in Q4.",
            "Repeat customers spend 30% more on average.",
            "Product X underperforms despite high traffic.",
            "Churn is highest among first-time buyers."
        ]

    def suggest_key_findings(self):
        return [
            "Top 10% of customers generate 50% of revenue.",
            "Regions A and B show above-average returns.",
            "Marketing boosts sales temporarily but not retention.",
            "Customer lifetime value is strongly tied to loyalty points."
        ]

    def suggest_case_titles(self):
        return [
            "The Hidden Value of Loyalty",
            "Uncovering Sales Patterns",
            "Winning Back Lost Customers",
            "Revenue Drivers Revealed",
            "Data-Driven Campaign Success"
        ]

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

uploaded = files.upload()
df = pd.read_csv('dataset.csv')

# Apply cleaning steps
{self.cleaning_steps}

df.to_csv('cleaned_dataset.csv', index=False)
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
