import streamlit as st
from src.db import conn

def show():
    st.title("💰 Budget Planner")

    # ✅ create cursor
    cursor = conn.cursor()

    budget = st.number_input("Set Monthly Budget", min_value=0.0)

    if st.button("Save Budget"):
        cursor.execute("INSERT INTO budget (amount) VALUES (?)", (budget,))
        conn.commit()

        st.success("✅ Budget saved!")