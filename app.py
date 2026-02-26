import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Abhishek Jha | Analytics Portfolio",
    page_icon="📊",
    layout="wide"
)

# 2. Custom CSS for Styling
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* Customizing the project cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stButton) {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        transition: transform 0.2s ease-in-out;
    }
    
    /* Hover effect for cards */
    div[data-testid="stVerticalBlock"] > div:has(div.stButton):hover {
        transform: translateY(-5px);
        border: 1px solid #4A90E2;
    }

    /* Professional Font Styling */
    h1, h2, h3 {
        color: #1E3A8A;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100) # Placeholder for your photo
    st.title("Abhishek Jha")
    st.markdown("🚀 **Data Analyst | Experimentation | Forecasting**")
    
    st.divider()
    
    st.markdown("### Connect")
    st.markdown("[🔗 GitHub Profile](https://github.com/Abhishek-Jha-UW)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/)")
    
    st.divider()
    st.info("Analytics apps built with Python, Scikit-Learn, and Streamlit.")

# 4. Main Header
st.title("📊 Analytics Portfolio")
st.markdown("#### *Turning complex data into interactive decision tools.*")
st.write("") # Spacer

# 5. Project Card Component with Tech Tags
def project_card(title, description, tags, link):
    with st.container(border=True):
        st.subheader(title)
        st.write(description)
        # Tech Tags
        tag_html = "".join([f'<span style="background-color:#E0F2FE; color:#0369A1; padding:2px 8px; border-radius:10px; font-size:12px; margin-right:5px;">{t}</span>' for t in tags])
        st.markdown(tag_html, unsafe_allow_html=True)
        st.write("") # Spacer
        st.link_button("View Live App", link, use_container_width=True)

# ---------------------------------------------------------
# Sections
# ---------------------------------------------------------

# Section: Strategic Impact
st.header("📈 Forecasting & Pricing")
c1, c2 = st.columns(2)
with c1:
    project_card("Timeseries Forecasting", "Predictive modeling to project future business metrics.", ["Python", "Prophet", "Stats"], "https://abhishek-jha-uw-forecasting-app-bu6esr3b9qxhwgkeu6rer7.streamlit.app/")
with c2:
    project_card("Dynamic Pricing Simulator", "Price elasticity modeling to optimize revenue.", ["Economics", "Simulations"], "https://dynamic-pricing-elasticity-simulator-m9pycn5tudxyqrevs3spwl.streamlit.app/")

st.header("🧪 Experimentation & Growth")
c3, c4 = st.columns(2)
with c3:
    project_card("A/B Testing Tool", "Hypothesis testing and power analysis framework.", ["Statistics", "A/B Testing"], "https://a-b-testing-experimentation-lqmnpr27pbueqetibd5xdjk.streamlit.app/")
with c4:
    project_card("Customer Churn System", "Early warning indicators for high-risk accounts.", ["ML", "Churn Analysis"], "https://customer-health-churn-early-warning-system-bvwjzcmbxnmvxgrudsv.streamlit.app/")

st.header("🛠️ Data Quality & IQ")
c5, c6 = st.columns(2)
with c5:
    project_card("GuardianSQL", "Automated monitoring for data health and pipelines.", ["SQL", "Data Quality"], "https://guardiansql-xuah5wqluljyfhb5fe9olu.streamlit.app/")
with c6:
    project_card("Recommendation Engine", "Collaborative filtering for personalized discovery.", ["RecSys", "Scikit-Learn"], "https://recommendation-system-user-based-collaborative-filtering-lmux9.streamlit.app/")

# Footer
st.divider()
st.center = st.markdown("<p style='text-align: center; color: grey;'>© 2026 Abhishek Jha | Built for Business Intelligence</p>", unsafe_allow_html=True)
