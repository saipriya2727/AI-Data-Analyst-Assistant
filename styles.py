import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* ==========================================
       GOOGLE FONT
    ========================================== */

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"]{
        font-family:'Poppins',sans-serif;
    }

    /* ==========================================
       MAIN BACKGROUND
    ========================================== */

    .stApp{
        background:
            radial-gradient(circle at top left,#EDE9FE 0%,transparent 40%),
            radial-gradient(circle at top right,#DBEAFE 0%,transparent 40%),
            radial-gradient(circle at bottom left,#FEF3C7 0%,transparent 35%),
            #F8FAFC;

        background-attachment:fixed;
    }

    /* ==========================================
       SIDEBAR
    ========================================== */

    section[data-testid="stSidebar"]{

        background:#FFFFFF !important;

        border-right:1px solid #E2E8F0;

        padding-top:15px;

    }

    /* ==========================================
       SIDEBAR TEXT
    ========================================== */

    section[data-testid="stSidebar"] *{

        color:#1F2937 !important;

    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3{

        color:#1E3A8A !important;

        font-weight:700 !important;

    }

    /* ==========================================
       SIDEBAR CARDS
    ========================================== */

    .stRadio{

        background:#EEF6FF;

        border:1px solid #D6E8FF;

        border-radius:15px;

        padding:15px;

        margin-bottom:18px;

    }

    .stFileUploader{

        background:#EEF6FF;

        border:1px solid #D6E8FF;

        border-radius:15px;

        padding:15px;

        margin-bottom:18px;

    }

    .stAlert{

        border-radius:15px;

    }

    /* ==========================================
       FILE UPLOADER
    ========================================== */

    [data-testid="stFileUploader"]{

        background:#EEF6FF;

        border-radius:15px;

        border:1px solid #D6E8FF;

    }

    [data-testid="stFileUploader"] button{

        background:#2563EB !important;

        color:white !important;

        border:none !important;

        border-radius:10px;

        font-weight:700;

    }

    [data-testid="stFileUploader"] small{

        color:#64748B !important;

    }

    /* ==========================================
       RADIO BUTTONS
    ========================================== */

    .stRadio label{

        font-weight:600 !important;

    }

    /* ==========================================
       MAIN CONTAINER
    ========================================== */

    .block-container{

        max-width:1200px;

        padding-top:2rem;

        padding-bottom:2rem;

    }

    /* ==========================================
       TITLES
    ========================================== */

    h1{

        color:#1E3A8A !important;

        font-weight:800 !important;

    }

    h2{

        color:#0F172A !important;

        font-weight:700 !important;

    }

    h3{

        color:#1E293B !important;

        font-weight:700 !important;

    }

    h4{

        color:#334155 !important;

        font-weight:600 !important;

    }

    /* ==========================================
       TEXT
    ========================================== */

    p,
    span,
    label,
    li{

        color:#1F2937 !important;

        font-weight:500;

        line-height:1.6;

    }

    /* ==========================================
       BUTTONS
    ========================================== */

    .stButton > button{

        background:linear-gradient(90deg,#4F46E5,#2563EB);

        color:white !important;

        border:none;

        border-radius:10px;

        font-weight:700;

        transition:.3s;

    }

    .stButton > button:hover{

        transform:translateY(-2px);

        box-shadow:0 8px 20px rgba(37,99,235,.25);

    }

    /* ==========================================
       METRIC CARDS
    ========================================== */

    div[data-testid="metric-container"]{

        background:white;

        border-radius:15px;

        border:1px solid #E2E8F0;

        box-shadow:0 4px 12px rgba(0,0,0,.08);

        padding:10px;

    }

    /* ==========================================
       DATAFRAME
    ========================================== */

    div[data-testid="stDataFrame"]{

        border-radius:12px;

        overflow:hidden;

    }

    /* ==========================================
       EXPANDER
    ========================================== */

    .streamlit-expanderHeader{

        color:#1E293B !important;

        font-weight:700 !important;

    }

    /* ==========================================
       SUCCESS MESSAGE
    ========================================== */

    div[data-testid="stAlert"]{

        border-radius:15px;

    }

    /* ==========================================
       MOBILE
    ========================================== */

    @media(max-width:768px){

        .block-container{

            padding-top:1rem;

            padding-bottom:1rem;

        }

        h1{

            font-size:28px !important;

        }

        h2{

            font-size:22px !important;

        }

        h3{

            font-size:18px !important;

        }

    }

    </style>
    """, unsafe_allow_html=True)