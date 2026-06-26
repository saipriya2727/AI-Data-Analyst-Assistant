import streamlit as st
from styles import load_css
from config import model

from pdf_utils import extract_pdf_text

from excel_utils import (
    load_data,
    get_dataset_summary,
    answer_data_question,
)

from dashboard import show_dashboard
from charts import show_charts
from insights import show_ai_insights
from report_generator import generate_report
# -----------------------------
# Session State
# -----------------------------

if "chat" not in st.session_state:
    st.session_state.chat = model.start_chat(history=[])

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = None

if "df" not in st.session_state:
    st.session_state.df = None

if "data_summary" not in st.session_state:
    st.session_state.data_summary = None
# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="AI Data Analyst Assistant",
    page_icon="🤖",
    layout="wide"
)
load_css()
# -----------------------------
# Navigation
# -----------------------------

PAGES = [
    "🏠 Home",
    "🤖 AI Chat",
    "📄 PDF Chat",
    "📊 Data Analysis",
    "📈 Dashboard",
    "📥 AI Report",
    "ℹ️ About"
]
# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:

    st.image("logo.png", width=150)

    st.markdown("# 🤖 AI Data Analyst")
    st.caption("Powered by Google Gemini")


    st.title("AI Data Analyst")

    st.success("🟢 Gemini Connected")

    st.markdown("### Navigation")

    page = st.radio(
    "📂 Navigation",
    PAGES
   )

    st.divider()

    st.write("Welcome Sai Priya! 👋")

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []
        st.session_state.chat = model.start_chat(history=[])

        st.session_state.pdf_text = None
        st.session_state.df = None
        st.session_state.data_summary = None

        st.rerun()

    st.divider()

    uploaded_pdf = st.file_uploader(
        "📄 Upload PDF",
        type=["pdf"]
    )

    if uploaded_pdf:

        st.session_state.pdf_text = extract_pdf_text(uploaded_pdf)

        st.success("✅ PDF Uploaded")

    st.divider()

    uploaded_data = st.file_uploader(
        "📊 Upload CSV / Excel",
        type=["csv", "xlsx"]
    )

    if uploaded_data:

        df = load_data(uploaded_data)

        st.session_state.df = df

        st.session_state.data_summary = get_dataset_summary(df)

        st.success("✅ Dataset Loaded")

    st.divider()

    st.markdown("### 🛠 Built With")

    st.write("Python")

    st.write("Streamlit")

    st.write("Google Gemini")

    st.write("Pandas")

    st.write("Plotly")
# -----------------------------
# Home Page
# -----------------------------

if page == "🏠 Home":

    st.title("🤖 AI Data Analyst Assistant")

    st.markdown("""
### AI-Powered Document Analysis & Data Analytics

Analyze PDFs, explore datasets, generate AI insights, build interactive dashboards, and create professional reports—all in one application.
""")

    st.divider()

    # =============================
    # Features
    # =============================

    st.subheader("🚀 Key Features")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>🤖</h2>

<h4>AI Chat</h4>

Ask questions using Google Gemini AI.

</div>
""", unsafe_allow_html=True)

    with col2:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>📄</h2>

<h4>PDF Chat</h4>

Upload PDF documents and ask questions instantly.

</div>
""", unsafe_allow_html=True)

    with col3:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>📊</h2>

<h4>Data Analysis</h4>

Analyze CSV & Excel datasets with AI assistance.

</div>
""", unsafe_allow_html=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>📈</h2>

<h4>Dashboard</h4>

Interactive KPIs, summaries, and visual analytics.

</div>
""", unsafe_allow_html=True)

    with col5:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>💡</h2>

<h4>AI Insights</h4>

Automatically discover patterns and useful insights.

</div>
""", unsafe_allow_html=True)

    with col6:
        st.markdown("""
<div style='padding:18px;
border-radius:12px;
background-color:#F8FAFC;
border:1px solid #E5E7EB;
text-align:center;
height:180px;'>

<h2>📥</h2>

<h4>AI Reports</h4>

Generate professional PDF reports instantly.

</div>
""", unsafe_allow_html=True)

    st.divider()

    # =============================
    # Technology Stack
    # =============================

    st.subheader("🛠 Technology Stack")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Language", "Python")

    with col2:
        st.metric("Framework", "Streamlit")

    with col3:
        st.metric("AI Model", "Gemini")

    with col4:
        st.metric("Visualization", "Plotly")

    st.divider()

    # =============================
    # Project Highlights
    # =============================

    st.subheader("📌 Project Highlights")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Features", "7+")

    with c2:
        st.metric("Modules", "8")

    with c3:
        st.metric("Reports", "PDF")

    with c4:
        st.metric("AI Powered", "100%")

    st.success("👈 Use the navigation menu in the sidebar to explore the application.")
# -----------------------------
# About Page
# -----------------------------

if page == "ℹ️ About":

    st.title("ℹ️ About AI Data Analyst Assistant")

    st.markdown("""
### An AI-powered platform for document analysis, data analytics, dashboards, and intelligent reporting.

This application helps users analyze documents and datasets quickly using **Google Gemini AI**, **Python**, and **Streamlit**.
""")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("🎯 Project Features")

        st.markdown("""
- 🤖 AI Chat Assistant
- 📄 PDF Question Answering
- 📊 CSV & Excel Data Analysis
- 📈 Interactive Dashboard
- 💡 AI-generated Insights
- 📥 Professional PDF Reports
- ⚡ Fast & User-Friendly Interface
""")

    with col2:

        st.subheader("🛠 Technologies Used")

        st.markdown("""
