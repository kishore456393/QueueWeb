import streamlit as st
import subprocess
import os
import sys
import time
import json
from pathlib import Path

st.set_page_config(page_title='System Test - QueueGuidance', layout='wide', page_icon='🧪')

st.title('🧪 Complete System Test')
st.markdown('''
### Test all three critical features:
1. ✅ **Video Opening & Polygon Drawing**
2. ✅ **Language Switching without Errors**
3. ✅ **Queue Count Dynamic Updates**
''')

# Status tracking
if 'test1_status' not in st.session_state:
    st.session_state.test1_status = 'pending'
if 'test2_status' not in st.session_state:
    st.session_state.test2_status = 'pending'
if 'test3_status' not in st.session_state:
    st.session_state.test3_status = 'pending'

# Get project root (go back to QueueGuidance folder)
project_root = Path(__file__).parent.parent.parent / 'QueueGuidance'

st.markdown("---")

# TEST 1: Video Opening & Polygon Drawing
st.markdown("### 📋 TEST 1: Video Opening & Polygon Drawing")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    **What this tests:**
    - Video opens successfully
    - Polygon drawing interface appears
    - Can draw polygons by clicking
    - Save polygons with 'S' key
    """)

with col2:
    status_icon = {
        'pending': '⏳',
        'running': '🔄',
        'success': '✅',
        'failed': '❌'
    }
    st.markdown(f"### {status_icon[st.session_state.test1_status]}")

if st.button('▶️ Run Test 1: Video & Polygons', key='test1_btn'):
    st.session_state.test1_status = 'running'
    with st.spinner('Starting video handler...'):
        try:
            # Run the robust video handler
            cmd = f'cd "{project_root}" && python robust_video_handler.py'
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            st.info('✅ Video handler started! A window should open for polygon drawing.')
            st.info('⚠️ After drawing polygons, press "S" to save and continue.')
            st.session_state.test1_status = 'running'
            st.markdown('**Instructions:**')
            st.markdown('- Left Click: Add point')
            st.markdown('- Right Click: Finish polygon')
            st.markdown('- S: Save & Continue')
            st.markdown('- Q: Quit')
        except Exception as e:
            st.error(f'❌ Failed to start video handler: {e}')
            st.session_state.test1_status = 'failed'

st.markdown("---")

# TEST 2: Dashboard Language Switching
st.markdown("### 📋 TEST 2: Dashboard Language Switching")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    **What this tests:**
    - Dashboard opens successfully
    - Language selector works
    - No errors when switching languages
    - UI text changes to selected language
    """)

with col2:
    st.markdown(f"### {status_icon[st.session_state.test2_status]}")

if st.button('▶️ Run Test 2: Language Switching', key='test2_btn'):
    st.session_state.test2_status = 'running'
    with st.spinner('Starting professional dashboard...'):
        try:
            # Run the professional dashboard
            cmd = f'cd "{project_root}" && start cmd /k "python -m streamlit run professional_dashboard.py"'
            subprocess.Popen(cmd, shell=True)
            st.success('✅ Dashboard started!')
            st.info('🌐 Try changing languages in the dashboard sidebar')
            st.info('📍 Dashboard should open at http://localhost:8503')
            st.markdown('[Open Dashboard](http://localhost:8503)', unsafe_allow_html=True)
            st.session_state.test2_status = 'running'
        except Exception as e:
            st.error(f'❌ Failed to start dashboard: {e}')
            st.session_state.test2_status = 'failed'

st.markdown("---")

# TEST 3: Queue Count Dynamic Updates
st.markdown("### 📋 TEST 3: Queue Count Dynamic Updates")
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("""
    **What this tests:**
    - Data generator shows queue statistics
    - Queue count matches number of polygons
    - Counts update dynamically
    - Audio announcements work every 10 seconds
    """)

with col2:
    st.markdown(f"### {status_icon[st.session_state.test3_status]}")

