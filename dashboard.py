import streamlit as st

from report_generator import generate_report

def show_dashboard(df):

    rows = df.shape[0]
    columns = df.shape[1]
    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("📊 Rows", rows)
    c2.metric("📋 Columns", columns)
    c3.metric("❌ Missing", missing)
    c4.metric("🔁 Duplicates", duplicates)
