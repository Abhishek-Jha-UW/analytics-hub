import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Abhishek Jha | Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------------------------------------------------------
# Sidebar
# ---------------------------------------------------------
with st.sidebar:
    st.title("Abhishek Jha")
    st.markdown("**Data Analyst | Experimentation | Forecasting | Pricing**")

    st.markdown(
        """
        [GitHub Profile](https://github.com/Abhishek-Jha-UW)  
        [LinkedIn](https://www.linkedin.com/)  
        """
    )

    st.write("---")
    st.caption(
        "This portfolio showcases interactive analytics applications built using "
        "Python, Streamlit, and statistical modeling."
    )

# ---------------------------------------------------------
# Main Header
# ---------------------------------------------------------
st.title("Analytics Portfolio")
st.markdown(
    """
    A curated collection of interactive analytics applications demonstrating capabilities in  
    **forecasting, experimentation, pricing, customer intelligence, data quality, and recommendation systems.**
    """
)
st.write("---")

# ---------------------------------------------------------
# Reusable Project Card Component
# ---------------------------------------------------------
def project_card(title, description, link):
    with st.container(border=True):
        st.subheader(title)
        st.write(description)
        st.link_button("Open App", link, use_container_width=True)

# ---------------------------------------------------------
# Section: Forecasting & Pricing
# ---------------------------------------------------------
st.header("Forecasting & Pricing")

col1, col2 = st.columns(2)

with col1:
    project_card(
        "Timeseries Forecasting",
        "Forecasting framework using statistical and time-series models to project future trends.",
        "https://abhishek-jha-uw-forecasting-app-bu6esr3b9qxhwgkeu6rer7.streamlit.app/"
    )

with col2:
    project_card(
        "Dynamic Pricing & Elasticity Simulator",
        "Interactive simulator to analyze price elasticity and optimize revenue strategies.",
        "https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/"
    )

# ---------------------------------------------------------
# Section: Experimentation & Growth
# ---------------------------------------------------------
st.header("Experimentation & Growth")

col3, col4 = st.columns(2)

with col3:
    project_card(
        "A/B Testing Experimentation Tool",
        "Statistical experimentation framework for hypothesis testing, power analysis, and lift estimation.",
        "https://a-b-testing-experimentation-lqmnpr27pbueqetibd5xdjk.streamlit.app/"
    )

with col4:
    project_card(
        "Customer Health & Churn Early Warning System",
        "Predictive system identifying at-risk customers using behavioral and health-score indicators.",
        "https://customer-health-churn-early-warning-system-bvwjzcmbxnmvxgrudsv.streamlit.app/"
    )

# ---------------------------------------------------------
# Section: Data Quality & Intelligence
# ---------------------------------------------------------
st.header("Data Quality & Intelligence")

col5, col6 = st.columns(2)

with col5:
    project_card(
        "GuardianSQL – Data Health & Quality",
        "Automated data quality monitoring to ensure reliable pipelines and accurate reporting.",
        "https://guardiansql-xuah5wqluljyfhb5fe9olu.streamlit.app/"
    )

with col6:
    project_card(
        "Recommendation System – Collaborative Filtering",
        "User-based recommendation engine for personalized ranking and content discovery.",
        "https://recommendation-system-user-based-collaborative-filtering-lmux9.streamlit.app/"
    )

# ---------------------------------------------------------
# Section: Market Intelligence
# ---------------------------------------------------------
st.header("Market Intelligence")

project_card(
    "Competitive Landscape Mapping",
    "Visualization tool for analyzing competitor positioning and market structure.",
    "https://competitive-landscape-mapping-f66enxmzggca3juvhzozae.streamlit.app/"
)

# ---------------------------------------------------------
# Footer
# ---------------------------------------------------------
st.write("---")
st.caption("© 2026 Abhishek Jha | Built with Streamlit")
