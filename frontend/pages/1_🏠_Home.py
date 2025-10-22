import streamlit as st

st.title('🏠 Home')
st.markdown('Welcome to **QueueGuidance** – your AI-powered Queue Management System.')
st.image('https://streamlit.io/images/brand/streamlit-mark-color.png', width=150)

st.markdown("---")

st.markdown("""
### 🚀 Quick Start Guide

#### 1️⃣ Test Your System
Navigate to **🧪 System Test** to run comprehensive tests:
- Video Opening & Polygon Drawing
- Language Switching
- Dynamic Queue Updates

#### 2️⃣ Upload Video
Go to **🎥 Video Upload** to upload your queue video and start detection.

#### 3️⃣ Monitor Live
Check **🧠 Live Dashboard** for real-time queue analysis and recommendations.

#### 4️⃣ View Analytics
Review **📊 Analytics** for historical trends and insights.
""")

st.markdown("---")

st.markdown("### 🎯 Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **🎥 Video Processing**
    - Upload queue videos
    - Real-time detection
    - Polygon zone definition
    """)

with col2:
    st.markdown("""
    **🧠 Smart Analysis**
    - Queue length tracking
    - Wait time estimation
    - Optimal queue recommendation
    """)

with col3:
    st.markdown("""
    **🔊 Multi-language**
    - 14+ Indian languages
    - Audio announcements
    - Dynamic switching
    """)

st.markdown("---")
st.success('✨ Navigate to **System Test** to begin testing!')

