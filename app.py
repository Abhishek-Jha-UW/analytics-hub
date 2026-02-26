import streamlit as st

st.set_page_config(page_title="Abhishek Jha – Analytics Portfolio", layout="centered")

st.title("Abhishek Jha – Analytics Portfolio")
st.write(
    "A collection of interactive analytics apps covering experimentation, forecasting, "
    "pricing, data engineering, and KPI dashboards."
)

st.subheader("Interactive Apps")

st.write("**Dynamic Pricing & Elasticity Simulator**")
st.link_button("Open App", "https://dynamic-pricing-simulator.streamlit.app")

st.write("**Forecasting Framework**")
st.link_button("Open App", "https://forecasting-framework.streamlit.app")

st.write("**A/B Testing Experimentation Tool**")
st.link_button("Open App", "https://ab-testing-tool.streamlit.app")

st.write("**Customer Health & Churn Early Warning System**")
st.link_button("Open App", "https://customer-churn-warning.streamlit.app")

st.write("**Competitive Landscape Mapping**")
st.link_button("Open App", "https://competitive-landscape.streamlit.app")

st.write("---")
st.write("GitHub Profile: https://github.com/Abhishek-Jha-UW")