- Python
- Streamlit
- Google Gemini API
- Pandas
- Plotly
- ReportLab
- PyPDF
""")

    st.divider()

    st.subheader("👩‍💻 Developer")

    st.success("""
**Sai Priya**

B.Tech – Computer Science Engineering (AI & ML)

Passionate about Artificial Intelligence, Machine Learning, Data Analytics, and Generative AI.
""")

    st.divider()

    st.subheader("🚀 Future Enhancements")

    st.markdown("""
- 📊 Advanced AI Analytics
- 🌐 Multi-language Support
- ☁ Cloud Deployment
- 📁 Multiple File Upload
- 📈 Predictive Analytics
- 🔐 User Authentication
""")
# -----------------------------
# AI Chat
# -----------------------------

if page == "🤖 AI Chat":

    st.title("💬 AI Chat")

    st.write("Ask any question and chat with AI.")

    # Display Chat History
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input("Ask me anything...")

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                response = st.session_state.chat.send_message(prompt)

                st.markdown(response.text)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response.text
            }
        )
# -----------------------------
# PDF Chat
# -----------------------------

if page == "📄 PDF Chat":

    st.title("📄 PDF Chat")

    st.write("Upload a PDF from the sidebar and ask questions about it.")

    if st.session_state.pdf_text is None:

        st.warning("Please upload a PDF first.")

    else:

        prompt = st.chat_input("Ask a question about the PDF...")

        if prompt:

            with st.chat_message("user"):
                st.markdown(prompt)

            with st.chat_message("assistant"):

                with st.spinner("Reading PDF..."):

                    full_prompt = f"""
You are an AI Assistant.

Answer ONLY using the uploaded PDF.

If the answer is not available in the PDF, reply:

'I couldn't find that information in the uploaded PDF.'

PDF Content:

{st.session_state.pdf_text}

Question:

{prompt}
"""

                    response = st.session_state.chat.send_message(full_prompt)

                    st.markdown(response.text)
# -----------------------------
# Data Analysis
# -----------------------------

if page == "📊 Data Analysis":

    st.title("📊 Data Analysis")

    if st.session_state.df is None:

        st.warning("Please upload a CSV or Excel file from the sidebar.")

    else:

        st.success("✅ Dataset Loaded Successfully!")

        st.dataframe(st.session_state.df)

        st.subheader("📋 Dataset Summary")

        st.text(st.session_state.data_summary)

        prompt = st.chat_input("Ask about your dataset...")

        if prompt:

            with st.chat_message("user"):
                st.markdown(prompt)

            pandas_answer = answer_data_question(
                st.session_state.df,
                prompt
            )

            if pandas_answer is not None:

                with st.chat_message("assistant"):
                    st.markdown(pandas_answer)

            else:

                full_prompt = f"""
You are an AI Data Analyst.

Dataset Summary:

{st.session_state.data_summary}

Answer ONLY using the dataset summary.

Question:

{prompt}
"""

                response = st.session_state.chat.send_message(full_prompt)

                with st.chat_message("assistant"):
                    st.markdown(response.text)
# -----------------------------
# Dashboard
# -----------------------------

if page == "📈 Dashboard":

    st.title("📈 AI Dashboard")

    st.info(
        "Analyze your uploaded dataset using AI-powered insights, interactive charts, and statistical summaries."
    )

    if st.session_state.df is None:

        st.warning("⚠ Please upload a CSV or Excel file first.")

    else:

        df = st.session_state.df

        st.success("✅ Dashboard loaded successfully!")

        # -----------------------------
        # KPI Cards
        # -----------------------------
        st.subheader("📊 Dataset Overview")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("📄 Rows", df.shape[0])

        with col2:
            st.metric("📑 Columns", df.shape[1])

        with col3:
            st.metric("❌ Missing Values", int(df.isnull().sum().sum()))

        with col4:
            st.metric("🔄 Duplicate Rows", int(df.duplicated().sum()))

        st.divider()

        # -----------------------------
        # Dashboard Visuals
        # -----------------------------
        st.subheader("📈 Dashboard")

        show_dashboard(df)

        st.divider()

        # -----------------------------
        # Dataset Statistics
        # -----------------------------
        with st.expander("📋 Dataset Statistics", expanded=True):

            st.dataframe(
                df.describe().round(2),
                use_container_width=True
            )

        # -----------------------------
        # Dataset Preview
        # -----------------------------
        with st.expander("👀 Dataset Preview"):

            st.dataframe(
                df.head(10),
                use_container_width=True
            )

        # -----------------------------
        # AI Insights
        # -----------------------------
        with st.expander("🤖 AI Insights", expanded=True):

            show_ai_insights(df)

        # -----------------------------
        # Interactive Charts
        # -----------------------------
        with st.expander("📊 Interactive Charts", expanded=True):

            show_charts(df)
# -----------------------------
# AI Report
# -----------------------------

if page == "📥 AI Report":

    st.title("📥 AI Report Generator")

    if st.session_state.df is None:

        st.warning("Please upload a dataset first.")

    else:

        st.write("Generate a professional AI report for your dataset.")

        if st.button("📄 Generate Report"):

            report = generate_report(
                st.session_state.data_summary,
                "Automatically generated by AI Data Analyst Assistant."
            )

            with open(report, "rb") as file:

                st.download_button(
                    "⬇ Download AI Report",
                    file,
                    file_name="AI_Report.pdf",
                    mime="application/pdf"
                )
                st.divider()

                st.markdown(
"""
<div style="text-align:center">

Made with ❤️ by <b>Sai Priya</b>

AI Data Analyst Assistant

Python • Streamlit • Gemini • Plotly

Version 1.0

</div>
""",
unsafe_allow_html=True)