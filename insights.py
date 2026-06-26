import streamlit as st


def show_ai_insights(df):

    st.subheader("🤖 AI Insights")

    rows = df.shape[0]
    cols = df.shape[1]
    missing = int(df.isnull().sum().sum())
    duplicates = int(df.duplicated().sum())

    st.success(f"✅ Dataset contains {rows} rows and {cols} columns.")

    if missing == 0:
        st.info("✅ No missing values found.")
    else:
        st.warning(f"⚠️ Missing values found: {missing}")

    if duplicates == 0:
        st.success("✅ No duplicate rows found.")
    else:
        st.warning(f"⚠️ Duplicate rows found: {duplicates}")

    numeric = df.select_dtypes(include="number").columns

    if len(numeric) > 0:
        st.info(f"📊 Numeric Columns: {', '.join(numeric)}")

    categorical = df.select_dtypes(include="object").columns

    if len(categorical) > 0:
        st.info(f"📝 Categorical Columns: {', '.join(categorical)}")