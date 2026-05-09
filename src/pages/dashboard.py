import streamlit as st
import plotly.express as px
import pandas as pd
from src.db import conn
from src.analysis import load_data, category_summary, monthly_summary, payment_summary
from src.report import generate_pdf


def show():
    st.title("📊 Expense Dashboard Pro")

    df = load_data(conn)

    if df.empty:
        st.warning("No data available")
        return

    # -----------------------------
    # DATE FILTER
    # -----------------------------
    df['date'] = pd.to_datetime(df['date'])

    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", df['date'].min())

    with col2:
        end_date = st.date_input("End Date", df['date'].max())

    df = df[(df['date'] >= pd.to_datetime(start_date)) &
            (df['date'] <= pd.to_datetime(end_date))]

    # -----------------------------
    # CATEGORY FILTER
    # -----------------------------
    category_filter = st.selectbox(
        "Filter by Category",
        ["All"] + list(df['category'].unique()),
        key="category_filter"
    )

    if category_filter != "All":
        df = df[df['category'] == category_filter]

    # -----------------------------
    # KPI CARDS
    # -----------------------------
    total_spend = df["amount"].sum()
    avg_daily = df.groupby("date")["amount"].sum().mean()
    cat = category_summary(df)

    top_category = "N/A"
    if not cat.empty:
        top_category = cat.loc[cat["amount"].idxmax()]["category"]

    c1, c2, c3 = st.columns(3)

    c1.metric("💰 Total Spend", f"₹{total_spend:.2f}")
    c2.metric("📊 Avg Daily Spend", f"₹{avg_daily:.2f}")
    c3.metric("🏆 Top Category", top_category)

    # -----------------------------
    # SMART INSIGHTS
    # -----------------------------
    st.subheader("🧠 Smart Insights")

    if total_spend > avg_daily * 10:
        st.error("🚨 Unusual spending spike detected!")

    if df['amount'].std() > 1000:
        st.warning("⚠️ Your spending is inconsistent")

    if total_spend > 10000:
        st.error("⚠️ You are overspending!")

    food_spend = df[df['category'] == "Food"]["amount"].sum()
    if food_spend > 3000:
        st.warning("🍔 High spending on Food!")

    st.success(f"💡 You spent most on {top_category}")

    # -----------------------------
    # CHARTS
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            px.bar(cat, x="category", y="amount", title="Category Spending"),
            use_container_width=True
        )

    with col2:
        pay = payment_summary(df)
        st.plotly_chart(
            px.pie(pay, names="payment_method", values="amount", title="Payment Methods"),
            use_container_width=True
        )

    # Monthly Trend
    month = monthly_summary(df)
    st.plotly_chart(
        px.line(month, x="month", y="amount", title="Monthly Trend"),
        use_container_width=True
    )

    # -----------------------------
    # DOWNLOADS
    # -----------------------------
    st.subheader("📥 Download Report")

    # CSV
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv",
        key="csv_download"
    )

    # PDF
    if st.button("Generate PDF Report", key="pdf_generate"):
        generate_pdf(total_spend, top_category)

        with open("reports/report.pdf", "rb") as f:
            st.download_button(
                "Download PDF",
                f,
                file_name="report.pdf",
                key="pdf_download"
            )