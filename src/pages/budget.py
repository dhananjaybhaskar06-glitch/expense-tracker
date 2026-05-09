import streamlit as st
from src.db import conn, cursor
import pandas as pd

def show():
    st.title("💰 Budget Tracker")

    category = st.text_input("Category")
    amount = st.number_input("Budget Amount", min_value=0.0)

    if st.button("Set Budget"):
        cursor.execute("INSERT INTO budgets VALUES (?, ?)", (category, amount))
        conn.commit()
        st.success("Budget Saved!")

    # Show budgets
    df = pd.read_sql_query("SELECT * FROM budgets", conn)
    st.write(df)