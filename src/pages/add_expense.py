import streamlit as st
from datetime import datetime
from src.db import conn, cursor
from src.utils import auto_category

def show():
    st.title("➕ Add Expense")

    date = st.date_input("Date", datetime.today())
    desc = st.text_input("Description")
    amount = st.number_input("Amount", min_value=0.0)
    payment = st.selectbox("Payment", ["Cash", "UPI", "Card"])

    if st.button("Add Expense"):
        category = auto_category(desc)

        cursor.execute("INSERT INTO expenses VALUES (?, ?, ?, ?, ?)",
                       (str(date), category, amount, payment, desc))
        conn.commit()

        st.success(f"Added under {category}")