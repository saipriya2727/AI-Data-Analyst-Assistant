import streamlit as st

def load_css():
    st.markdown("""
    <style>

    /* ==========================================
       GOOGLE FONT
    ========================================== */

    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    html, 
    body, 
    [class*="css"] {
        font-family: 'Poppins', sans-serif;
        font-weight: 500;
    }

    /* ==========================================
       MAIN APP BACKGROUND
    ========================================== */

    .stApp{
        background:
            radial-gradient(circle at top left,#EDE9FE 0%,transparent 40%),
            radial-gradient(circle at top right,#DBEAFE 0%,transparent 40%),
            radial-gradient(circle at bottom left,#FEF3C7 0%,transparent 35%),
            #F8FAFC;

        background-attachment: fixed;
    }

    /* ==========================================
       MAIN CONTAINER
    ========================================== */

    .block-container{
        padding-top:2rem;
        padding-bottom:2rem;
        max-width:1200px;
    }

    /* ==========================================
       HEADINGS
    ========================================== */

    /* ==========================================
    TEXT
     ========================================== */

    p,
    label,
    span,
    li{
        color:#1F2937 !important;
        font-weight:500 !important;
        line-height:1.7;
    }
                /* ==========================================
                   BUTTONS
             ========================================== */

    .stButton > button{

         background:linear-gradient(90deg,#4F46E5,#2563EB);

         color:white !important;

         font-weight:700;

         border:none;

         border-radius:10px;

      }
                /* ==========================================
           METRICS
     ========================================== */

   div[data-testid="metric-container"]{

       background:white;

       border-radius:15px;

       border:1px solid #E2E8F0;

      box-shadow:0 4px 12px rgba(0,0,0,0.08);

     }
    </style>
    """, unsafe_allow_html=True)