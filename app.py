import streamlit as st

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="The Molecular Man | Expert Tuition Solutions",
    page_icon="🧪",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------------------------------------------------
# CUSTOM AESTHETIC STYLING (CSS)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    /* Main Background and Text */
    .stApp {
        background-color: #f8f9fa;
        color: #0f172a;
    }
    
    /* Headers */
    h1, h2, h3 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #1e3a8a; /* Deep Blue */
    }
    
    /* "Online Only" Banner Style */
    .online-banner {
        background: linear-gradient(90deg, #ef4444 0%, #b91c1c 100%);
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #3b82f6;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER & HERO SECTION
# -----------------------------------------------------------------------------
col1, col2 = st.columns([1, 5])

with col1:
    # --- LOGO PLACEMENT ---
    try:
        st.image("logo.png", width=130) 
    except:
        st.markdown("🧬") # Fallback if image missing

with col2:
    st.title("The Molecular Man")
    st.subheader("Expert Tuition Solutions")
    st.markdown("**Unlock Your Academic Potential | Chemistry & Beyond**")

st.markdown("---")

# -----------------------------------------------------------------------------
# IMPORTANT ANNOUNCEMENT
# -----------------------------------------------------------------------------
st.markdown("""
<div class="online-banner">
    📢 IMPORTANT UPDATE: The Molecular Man Expert Tuition Solutions is now accepting students <u>ONLY ONLINE</u>.
    <br>Learn from the comfort of your home with our specialized digital curriculum.
</div>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home & Services", "🐍 Python Bootcamp", "About Instructor", "Contact"])

st.sidebar.markdown("---")
st.sidebar.info(
    """
    **📞 Contact Us**
    \n(+91) 7339315376
    """
)

# -----------------------------------------------------------------------------
# PAGE: HOME & SERVICES
# -----------------------------------------------------------------------------
if page == "Home & Services":
    st.header("🧪 Our Online Services")
    st.write("We provide tailored tuition solutions that foster deep understanding and lasting success.")

    c1, c2 = st.columns(2)
    with c1:
        st.info("**Classes 6 - 10 (All Subjects)**")
        st.write("A solid foundation in core concepts with a structured approach to critical thinking.")
    with c2:
        st.info("**Classes 11 - 12 (Specialized Chemistry)**")
        st.write("Deepen your understanding of Organic, Inorganic, and Physical Chemistry.")

    c3, c4 = st.columns(2)
    with c3:
        st.error("**NEET & JEE Aspirants**")
        st.write("Intensive, goal-oriented coaching for comprehensive exam readiness.")
    with c4:
        st.success("**Why Choose Us?**")
        st.write("- Individualized Learning Plans\n- Holistic Development\n- Proven Results")

# -----------------------------------------------------------------------------
# PAGE: PYTHON BOOTCAMP
# -----------------------------------------------------------------------------
elif page == "🐍 Python Bootcamp":
    st.header("🚀 New: Python Bootcamp")
    st.markdown("### *Master the language of Data Science and AI*")
    
    bc_col1, bc_col2 = st.columns([1, 1])
    
    with bc_col1:
        # --- POSTER PLACEMENT ---
        try:
            st.image("poster.jpg", caption="Join our Weekend Bootcamp!", use_container_width=True)
        except:
            st.warning("⚠️ 'poster.jpg' not found.")

    with bc_col2:
        st.success("##### 📅 Schedule: Saturdays & Sundays")
        st.write("""
        Join **M. Mohammed Salmaan** for an intensive weekend bootcamp designed to take you from zero to hero in Python.
        
        **What we cover:**
        - ✅ Python Basics & Syntax
        - ✅ Data Structures & Algorithms
        - ✅ Introduction to Data Science Libraries (Pandas, NumPy)
        
        **Mode:** Online Live Classes
        """)
        if st.button("Enquire About Bootcamp"):
            st.markdown("**Send us a WhatsApp message at (+91) 7339315376**")

# -----------------------------------------------------------------------------
# PAGE: ABOUT INSTRUCTOR
# -----------------------------------------------------------------------------
elif page == "About Instructor":
    st.header("👨‍🏫 About The Instructor")
    
    col_img, col_text = st.columns([1, 3])
    
    with col_img:
        # --- YOUR IMAGE PLACEMENT ---
        try:
            st.image("image.jpeg", caption="M. Mohammed Salmaan", width=200)
        except:
            st.warning("⚠️ 'image.jpeg' not found.")
            
    with col_text:
        st.markdown("### Mohammed Salmaan M")
        st.caption("M.Sc. Chemistry | B.Ed | Data Science | Gen AI")
        
        st.write("""
        With a strong academic background in Chemistry (M.Sc., 80%) and a passion for teaching, 
        I have dedicated my career to helping students achieve academic excellence.
        
        My journey includes:
        - **Academic Excellence:** 9.4 CGPA in Class 10, Gold Medalist in B.Sc. & M.Sc.
        - **Industry Experience:** Former Production Officer at Chemplast Sanmar & Aurolab.
        - **Teaching Experience:** Founder of Tuition Solutions and The Molecular Man.
        
        Currently, I am integrating **Generative AI and Data Science** into modern education to prepare students for the future.
        """)

# -----------------------------------------------------------------------------
# PAGE: CONTACT
# -----------------------------------------------------------------------------
elif page == "Contact":
    st.header("📞 Contact Us")
    st.markdown("""
    **📱 Phone / WhatsApp:** (+91) 7339315376
    **📍 Location:** Madurai, Tamil Nadu (Operating Online)
    """)
    st.write("---")
    st.write("© 2026 The Molecular Man - Expert Tuition Solutions")