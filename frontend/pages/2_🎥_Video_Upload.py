import streamlit as st
import os
import sys
import subprocess
import json
import cv2
import numpy as np
import time
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw

# Page config
st.set_page_config(
    page_title='Setup & Process',
    page_icon='🎥',
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
    
    /* ===== ROOT VARIABLES (Figma Design) ===== */
    :root {
        --bg-primary: #f8f9fd;
        --bg-secondary: #eef2ff;
        --surface: #ffffff;
        --border: #e2e8f0;
        --text-primary: #1a202c;
        --text-secondary: #718096;
        --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --accent-primary: #667eea;
        --radius-xl: 1rem; /* 16px */
        --radius-lg: 0.75rem; /* 12px */
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.05), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
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
    
    /* ===== PAGE HEADER ===== */
    .page-header {
        background: var(--surface);
        padding: 2rem;
        border-radius: var(--radius-xl);
        text-align: center;
        margin-bottom: 2rem;
        border: 1px solid var(--border);
        box-shadow: var(--shadow-sm);
    }
    
    .page-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .page-subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
    }
    
    /* ===== STEP CONTAINER ===== */
    .step-container {
        background: var(--surface);
        padding: 2rem;
        border-radius: var(--radius-xl);
        margin: 1.5rem 0;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
    }
    
    .step-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1.5rem;
        display: flex;
        align-items: center;
        gap: 0.75rem;
    }
    
    .step-number {
        background: var(--accent-gradient);
        color: white;
        width: 36px;
        height: 36px;
        border-radius: 50%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-weight: 700;
        font-size: 1rem;
    }
    
    /* ===== BUTTONS ===== */
    .stButton>button {
        border-radius: var(--radius-lg) !important;
        font-weight: 600 !important;
        height: 3rem !important;
        font-size: 1rem !important;
        border: 1px solid var(--border) !important;
        background: var(--surface) !important;
        color: var(--text-primary) !important;
        transition: all 0.2s ease !important;
    }
    
    .stButton>button:hover {
        border-color: var(--accent-primary) !important;
        color: var(--accent-primary) !important;
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    .stButton>button[kind="primary"] {
        background: var(--accent-gradient) !important;
        color: white !important;
        border: none !important;
    }
    
    /* ===== FILE UPLOADER ===== */
    .stFileUploader {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        padding: 1.5rem;
    }
    
    /* ===== METRICS ===== */
    .metric-card {
        background: var(--bg-primary);
        padding: 1.5rem;
        border-radius: var(--radius-xl);
        text-align: center;
        border: 1px solid var(--border);
    }
    
    .metric-value {
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--accent-primary);
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        margin-top: 0.25rem;
    }
    
    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'video_uploaded' not in st.session_state:
    st.session_state.video_uploaded = False
if 'polygons_drawn' not in st.session_state:
    st.session_state.polygons_drawn = False
if 'detection_running' not in st.session_state:
    st.session_state.detection_running = False
if 'drawing_mode' not in st.session_state:
    st.session_state.drawing_mode = False
if 'polygons' not in st.session_state:
    st.session_state.polygons = []
if 'current_polygon' not in st.session_state:
    st.session_state.current_polygon = []
if 'first_frame' not in st.session_state:
    st.session_state.first_frame = None

