import streamlit as st
import os

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
# HELPER FUNCTION TO FIND IMAGES
# -----------------------------------------------------------------------------
def get_image_path(filename_base):
    """
    Checks for .jpg, .jpeg, or .png versions of a filename 
    to avoid 'File Not Found' errors.
    """
    extensions = [".png", ".jpg", ".jpeg"] 
    for ext in extensions:
        if os.path.exists(filename_base + ext):
            return filename_base + ext
        if os.path.exists(filename_base + ext.upper()):
            return filename_base + ext.upper()
    return None

# -----------------------------------------------------------------------------
# CUSTOM AESTHETIC STYLING (CSS)
# -----------------------------------------------------------------------------
st.markdown("""
<style>
    .stApp { background-color: #f8f9fa; color: #0f172a; }
    h1, h2, h3 { font-family: 'Helvetica Neue', sans-serif; font-weight: 700; color: #1e3a8a; }
    
    /* Banner Style */
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
    
    /* Card Style for Bots */
    .bot-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* Button Styling */
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 24px;
        font-weight: 600;
    }
    .stButton>button:hover { background-color: #3b82f6; }
</style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HEADER & HERO SECTION
# -----------------------------------------------------------------------------
col1, col2 = st.columns([1, 5])

with col1:
    logo_path = get_image_path("logo")
    if logo_path:
        st.image(logo_path, width=130)
    else:
        st.markdown("<div style='font-size: 80px;'>🧪</div>", unsafe_allow_html=True)

with col2:
    st.title("The Molecular Man")
    st.subheader("Expert Tuition Solutions")
    st.markdown("**Unlock Your Academic Potential | Chemistry | Physics | Maths | Biology | Python & Beyond**")

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

# UPDATED MENU with "The Molecular Man AI"
page = st.sidebar.radio("Go to", [
    "Home & Services", 
    "✨ The Molecular Man AI", 
    "🐍 Python Bootcamp", 
    "🤖 Student Support Bots", 
    "About Instructor", 
    "Contact"
])

st.sidebar.markdown("---")
st.sidebar.info("**📞 Contact Us**\n\n(+91) 7339315376")

# -----------------------------------------------------------------------------
# PAGE: HOME & SERVICES
# -----------------------------------------------------------------------------
if page == "Home & Services":
    st.header("🧪 Our Online Services")
    st.write("We provide tailored tuition solutions that foster deep understanding and lasting success.")

    c1, c2 = st.columns(2)
    with c1:
        st.info("**Classes 6 - 10 (Science('Physics','Chemistry'&'Biology') | Maths('Basic','Standard' & 'Advanced' | | SST | Hindi)**")
        st.write("A solid foundation in core concepts with a structured approach to critical thinking.")
    with c2:
        st.info("**Classes 11 - 12 (Specialized & Simplified Chemistry | Physics | Biology | Maths )**")
        st.write("Deepen your understanding of Organic, Inorganic, and Physical Chemistry.")

    c3, c4 = st.columns(2)
    with c3:
        st.error("**NEET & JEE Aspirants**")
        st.write("Intensive, goal-oriented coaching for comprehensive exam readiness.")
    with c4:
        st.success("**Why Choose Us?**")
        st.write("- Individualized Learning Plans\n- Holistic Development\n- Proven Results")
        st.write("**NO EXTRA CHARGES FOR IGCSE,ICSE,ISC etc.,**")
        st.write("**AI based Student Monitoring System through out the session**")

# -----------------------------------------------------------------------------
# PAGE: THE MOLECULAR MAN AI (NEW)
# -----------------------------------------------------------------------------
elif page == "✨ The Molecular Man AI":
    st.header("✨ The Molecular Man AI")
    st.markdown("### *The Most Powerful AI for Students*")
    st.write("Experience our most advanced tool yet. This AI understands full problem statements and provides human-like reasoning.")

    st.markdown("---")
    
    # Feature Card
    with st.container():
        col_icon, col_details = st.columns([1, 4])
        
        with col_icon:
            st.markdown("<div style='font-size: 70px; text-align: center;'>🧠</div>", unsafe_allow_html=True)
            
        with col_details:
            st.markdown("### The Molecular Man AI - v1")
            st.write("""
            **Capabilities:**
            - 📄 Solves full Word Problems (Age, Trigonometry, etc.)
            - 🔢 Auto-extracts numbers from text
            - 📝 Provides Step-by-Step Logic
            """)
            
            # The Link Button requested
            st.link_button("🚀 Launch The Most Powerful AI", "https://the-molecular-man-ai-v1.streamlit.app/")

# -----------------------------------------------------------------------------
# PAGE: PYTHON BOOTCAMP
# -----------------------------------------------------------------------------
elif page == "🐍 Python Bootcamp":
    st.header("🚀 New: Python Bootcamp")
    st.markdown("### *Master the language of Data Science and AI*")
    
    bc_col1, bc_col2 = st.columns([1, 1])
    
    with bc_col1:
        poster_path = get_image_path("poster") 
        if poster_path:
            st.image(poster_path, caption="Join our Weekend Bootcamp!", use_container_width=True)
        else:
            st.warning("⚠️ 'poster.jpg' not found. Please check the filename.")

    with bc_col2:
        st.success("##### 📅 Schedule: Saturdays & Sundays (2hr/Week)")
        st.write("""
        Join **Mohammed Salmaan M** for an intensive weekend bootcamp designed to take you from zero to hero in Python.
        
        **What we cover:**
        - ✅ Python Basics & Syntax
        - ✅ Data Structures & Algorithms
        - ✅ Introduction to Data Science Libraries (Pandas, NumPy)
        
        **Mode:** Online Live Classes  
        **Requirement:** A basic system configured to run Jupyter Notebook.
        """)
        if st.button("Enquire About Bootcamp"):
            st.markdown("**Send us a WhatsApp message at (+91) 7339315376**")

# -----------------------------------------------------------------------------
# PAGE: STUDENT SUPPORT BOTS
# -----------------------------------------------------------------------------
elif page == "🤖 Student Support Bots":
    st.header("🤖 Student Support Bots")
    st.write("Access our specialized tools for specific topics.")
    
    st.markdown("---")

    # Bot Card 1: Quadratic Solver
    with st.container():
        col_icon, col_details = st.columns([1, 4])
        
        with col_icon:
            st.markdown("<div style='font-size: 60px; text-align: center;'>🧮</div>", unsafe_allow_html=True)
            
        with col_details:
            st.markdown("### Quadratic Equation Solver")
            st.write("Struggling with roots? Just enter your coefficients (a, b, c) and get the solution steps instantly.")
            st.link_button("🚀 Launch Solver Bot", "https://molecular-man-bot-01.streamlit.app/")

# -----------------------------------------------------------------------------
# PAGE: ABOUT INSTRUCTOR
# -----------------------------------------------------------------------------
elif page == "About Instructor":
    st.header("👨‍🏫 About The Instructor")
    
    col_img, col_text = st.columns([1, 3])
    
    with col_img:
        profile_path = get_image_path("profile") 
        if profile_path:
            st.image(profile_path, caption="Mohammed Salmaan M - The Founder", width=200)
        else:
            st.warning("⚠️ 'profile.jpg' not found. Please check the filename.")
            
    with col_text:
        st.markdown("### Mohammed Salmaan M")
        st.caption("M.Sc. Chemistry | B.Ed | Gen AI | Data Science")
        
        st.write("""
        With a strong academic background in Chemistry (M.Sc., 80%) and a passion for teaching, 
        I have dedicated my career to helping students achieve academic excellence.
        
        My journey includes:
        - **Academic Excellence:** 9.4 CGPA in Class 10, Gold Medalist in B.Sc. & M.Sc.
        - **Industry Experience:** Former Production Officer @ Chemplast Sanmar & Production Chemist @ Aurolab.
        - **Teaching Experience:** Founder of The Molecular Man Expert Tuition Solutions, and Implemented AI in Teaching Effectively - Industry Revolutionized.
        
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
    st.write("© 2026 Mohammed Salmaan - The Molecular Man - Expert Tuition Solutions")