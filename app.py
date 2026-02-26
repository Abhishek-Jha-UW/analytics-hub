import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Abhishek Jha | Analytics Portfolio",
    layout="wide"
)

# -------------------------------------------------------
# GLOBAL STYLING (Clean / Executive Look)
# -------------------------------------------------------
st.markdown("""
<style>

/* App background */
.stApp {
    background-color: #ffffff;
}

/* Typography */
h1 {
    font-size: 42px !important;
    font-weight: 600 !important;
    color: #111111;
}

h2 {
    font-size: 24px !important;
    font-weight: 600 !important;
    margin-top: 40px !important;
    color: #222222;
}

h3 {
    font-size: 18px !important;
    font-weight: 600 !important;
    color: #111111;
}

/* Card styling */
.portfolio-card {
    border: 1px solid #e6e6e6;
    padding: 28px;
    border-radius: 6px;
    background-color: #ffffff;
    transition: all 0.2s ease;
    height: 100%;
}

.portfolio-card:hover {
    border: 1px solid #111111;
}

/* Description text */
.card-desc {
    color: #555555;
    font-size: 14px;
    margin-bottom: 16px;
}

/* Tag styling */
.tag {
    display: inline-block;
    border: 1px solid #d9d9d9;
    padding: 4px 10px;
    font-size: 12px;
    margin-right: 6px;
    margin-bottom: 6px;
    border-radius: 4px;
    color: #444444;
}

/* Button styling */
div.stLinkButton > a {
    background-color: #111111 !important;
    color: white !important;
    border-radius: 4px !important;
    font-size: 14px !important;
}

div.stLinkButton > a:hover {
    background-color: #333333 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #fafafa;
    border-right: 1px solid #eeeeee;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
with st.sidebar:
    st.markdown("## Abhishek Jha")
    st.markdown("**MSBA | Data & Decision Science**")
    st.markdown("Seattle, WA")

    st.divider()

    st.markdown("### Focus Areas")
    st.markdown("""
    • Forecasting  
    • Experimentation  
    • Pricing Strategy  
    • Data Quality Systems  
    """)

    st.divider()

    st.markdown("### Connect")
    st.markdown("[GitHub](https://github.com/Abhishek-Jha-UW)")
    st.markdown("[LinkedIn](https://www.linkedin.com/)")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.title("Analytics Applications")
st.markdown("Building decision systems for forecasting, growth, and data governance.")

# -------------------------------------------------------
# REUSABLE CARD COMPONENT
# -------------------------------------------------------
def project_card(title, description, tags, link):
    tag_html = "".join([f"<span class='tag'>{t}</span>" for t in tags])

    st.markdown(f"""
    <div class="portfolio-card">
        <h3>{title}</h3>
        <p class="card-desc">{description}</p>
        {tag_html}
    </div>
    """, unsafe_allow_html=True)

    st.link_button("View Application", link, use_container_width=True)


# -------------------------------------------------------
# SECTIONS
# -------------------------------------------------------

# Forecasting & Pricing
st.header("Forecasting & Pricing")

col1, col2 = st.columns(2)

with col1:
    project_card(
        "Time Series Forecasting",
        "Business forecasting models using Prophet and statistical methods to project revenue and demand trends.",
        ["Python", "Prophet", "Time Series"],
        "https://abhishek-jha-uw-forecasting-app-bu6esr3b9qxhwgkeu6rer7.streamlit.app/"
    )

with col2:
    project_card(
        "Dynamic Pricing Simulator",
        "Elasticity-based pricing engine to simulate revenue optimization scenarios.",
        ["Economics", "Simulation", "Optimization"],
        "https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/"
    )

# Experimentation
st.header("Experimentation & Growth")

col3, col4 = st.columns(2)

with col3:
    project_card(
        "A/B Testing Platform",
        "Statistical testing framework with power analysis and experiment diagnostics.",
        ["Statistics", "Hypothesis Testing"],
        "https://a-b-testing-experimentation-lqmnpr27pbueqetibd5xdjk.streamlit.app/"
    )

with col4:
    project_card(
        "Customer Churn Prediction",
        "Machine learning system identifying high-risk customers using behavioral signals.",
        ["Machine Learning", "Classification"],
        "https://customer-health-churn-early-warning-system-bvwjzcmbxnmvxgrudsv.streamlit.app/"
    )

# Data Systems
st.header("Data Quality & Systems")

col5, col6 = st.columns(2)

with col5:
    project_card(
        "GuardianSQL",
        "Automated data quality monitoring framework for SQL-based pipelines.",
        ["SQL", "Data Governance"],
        "https://guardiansql-xuah5wqluljyfhb5fe9olu.streamlit.app/"
    )

with col6:
    project_card(
        "Recommendation Engine",
        "Collaborative filtering system for personalized product discovery.",
        ["Recommender Systems", "Scikit-Learn"],
        "https://recommendation-system-user-based-collaborative-filtering-lmux9.streamlit.app/"
    )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.divider()
st.markdown(
    "<p style='text-align:center; color:#888888; font-size:13px;'>© 2026 Abhishek Jha | Analytics & Decision Systems</p>",
    unsafe_allow_html=True
)
