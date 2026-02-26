import streamlit as st

# -------------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="Abhishek Jha | Analytics Portfolio",
    layout="wide"
)

# -------------------------------------------------------
# GLOBAL STYLING — Clean Enterprise Aesthetic
# -------------------------------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="st-"] {
    font-family: 'Inter', sans-serif;
}

/* Background */
.stApp {
    background-color: #ffffff;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #f7f8fa;
    border-right: 1px solid #e6e8eb;
    padding-top: 20px;
}

/* Main Headline */
h1 {
    font-size: 40px !important;
    font-weight: 700 !important;
    color: #111827;
    margin-bottom: 10px;
}

h2 {
    font-size: 22px !important;
    font-weight: 600 !important;
    margin-top: 50px !important;
    margin-bottom: 15px !important;
    color: #111827;
}

/* Section Label */
.section-label {
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    color: #6b7280;
    text-transform: uppercase;
    margin-top: 40px;
    margin-bottom: 5px;
}

/* Card Styling */
.project-card {
    border: 1px solid #e5e7eb;
    padding: 24px;
    border-radius: 8px;
    background-color: #ffffff;
    transition: border 0.2s ease;
    margin-bottom: 18px;
}

.project-card:hover {
    border: 1px solid #111827;
}

/* Title */
.project-title {
    font-size: 18px;
    font-weight: 600;
    color: #111827;
    margin-bottom: 6px;
}

/* Impact Line */
.project-impact {
    font-size: 14px;
    font-weight: 600;
    color: #2563eb;
    margin-bottom: 10px;
}

/* Description */
.project-desc {
    font-size: 14px;
    color: #4b5563;
    margin-bottom: 12px;
}

/* Tags */
.tag {
    display: inline-block;
    font-size: 11px;
    font-weight: 600;
    padding: 4px 8px;
    border-radius: 5px;
    background-color: #f3f4f6;
    color: #374151;
    border: 1px solid #e5e7eb;
    margin-right: 6px;
    margin-bottom: 6px;
}

/* Buttons */
div.stLinkButton > a {
    background-color: #111827 !important;
    color: #ffffff !important;
    border-radius: 6px !important;
    font-weight: 600 !important;
    padding: 0.5rem 1rem !important;
    border: none !important;
}

div.stLinkButton > a:hover {
    background-color: #374151 !important;
}

footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR
# -------------------------------------------------------
with st.sidebar:
    st.markdown("## Abhishek Jha")
    st.markdown("**MSBA | Data & Decision Science**")
    st.caption("Seattle, Washington")

    st.divider()

    st.markdown("### Core Focus")
    st.markdown("""
    • Forecasting & Revenue Modeling  
    • Experimentation & Causal Inference  
    • Pricing & Optimization  
    • Machine Learning Systems  
    • Data Quality & Governance  
    """)

    st.divider()

    st.markdown("[GitHub](https://github.com/Abhishek-Jha-UW)")
    st.markdown("[LinkedIn](https://www.linkedin.com/)")

# -------------------------------------------------------
# HEADER
# -------------------------------------------------------
st.title("Analytics Decision Systems")
st.markdown(
    "A portfolio of production-style analytics applications designed to support forecasting, growth experimentation, pricing strategy, and data governance."
)

# -------------------------------------------------------
# CARD COMPONENT
# -------------------------------------------------------
def render_card(title, impact, desc, tags, link):
    tag_html = "".join([f"<span class='tag'>{t}</span>" for t in tags])

    st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{title}</div>
            <div class="project-impact">{impact}</div>
            <div class="project-desc">{desc}</div>
            {tag_html}
        </div>
    """, unsafe_allow_html=True)

    st.link_button("View Application", link, use_container_width=True)

# -------------------------------------------------------
# CONTENT
# -------------------------------------------------------

# Revenue & Forecasting
st.markdown("<div class='section-label'>Revenue & Prediction</div>", unsafe_allow_html=True)
st.header("Forecasting & Pricing Systems")

c1, c2 = st.columns(2)

with c1:
    render_card(
        "Revenue Forecasting Engine",
        "Improved forecast accuracy by +12% vs baseline moving average model",
        "Time series forecasting framework using Prophet and SARIMAX to project revenue and demand trends.",
        ["Python", "Prophet", "Time Series", "Forecasting"],
        "https://abhishek-jha-uw-forecasting-app-bu6esr3b9qxhwgkeu6rer7.streamlit.app/"
    )

with c2:
    render_card(
        "Dynamic Pricing Simulator",
        "Simulated elasticity scenarios to optimize revenue under demand constraints",
        "Elasticity-driven pricing engine enabling scenario-based revenue optimization.",
        ["Economics", "Optimization", "Simulation"],
        "https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/"
    )

# Growth & Experimentation
st.markdown("<div class='section-label'>Growth & Retention</div>", unsafe_allow_html=True)
st.header("Experimentation & ML Systems")

c3, c4 = st.columns(2)

with c3:
    render_card(
        "A/B Testing Platform",
        "Automated statistical testing with power analysis and lift diagnostics",
        "End-to-end experimentation framework supporting hypothesis testing and decision confidence evaluation.",
        ["Statistics", "A/B Testing", "Causal Inference"],
        "https://a-b-testing-experimentation-lqmnpr27pbuqetibd5xdjk.streamlit.app/"
    )

with c4:
    render_card(
        "Churn Early Warning System",
        "ML classification identifying high-risk customer segments",
        "Supervised learning pipeline detecting churn risk using behavioral and transactional features.",
        ["Scikit-Learn", "XGBoost", "Classification"],
        "https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/"
    )

# Systems & Intelligence
st.markdown("<div class='section-label'>Data Systems & Intelligence</div>", unsafe_allow_html=True)
st.header("Governance & Recommendation Systems")

c5, c6 = st.columns(2)

with c5:
    render_card(
        "GuardianSQL",
        "Automated anomaly detection for production SQL pipelines",
        "Data quality monitoring framework ensuring integrity, validation, and pipeline health.",
        ["SQL", "Data Quality", "Monitoring"],
        "https://guardiansql-xuah5wqluljyfhb5fe9olu.streamlit.app/"
    )

with c6:
    render_card(
        "Recommendation Engine",
        "Personalized ranking using collaborative filtering",
        "User-based collaborative filtering system for personalized product discovery.",
        ["Recommender Systems", "Machine Learning"],
        "https://recommendation-system-user-based-collaborative-filtering-lmux9.streamlit.app/"
    )

# -------------------------------------------------------
# FOOTER
# -------------------------------------------------------
st.divider()
st.markdown(
    "<p style='text-align:center; color:#9ca3af; font-size:13px;'>© 2026 Abhishek Jha | Analytics & Decision Science</p>",
    unsafe_allow_html=True
)
