import streamlit as st

# Page config with custom theme
st.set_page_config(
    page_title='QueueGuidance - AI Queue Management',
    page_icon='🎯',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Custom CSS - Figma-Inspired Design
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* ===== GLOBAL RESET & FONT ===== */
    * {
        font-family: 'Inter', sans-serif;
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    /* ===== ROOT VARIABLES (Dark Theme) ===== */
    :root {
        --bg-primary: #111827;      /* Dark Gray-900 */
        --bg-secondary: #1F2937;   /* Dark Gray-800 */
        --surface: #374151;       /* Dark Gray-700 */
        --border: #4B5563;        /* Dark Gray-600 */
        --text-primary: #F9FAFB;   /* Light Gray-50 */
        --text-secondary: #D1D5DB; /* Light Gray-300 */
        --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --radius-xl: 1rem; /* 16px */
        --radius-lg: 0.75rem; /* 12px */
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.15);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -1px rgba(0, 0, 0, 0.15);
    }
    
    /* ===== MAIN LAYOUT ===== */
    .main {
        background: linear-gradient(135deg, var(--bg-primary) 0%, var(--bg-secondary) 100%) !important;
    }
    
    .block-container {
        padding: 2rem 2.5rem !important;
        max-width: 1440px !important;
    }
    
    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: var(--surface) !important;
        border-right: 1px solid var(--border) !important;
        width: 280px !important;
        min-width: 280px !important;
        box-shadow: var(--shadow-sm);
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        gap: 0.5rem;
    }

    [data-testid="stSidebar"] .stRadio [data-baseweb="radio"] {
        height: 44px;
        width: 100%;
        border-radius: var(--radius-lg);
        padding: 0 1rem;
        transition: background 0.2s ease;
    }
    
    [data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:has(input:checked) {
        background: var(--accent-gradient);
        color: white;
    }
    
    [data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:hover {
        background: #fafbff;
    }
    
    [data-testid="stSidebar"] .stRadio [data-baseweb="radio"]:has(input:checked):hover {
        background: var(--accent-gradient);
        opacity: 0.9;
    }
    
    [data-testid="stSidebar"] .stRadio label {
        font-weight: 500;
        font-size: 14px;
    }
    
    /* ===== MAIN HEADER ===== */
    .main-header {
        background: var(--surface);
        padding: 2.5rem;
        border-radius: var(--radius-xl);
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
    }
    
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
        font-weight: 400;
    }
    
    /* ===== FEATURE CARDS ===== */
    .feature-card {
        background: var(--surface);
        padding: 2rem;
        border-radius: var(--radius-xl);
        box-shadow: var(--shadow-sm);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
        border: 1px solid var(--border);
        text-align: center;
    }
    
    .feature-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-md);
    }
    
    .feature-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
        display: inline-block;
        background: var(--accent-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    .feature-title {
        font-size: 1.25rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .feature-text {
        color: var(--text-secondary);
        font-size: 0.95rem;
        line-height: 1.6;
    }
    
    /* ===== EXPANDER ===== */
    .st-expander {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-xl) !important;
        box-shadow: var(--shadow-sm) !important;
    }
    
    .st-expander header {
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }
    
    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <div class="main-title">🎯 QueueGuidance</div>
    <div class="subtitle">AI-Powered Intelligent Queue Management System</div>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.markdown("## 📍 Navigation")
    st.markdown("###")
    
    selected_page = st.radio(
        "Choose a page:",
        ["🏠 Home", "🎥 Setup & Process", "📊 Live Dashboard"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("### ℹ️ System Info")
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px;'>
        <p style='margin: 0; font-size: 0.9rem;'>
        ✓ AI-Powered Detection<br>
        ✓ Real-time Analytics<br>
        ✓ Multi-language Support<br>
        ✓ Smart Recommendations
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📞 Need Help?")
    st.markdown("Check the step-by-step guides on each page.")

# Main content based on selection
if selected_page == "🏠 Home":
    # Welcome Section
    st.markdown("""
    <div class='stats-container' style='text-align: center;'>
        <h2 style='color: #2c3e50; margin-bottom: 1rem;'>Welcome to QueueGuidance</h2>
        <p style='font-size: 1.2rem; color: #7f8c8d; line-height: 1.8;'>
            Transform your queue management with cutting-edge AI technology.<br>
            Upload videos, define zones, and get real-time intelligent insights.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🎥</div>
            <div class='feature-title'>Upload & Process</div>
            <div class='feature-text'>
                Upload queue videos and define custom zones using an intuitive 
                point-and-click interface. Support for multiple queue areas.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>🧠</div>
            <div class='feature-title'>AI Detection</div>
            <div class='feature-text'>
                Advanced YOLO-based person detection with high accuracy. 
                Real-time queue counting and analysis running in background.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class='feature-card'>
            <div class='feature-icon'>📊</div>
            <div class='feature-title'>Live Dashboard</div>
            <div class='feature-text'>
                Real-time analytics with auto-refresh, interactive charts, 
                and multi-language audio announcements.
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("###")
    st.markdown("###")
    
    # Quick Start Guide
    with st.expander("📖 Quick Start Guide", expanded=True):
        st.markdown("""
        ### How to Use QueueGuidance:
        
        #### Step 1: Setup & Process
        - Upload your queue video
        - Draw polygon zones around queues
        - Start AI detection
        
        #### Step 2: Live Dashboard
        - View real-time queue statistics
        - See which queue is fastest
        - Get recommendations for customers
        
        #### Step 3: Monitor & Optimize
        - Track queue performance
        - Identify bottlenecks
        - Improve customer experience
        """)
    
    st.markdown("###")
    st.success("� Use the sidebar to navigate to 'Setup & Process' to get started!")

elif selected_page == "🎥 Setup & Process":
    st.switch_page("pages/2_🎥_Video_Upload.py")
    
elif selected_page == "📊 Live Dashboard":
    st.switch_page("pages/3_🧠_Live_Dashboard.py")
