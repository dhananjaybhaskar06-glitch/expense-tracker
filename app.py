import streamlit as st

# -----------------------------
# 🎨 PAGE CONFIG (MUST BE FIRST)
# -----------------------------
st.set_page_config(page_title="Expense Tracker", layout="wide")

# -----------------------------
# 🎨 CUSTOM UI
# -----------------------------
st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# IMPORTS
# -----------------------------
from src.auth import login
from src.db import create_tables
from src.pages import dashboard, add_expense, budget

# -----------------------------
# DATABASE INIT
# -----------------------------
create_tables()

# -----------------------------
# 🔐 LOGIN SYSTEM
# -----------------------------
if not login():
    st.stop()

# -----------------------------
# 📌 SIDEBAR NAVIGATION (FIXED KEY)
# -----------------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Add Expense", "Budget"],
    key="main_navigation"   # ✅ FIXED ERROR HERE
)

# -----------------------------
# 📄 PAGE ROUTING
# -----------------------------
if page == "Dashboard":
    dashboard.show()

elif page == "Add Expense":
    add_expense.show()

elif page == "Budget":
    budget.show()