if st.button('▶️ Run Test 3: Dynamic Updates', key='test3_btn'):
    st.session_state.test3_status = 'running'
    with st.spinner('Starting data generator...'):
        try:
            # Run the data generator
            cmd = f'cd "{project_root}" && start cmd /k "python professional_data_generator.py"'
            subprocess.Popen(cmd, shell=True)
            st.success('✅ Data generator started!')
            st.info('📊 Queue count should match number of polygons drawn')
            st.info('🔊 Audio announcements should occur every 10 seconds')
            st.session_state.test3_status = 'running'
        except Exception as e:
            st.error(f'❌ Failed to start data generator: {e}')
            st.session_state.test3_status = 'failed'

st.markdown("---")

# Run All Tests Button
st.markdown("### 🚀 Quick Actions")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('🎯 Run ALL Tests', type='primary', use_container_width=True):
        st.info('Running all tests sequentially...')
        
        # Test 1
        try:
            cmd = f'cd "{project_root}" && start cmd /k "python robust_video_handler.py"'
            subprocess.Popen(cmd, shell=True)
            st.session_state.test1_status = 'running'
            time.sleep(2)
        except:
            st.session_state.test1_status = 'failed'
        
        # Test 2
        try:
            cmd = f'cd "{project_root}" && start cmd /k "python -m streamlit run professional_dashboard.py"'
            subprocess.Popen(cmd, shell=True)
            st.session_state.test2_status = 'running'
            time.sleep(2)
        except:
            st.session_state.test2_status = 'failed'
        
        # Test 3
        try:
            cmd = f'cd "{project_root}" && start cmd /k "python professional_data_generator.py"'
            subprocess.Popen(cmd, shell=True)
            st.session_state.test3_status = 'running'
        except:
            st.session_state.test3_status = 'failed'
        
        st.success('✅ All tests launched! Check the opened windows.')
        st.rerun()

with col2:
    if st.button('🔄 Reset Test Status', use_container_width=True):
        st.session_state.test1_status = 'pending'
        st.session_state.test2_status = 'pending'
        st.session_state.test3_status = 'pending'
        st.rerun()

with col3:
    if st.button('🛑 Stop All Processes', use_container_width=True):
        try:
            # Kill Python processes related to the tests
            subprocess.run('taskkill /F /IM python.exe /FI "WINDOWTITLE eq *robust*"', shell=True, capture_output=True)
            subprocess.run('taskkill /F /IM streamlit.exe', shell=True, capture_output=True)
            st.success('Stopped all test processes')
            st.session_state.test1_status = 'pending'
            st.session_state.test2_status = 'pending'
            st.session_state.test3_status = 'pending'
        except Exception as e:
            st.warning(f'Could not stop all processes: {e}')

st.markdown("---")

# Test Summary
st.markdown("### 📊 Test Summary")
summary_cols = st.columns(3)

with summary_cols[0]:
    st.metric("Test 1: Video/Polygons", 
              st.session_state.test1_status.upper(),
              delta=None)

with summary_cols[1]:
    st.metric("Test 2: Language Switch", 
              st.session_state.test2_status.upper(),
              delta=None)

with summary_cols[2]:
    st.metric("Test 3: Dynamic Updates", 
              st.session_state.test3_status.upper(),
              delta=None)

st.markdown("---")

# Checklist
st.markdown("### ✅ Test Checklist")

test1_checks = [
    "Video opened successfully",
    "Polygon drawing interface appeared",
    "Could draw polygons by clicking",
    "Saved polygons with 'S' key"
]

test2_checks = [
    "Dashboard opened at http://localhost:8503",
    "Language selector in sidebar works",
    "No errors when switching languages",
    "UI text changes to selected language"
]

test3_checks = [
    "Data generator shows queue statistics",
    "Queue count matches number of polygons",
    "Counts update dynamically",
    "Audio announcements work every 10 seconds"
]

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Test 1 Checklist:**")
    for check in test1_checks:
        st.checkbox(check, key=f'check1_{check}')

with col2:
    st.markdown("**Test 2 Checklist:**")
    for check in test2_checks:
        st.checkbox(check, key=f'check2_{check}')

with col3:
    st.markdown("**Test 3 Checklist:**")
    for check in test3_checks:
        st.checkbox(check, key=f'check3_{check}')

st.markdown("---")
st.info('💡 **Tip:** If all tests pass, your system is working perfectly!')
