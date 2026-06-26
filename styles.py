import streamlit as st

def load_css():

    st.markdown("""
    <style>

    /* ===========================
       Main App Background
    =========================== */

    .stApp{

        background:
        radial-gradient(circle at top left,#FDEBFF 0%,transparent 35%),
        radial-gradient(circle at top right,#D8F3FF 0%,transparent 35%),
        radial-gradient(circle at bottom left,#FFF7D6 0%,transparent 30%),
        linear-gradient(135deg,#F8FAFF 0%,#FDFBFF 100%);

        background-attachment: fixed;

    }

    /* ===========================
       Main Container
    =========================== */

    .main{

        padding:2rem;

    }

    /* ===========================
       Sidebar
    =========================== */

    section[data-testid="stSidebar"]{

        background:linear-gradient(
        180deg,
        #ECE2FF 0%,
        #F6F2FF 100%
        );

        border-right:1px solid #E5E7EB;

    }

    /* ===========================
       Headings
    =========================== */

    h1{

        font-size:42px;

        font-weight:800;

        background:linear-gradient(
        90deg,
        #5B4BFF,
        #2F80ED
        );

        -webkit-background-clip:text;

        -webkit-text-fill-color:transparent;

    }

    h2{

        color:#243B53;

        font-weight:700;

    }

    h3{

        color:#394867;

    }

    /* ===========================
       Cards
    =========================== */

    div[data-testid="stMetric"]{

        background:rgba(255,255,255,.72);

        backdrop-filter:blur(12px);

        border-radius:18px;

        padding:18px;

        border:1px solid rgba(255,255,255,.6);

        box-shadow:
        0 8px 25px rgba(120,120,180,.12);

    }

    /* ===========================
       Buttons
    =========================== */

    .stButton>button{

        border-radius:12px;

        background:linear-gradient(
        90deg,
        #8B5CF6,
        #4F46E5
        );

        color:white;

        font-weight:700;

        border:none;

        height:48px;

        width:100%;

        transition:0.3s;

    }

    .stButton>button:hover{

        transform:translateY(-2px);

        box-shadow:0 8px 18px rgba(79,70,229,.35);

    }

    /* ===========================
       Download Button
    =========================== */

    .stDownloadButton>button{

        border-radius:12px;

        background:linear-gradient(
        90deg,
        #10B981,
        #06B6D4
        );

        color:white;

        border:none;

        font-weight:700;

        width:100%;

    }

    /* ===========================
       Expander
    =========================== */

    .streamlit-expanderHeader{

        font-size:18px;

        font-weight:700;

    }

    /* ===========================
       DataFrame
    =========================== */

    div[data-testid="stDataFrame"]{

        border-radius:15px;

        overflow:hidden;

        box-shadow:0 5px 18px rgba(0,0,0,.08);

    }

    /* ===========================
       Success Box
    =========================== */

    div[data-testid="stAlert"]{

        border-radius:15px;

    }

    /* ===========================
       Chat Messages
    =========================== */

    div[data-testid="stChatMessage"]{

        border-radius:15px;

        background:rgba(255,255,255,.75);

        backdrop-filter:blur(8px);

    }

    </style>
    """, unsafe_allow_html=True)