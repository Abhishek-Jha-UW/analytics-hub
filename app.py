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
    color: #111827
