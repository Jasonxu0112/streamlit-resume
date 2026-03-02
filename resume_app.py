import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="Xueyuan Xu | Resume", page_icon="✦", layout="wide")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #0f0f0f;
    color: #e8e0d5;
}
h1, h2, h3 { font-family: 'DM Serif Display', serif; }

.hero {
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: 16px;
    padding: 3rem 2.5rem;
    margin-bottom: 2rem;
    border: 1px solid #ffffff15;
}
.hero h1 { font-size: 3.2rem; margin: 0; color: #f0e6d3; }
.hero p  { font-size: 1.1rem; color: #a0b4c8; margin-top: 0.5rem; }

.tag {
    display: inline-block;
    background: #0f3460;
    color: #a0c4ff;
    border-radius: 20px;
    padding: 4px 14px;
    font-size: 0.8rem;
    margin: 3px;
}
.section-card {
    background: #161616;
    border: 1px solid #ffffff12;
    border-radius: 12px;
    padding: 1.5rem;
    margin-bottom: 1rem;
}
.metric-box {
    background: linear-gradient(135deg, #1a1a2e, #0f3460);
    border-radius: 10px;
    padding: 1rem;
    text-align: center;
    border: 1px solid #ffffff15;
}
.metric-box .num { font-size: 2rem; font-family: 'DM Serif Display', serif; color: #a0c4ff; }
.metric-box .lbl { font-size: 0.75rem; color: #708090; text-transform: uppercase; letter-spacing: 1px; }
</style>
""", unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <h1>Xueyuan Xu</h1>
  <p>MBA Candidate · Rotman School of Management, University of Toronto</p>
  <p>📧 xueyuan.xu@rotman.utoronto.ca &nbsp;|&nbsp; 🏙️ Toronto, ON</p>
</div>
""", unsafe_allow_html=True)

# ── Sidebar widgets ───────────────────────────────────────────────────────────
st.sidebar.title("⚙️ Customize View")

section = st.sidebar.selectbox(
    "📂 Jump to Section",
    ["Overview", "Experience", "Education", "Skills", "Projects"]
)

show_chart_type = st.sidebar.radio(
    "📊 Skills Chart Style",
    ["Bar Chart", "Radar Chart"]
)

experience_filter = st.sidebar.multiselect(
    "🏢 Filter Experience by Industry",
    ["Finance", "Technology", "Consulting", "Research"],
    default=["Finance", "Technology", "Consulting", "Research"]
)

show_education = st.sidebar.checkbox("🎓 Show Education Details", value=True)
show_projects  = st.sidebar.checkbox("🚀 Show Projects", value=True)

# ── Quick metrics ─────────────────────────────────────────────────────────────
st.markdown("### ✦ At a Glance")
c1, c2, c3, c4 = st.columns(4)
for col, num, lbl in zip(
    [c1, c2, c3, c4],
    ["5+", "3", "2", "10+"],
    ["Years Experience", "Industries", "Degrees", "Projects"]
):
    col.markdown(f"""
    <div class="metric-box">
      <div class="num">{num}</div>
      <div class="lbl">{lbl}</div>
    </div>""", unsafe_allow_html=True)

st.markdown("---")

# ── Experience ────────────────────────────────────────────────────────────────
if section in ["Overview", "Experience"]:
    st.markdown("### 💼 Work Experience")

    experiences = [
        {
            "role": "Financial Analyst",
            "company": "ABC Capital",
            "period": "2021 – 2023",
            "industry": "Finance",
            "desc": "Built DCF and LBO models; supported $200M+ deal pipeline.",
            "tags": ["Excel", "Valuation", "M&A"]
        },
        {
            "role": "Product Manager Intern",
            "company": "TechCo",
            "period": "2020 – 2021",
            "industry": "Technology",
            "desc": "Led agile sprints; increased feature delivery speed by 30%.",
            "tags": ["Agile", "Roadmapping", "SQL"]
        },
        {
            "role": "Strategy Consultant",
            "company": "Consulting Group",
            "period": "2019 – 2020",
            "industry": "Consulting",
            "desc": "Delivered market-entry strategy for 3 Fortune 500 clients.",
            "tags": ["Strategy", "PowerPoint", "Market Research"]
        },
        {
            "role": "Research Assistant",
            "company": "University Lab",
            "period": "2018 – 2019",
            "industry": "Research",
            "desc": "Published 2 papers on NLP and sentiment analysis.",
            "tags": ["Python", "NLP", "Research"]
        },
    ]

    for exp in experiences:
        if exp["industry"] in experience_filter:
            tags_html = "".join(f'<span class="tag">{t}</span>' for t in exp["tags"])
            st.markdown(f"""
            <div class="section-card">
              <strong style="font-size:1.05rem">{exp['role']}</strong>
              &nbsp;·&nbsp; <span style="color:#a0b4c8">{exp['company']}</span>
              &nbsp;·&nbsp; <span style="color:#606878;font-size:0.85rem">{exp['period']}</span>
              <br/><span style="color:#708090;font-size:0.85rem">{exp['industry']}</span>
              <p style="margin:0.5rem 0 0.3rem">{exp['desc']}</p>
              {tags_html}
            </div>""", unsafe_allow_html=True)

# ── Education ─────────────────────────────────────────────────────────────────
if show_education and section in ["Overview", "Education"]:
    st.markdown("### 🎓 Education")
    edu_data = [
        {"Degree": "MBA", "Institution": "University of Toronto (Rotman)", "Year": "2024–2026", "GPA": "3.9"},
        {"Degree": "B.Sc. Computer Science", "Institution": "Peking University", "Year": "2015–2019", "GPA": "3.8"},
    ]
    st.dataframe(pd.DataFrame(edu_data), use_container_width=True, hide_index=True)

# ── Skills ────────────────────────────────────────────────────────────────────
if section in ["Overview", "Skills"]:
    st.markdown("### 🛠️ Skills Proficiency")

    skills = {
        "Python":          90,
        "Financial Modeling": 88,
        "SQL":             80,
        "Machine Learning":75,
        "PowerPoint":      85,
        "Product Strategy":78,
    }

    if show_chart_type == "Bar Chart":
        df_skills = pd.DataFrame({"Skill": list(skills.keys()), "Proficiency": list(skills.values())})
        fig = px.bar(
            df_skills, x="Proficiency", y="Skill", orientation="h",
            color="Proficiency", color_continuous_scale="Blues",
            range_x=[0, 100]
        )
        fig.update_layout(
            paper_bgcolor="#0f0f0f", plot_bgcolor="#161616",
            font_color="#e8e0d5", coloraxis_showscale=False,
            margin=dict(l=10, r=10, t=10, b=10)
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        categories = list(skills.keys())
        values     = list(skills.values())
        fig = go.Figure(go.Scatterpolar(
            r=values + [values[0]],
            theta=categories + [categories[0]],
            fill="toself",
            line_color="#4a9eff",
            fillcolor="rgba(74,158,255,0.2)"
        ))
        fig.update_layout(
            polar=dict(
                bgcolor="#161616",
                radialaxis=dict(visible=True, range=[0,100], color="#708090"),
                angularaxis=dict(color="#a0b4c8")
            ),
            paper_bgcolor="#0f0f0f", font_color="#e8e0d5",
            margin=dict(l=40, r=40, t=40, b=40)
        )
        st.plotly_chart(fig, use_container_width=True)

# ── Projects ──────────────────────────────────────────────────────────────────
if show_projects and section in ["Overview", "Projects"]:
    st.markdown("### 🚀 Selected Projects")
    projects = [
        ("LLM Sentiment Analyzer", "Built a fine-tuned BERT model for financial news sentiment classification.", ["Python", "HuggingFace", "NLP"]),
        ("Portfolio Optimizer",    "Developed mean-variance optimization tool with live market data.",          ["Python", "Finance", "Plotly"]),
        ("Streamlit Resume App",   "This interactive resume — built for Rotman MBA Lab 1.",                    ["Streamlit", "Plotly", "Python"]),
    ]
    for title, desc, tags in projects:
        tags_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
        st.markdown(f"""
        <div class="section-card">
          <strong style="font-size:1.05rem">{title}</strong>
          <p style="margin:0.4rem 0 0.3rem;color:#a0b4c8">{desc}</p>
          {tags_html}
        </div>""", unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("<p style='text-align:center;color:#404040;font-size:0.8rem'>Built with Streamlit · Xueyuan Xu · 2026</p>", unsafe_allow_html=True)
