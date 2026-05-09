import pandas as pd

def load_data(conn):
    return pd.read_sql_query("SELECT * FROM expenses", conn)

def category_summary(df):
    return df.groupby("category")["amount"].sum().reset_index()

def monthly_summary(df):
    df['date'] = pd.to_datetime(df['date'])
    df['month'] = df['date'].dt.to_period("M").astype(str)
    return df.groupby("month")["amount"].sum().reset_index()

def payment_summary(df):
    return df.groupby("payment_method")["amount"].sum().reset_index()