# Page Header
st.markdown("""
<div class="page-header">
    <div class="page-title">🎥 Setup & Process</div>
    <div class="page-subtitle">Upload video, define queue zones, and start AI detection</div>
</div>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 📋 Progress Tracker")
    st.markdown("###")
    
    # Progress with visual indicators
    progress = 0
    if st.session_state.video_uploaded:
        progress += 33
    if st.session_state.polygons_drawn:
        progress += 33
    if st.session_state.detection_running:
        progress += 34
    
    st.progress(progress / 100)
    st.markdown(f"**{progress}% Complete**")
    st.markdown("###")
    
    # Step status
    st.markdown("### 🎯 Current Status")
    
    if st.session_state.video_uploaded:
        st.markdown('<span class="status-badge status-completed">✓ Video Uploaded</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-badge status-pending">1. Upload Video</span>', unsafe_allow_html=True)
    
    if st.session_state.polygons_drawn:
        st.markdown('<span class="status-badge status-completed">✓ Zones Defined</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-badge status-pending">2. Draw Zones</span>', unsafe_allow_html=True)
    
    if st.session_state.detection_running:
        st.markdown('<span class="status-badge status-active">⚡ Detection Active</span>', unsafe_allow_html=True)
    else:
        st.markdown('<span class="status-badge status-pending">3. Start Detection</span>', unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 💡 Quick Guide")
    st.markdown("""
    <div style='background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 8px; font-size: 0.9rem;'>
        <strong>1.</strong> Upload your queue video<br>
        <strong>2.</strong> Click to draw queue boundaries<br>
        <strong>3.</strong> Launch AI detection<br>
        <strong>4.</strong> Monitor live dashboard
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Instructions
    st.markdown("### 📖 Instructions")
    if st.session_state.drawing_mode:
        st.info("""
        **Drawing Mode:**
        - Click on image to add points
        - Points form queue zones
        - Complete each zone
        - Click "Save Zones" when done
        """)
    else:
        st.info("""
        **Quick Guide:**
        1. Upload your video
        2. Draw queue zones
        3. Start AI detection
        4. View live dashboard
        """)
    
    st.markdown("---")
    
    # Quick actions
    st.markdown("### ⚙️ Quick Actions")
    
    if st.button("🔄 Reset All", use_container_width=True):
        st.session_state.video_uploaded = False
        st.session_state.polygons_drawn = False
        st.session_state.detection_running = False
        st.rerun()
    
    if st.button("🏠 Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Step 1: Upload Video
st.markdown('<div class="step-container">', unsafe_allow_html=True)
st.markdown('<div class="step-header"><span class="step-number">1</span> Upload Your Queue Video</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    uploaded_file = st.file_uploader(
        'Choose a video file (MP4, AVI, MOV, MKV)',
        type=['mp4', 'avi', 'mov', 'mkv'],
        help="Upload a video showing your queue areas"
    )

    if uploaded_file:
        # Save video to data folder
        project_root = Path(__file__).parent.parent.parent
        data_dir = project_root / 'data'
        data_dir.mkdir(exist_ok=True)
        
        video_path = data_dir / uploaded_file.name
        with open(video_path, 'wb') as f:
            f.write(uploaded_file.read())
        
        # Extract first frame
        try:
            cap = cv2.VideoCapture(str(video_path))
            ret, frame = cap.read()
            cap.release()
            if ret:
                st.session_state.first_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except Exception as e:
            st.warning(f"Could not extract frame: {e}")
        
        st.success(f'✅ Video uploaded successfully: **{uploaded_file.name}**')
        st.session_state.video_uploaded = True
        st.session_state.current_video = str(video_path)

with col2:
    if st.session_state.video_uploaded:
        st.metric("Status", "Completed", delta="Ready")
        st.metric("Video", uploaded_file.name if uploaded_file else "Loaded")

if st.session_state.video_uploaded:
    with st.expander("📺 Preview Video", expanded=False):
        st.video(st.session_state.current_video)

st.markdown('</div>', unsafe_allow_html=True)
st.markdown("###")

# Step 2: Draw Polygons
if st.session_state.video_uploaded:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><span class="step-number">2</span> Define Queue Zones</div>', unsafe_allow_html=True)
    
    # Extract first frame if not already done
    if st.session_state.first_frame is None:
        try:
            cap = cv2.VideoCapture(st.session_state.current_video)
            ret, frame = cap.read()
            cap.release()
            if ret:
                st.session_state.first_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        except Exception as e:
            st.error(f"Error loading video: {e}")
    
    col1, col2 = st.columns([3, 1])
    
    with col1:
        if not st.session_state.drawing_mode:
            if st.button('🎨 Start Drawing Queue Zones', type='primary', use_container_width=True):
                st.session_state.drawing_mode = True
                st.rerun()
        else:
            st.info("✏️ **Drawing Mode Active** - Use the external polygon drawing tool")
            
            if st.button("🖼️ Open Drawing Window", type='primary', use_container_width=True):
                # Use the original OpenCV-based drawing from backend
                try:
                    project_root = Path(__file__).parent.parent.parent
                    backend_path = project_root / 'backend' / 'detection_engine.py'
                    
                    video_name = Path(st.session_state.current_video).name
                    video_full_path = project_root / 'data' / video_name
                    
                    python_exe = sys.executable
                    
                    cmd = f'"{python_exe}" "{backend_path}" --video "{video_full_path}" --mode polygon'
                    process = subprocess.Popen(cmd, shell=True, cwd=str(project_root))
                    
                    st.success('🎨 Drawing window opened! Click on image to draw polygons.')
                    st.info("""
                    **Controls:**
                    - **Left Click**: Add point
                    - **Right Click**: Complete polygon
                    - **Middle Click**: Delete last polygon
                    - **S Key**: Save & exit
                    - **Q Key**: Quit without saving
                    """)
                    
                except Exception as e:
                    st.error(f'❌ Error: {e}')
            
            if st.button("✅ Done Drawing", use_container_width=True):
                # Check if polygons were saved
                project_root = Path(__file__).parent.parent.parent
                polygon_file = project_root / 'data' / 'polygons.json'
                
                if polygon_file.exists():
                    with open(polygon_file) as f:
                        polygon_data = json.load(f)
                        if polygon_data.get("queue_count", 0) > 0:
                            st.session_state.polygons_drawn = True
                            st.session_state.drawing_mode = False
                            st.success("✅ Polygons loaded successfully!")
                            st.rerun()
                        else:
                            st.warning("No polygons found. Please draw at least one zone.")
                else:
                    st.warning("No polygon file found. Please draw and save polygons first.")
            
            # Preview if first frame exists
            if st.session_state.first_frame is not None:
                with st.expander("📸 Video Preview", expanded=True):
                    st.image(st.session_state.first_frame, use_container_width=True)
    
    with col2:
        st.markdown("### 📊 Status")
        
        project_root = Path(__file__).parent.parent.parent
        polygon_file = project_root / 'data' / 'polygons.json'
        
        if polygon_file.exists():
            with open(polygon_file) as f:
                polygon_data = json.load(f)
                queue_count = polygon_data.get("queue_count", 0)
                st.metric("Queue Zones", queue_count, delta="Saved")
                if queue_count > 0:
                    st.session_state.polygons_drawn = True
        else:
            st.metric("Queue Zones", len(st.session_state.polygons), delta="Drawing")
        
        if st.session_state.drawing_mode:
            st.metric("Current Zone", len(st.session_state.current_polygon), delta="Points")
        
        st.markdown("---")
        st.markdown("### 💡 Tips")
        st.info("""
        - Click to add points
        - Need 3+ points per zone
        - Click "New Queue" to finish current zone
        - Click "Save Zones" when done
        """)
    
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown("###")

# Step 3: Start Detection
if st.session_state.polygons_drawn:
    st.markdown('<div class="step-container">', unsafe_allow_html=True)
    st.markdown('<div class="step-header"><span class="step-number">3</span> Start AI Detection</div>', unsafe_allow_html=True)
    
    st.markdown("Launch the detection system to analyze your queues in real-time.")
    
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        if not st.session_state.detection_running:
            if st.button('🚀 Start Detection', type='primary', use_container_width=True):
                with st.spinner('Initializing detection system...'):
                    try:
                        # Get the QueueGuidance-Web root directory
                        project_root = Path(__file__).parent.parent.parent
                        backend_path = project_root / 'backend' / 'detection_engine.py'
                        
                        # Build video path - data folder is at project root
                        video_name = Path(st.session_state.current_video).name
                        video_full_path = project_root / 'data' / video_name
                        
                        # Get Python executable
                        python_exe = sys.executable
                        
                        # Build command with headless flag to hide video window
                        cmd = [python_exe, str(backend_path), 
                               '--video', str(video_full_path), 
                               '--mode', 'detect',
                               '--headless']
                        
                        # Hide CMD window on Windows
                        startupinfo = subprocess.STARTUPINFO()
                        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                        startupinfo.wShowWindow = subprocess.SW_HIDE
                        
                        # Start process hidden in background
                        subprocess.Popen(cmd, 
                                       startupinfo=startupinfo,
                                       cwd=str(project_root),
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
                        
                        st.success('✅ Detection system active in background!')
                        st.session_state.detection_running = True
                        st.rerun()
                        
                    except Exception as e:
                        st.error(f'❌ Error: {e}')
        else:
            st.success("✅ Detection is currently running")
    
    with col2:
        if st.session_state.detection_running:
            if st.button('🛑 Stop', use_container_width=True):
                subprocess.run('taskkill /F /IM python.exe /FI "WINDOWTITLE eq *detection*"', 
                             shell=True, capture_output=True)
                st.session_state.detection_running = False
                st.rerun()
    
    with col3:
        if st.button('� Dashboard', use_container_width=True):
            st.switch_page("pages/3_🧠_Live_Dashboard.py")
    
    st.markdown('</div>', unsafe_allow_html=True)

# Final status and next steps
if st.session_state.detection_running:
    st.markdown("###")
    st.markdown("###")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 10px; text-align: center; color: white;'>
            <h3>🎉 System Active!</h3>
            <p style='font-size: 1.1rem;'>Your queue detection is now running.</p>
            <p>Visit the Live Dashboard to see real-time analytics.</p>
        </div>
        """, unsafe_allow_html=True)
