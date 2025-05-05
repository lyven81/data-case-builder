# data_case_builder.py

import streamlit as st

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
        return f"收到的数据集描述：{desc}"

    def define_problem(self, problem, ideas, target):
        self.problem = problem
        self.analysis_ideas = ideas
        self.target_group = target
        return f"问题已定义：{problem}，目标受众为：{target}"

    def business_context(self, goals, stakeholders, unknowns):
        self.business_goals = goals
        self.stakeholders = stakeholders
        self.unknowns = unknowns

    def cleaning_recommendations(self, summary, steps):
        self.cleaning_steps = steps
        return f"数据清洗建议：{steps}"

    def colab_cleaning_code(self):
        code = f"""
# Google Colab Cleaning Template
from google.colab import files
import pandas as pd

uploaded = files.upload()  # 上传 CSV 文件

# 加载数据
raw_df = pd.read_csv('dataset.csv')

# 清洗步骤（根据推荐进行修改）
{self.cleaning_steps}

# 导出清洗后的数据
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
    st.write("为数据分析项目构建完整的案例研究报告")

    agent = DataCaseBuilderAgent()

    st.header("Step 0: 数据集描述")
    dataset_desc = st.text_area("请描述数据集内容和字段：")
    if dataset_desc:
        st.success(agent.describe_dataset(dataset_desc))

    st.header("Step 1: 问题定义")
    problem = st.text_input("请简要描述业务问题或分析目标：")
    ideas = st.text_area("基于数据集，你推荐进行哪三项分析？每项用换行分隔：").splitlines()
    target = st.text_input("谁最关心这些发现？（目标受众）：")
    if problem and ideas and target:
        st.success(agent.define_problem(problem, ideas, target))

    st.subheader("详细业务背景")
    goals = st.text_area("1. 公司希望达成的业务目标：")
    stakeholders = st.text_area("2. 谁是关键利益相关者？他们的需求是什么？")
    unknowns = st.text_area("3. 有哪些关键未知？")
    if goals and stakeholders and unknowns:
        agent.business_context(goals, stakeholders, unknowns)
        st.info("业务背景信息已记录。")

    st.header("Step 2: 数据准备")
    summary = st.text_area("请用要点总结问题、目标、数据思路：")
    cleaning_steps = st.text_area("推荐的清洗步骤（转换格式、处理缺失值等）：")
    if cleaning_steps:
        st.code(agent.cleaning_recommendations(summary, cleaning_steps))

    if st.button("生成 Colab 清洗代码"):
        st.code(agent.colab_cleaning_code())

    st.header("Step 3: 分析建议")
    analysis_plan = st.text_area("请提出你准备进行的分析、使用的图表类型及目的：")
    if analysis_plan:
        st.success(agent.generate_analysis_summary(analysis_plan))

    st.header("Step 4: 总结洞察 & 案例准备")
    insights = st.text_area("请总结分析中的关键洞察，聚焦业务价值：")
    overview = st.text_area("请撰写案例概述（背景 + 目的）：")
    findings = st.text_area("总结关键发现：")
    if insights and overview and findings:
        agent.summarize_insights(insights, overview, findings)
        st.info("洞察和案例概述已保存。")

    st.header("Step 5: 案例标题建议")
    tone = st.selectbox("你希望标题呈现什么风格？", ["专业正式", "吸引注意", "带一点幽默"])
    titles = st.text_area("请提供三个相关标题建议，每个换行：").splitlines()
    if tone and titles:
        agent.suggest_case_titles(tone, titles)
        st.write("🎯 建议标题：")
        for t in titles:
            st.markdown(f"- {t}")

    st.header("Step 6: 最终汇总")
    if st.button("导出草稿报告"):
        st.subheader("📄 报告草稿预览")
        st.markdown(f"**概述：** {agent.case_overview}")
        st.markdown(f"**分析目标：** {agent.problem}")
        st.markdown(f"**建议分析：** {'; '.join(agent.analysis_ideas)}")
        st.markdown(f"**关键洞察：** {agent.insight_summary}")
        st.markdown(f"**结论与发现：** {agent.key_findings}")
        st.markdown(f"**推荐标题：** {', '.join(agent.case_study_title)}")

if __name__ == "__main__":
    main()
