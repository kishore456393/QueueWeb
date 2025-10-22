import streamlit as st
import json
import time
import os
import sys
import tempfile
import threading
from PIL import Image
from pathlib import Path
from streamlit_autorefresh import st_autorefresh
import plotly.graph_objects as go
import plotly.express as px

# Try to import audio system
try:
    import edge_tts
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False

try:
    import pygame
    pygame.mixer.init()
    PYGAME_AVAILABLE = True
except:
    PYGAME_AVAILABLE = False

# Page config
st.set_page_config(
    page_title='Live Dashboard',
    layout='wide',
    page_icon='📊',
    initial_sidebar_state='expanded'
)

# Custom CSS - Figma-Inspired Theme
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
        --text-primary: #F9FAFB;   /* Light Gray-50 */
        --text-secondary: #D1D5DB; /* Light Gray-300 */
        --accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --accent-primary: #667eea;
        --border: #4B5563;        /* Dark Gray-600 */
        --success: #10B981;       /* Green-500 */
        --success-light: #1F2937;  /* Gray-800 */
        --error: #F87171;         /* Red-400 */
        --error-light: #1F2937;    /* Gray-800 */
        --radius-xl: 1rem;
        --radius-lg: 0.75rem;
        --shadow-sm: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.15);
        --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.2), 0 2px 4px -1px rgba(0, 0, 0, 0.15);
        --transition-smooth: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* ===== MAIN LAYOUT ===== */
    .main {
        background-color: var(--bg-primary) !important;
    }
    
    .block-container {
        padding: 2rem 2.5rem !important;
        max-width: 1440px !important;
    }

    /* ===== SIDEBAR ===== */
    [data-testid="stSidebar"] {
        background: var(--surface) !important;
        border-right: 1px solid var(--border) !important;
        padding: 1.5rem !important;
    }
    
    [data-testid="stSidebar"] .stRadio > div {
        border-radius: var(--radius-lg);
        padding: 0.5rem;
        background-color: var(--bg-secondary);
    }

    [data-testid="stSidebar"] .stRadio [role="radiogroup"] > label {
        background: transparent;
        border-radius: var(--radius-lg);
        padding: 0.75rem 1rem;
        margin: 0.25rem 0;
        transition: var(--transition-smooth);
        font-weight: 500;
        color: var(--text-primary);
    }

    [data-testid="stSidebar"] .stRadio [role="radiogroup"] > label:hover {
        background-color: #fafbff;
    }

    [data-testid="stSidebar"] .stRadio [role="radiogroup"] > label[data-baseweb="radio"] > div:first-child {
        background: var(--accent-gradient) !important;
        border: none !important;
    }

    /* ===== DASHBOARD HEADER ===== */
    .dashboard-header {
        background: var(--surface);
        padding: 2.5rem;
        border-radius: var(--radius-xl);
        text-align: center;
        margin-bottom: 2.5rem;
        box-shadow: var(--shadow-sm);
        border: 1px solid var(--border);
    }
    
    .dashboard-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 0.5rem;
    }
    
    .dashboard-subtitle {
        font-size: 1.1rem;
        color: var(--text-secondary);
        font-weight: 500;
    }
    
    /* ===== METRIC CARDS ===== */
    .metric-card {
        background: linear-gradient(145deg, #4B5563, #374151);
        padding: 2rem;
        border-radius: var(--radius-xl);
        box-shadow: var(--shadow-md);
        text-align: center;
        border: 1px solid var(--border);
        transition: var(--transition-smooth);
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 180px; /* Ensure uniform height */
    }
    
    .metric-card:hover {
        transform: translateY(-4px);
        box-shadow: var(--shadow-md);
    }
    
    .metric-value {
        font-size: 2.75rem;
        font-weight: 700;
        color: var(--text-primary);
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        color: var(--text-secondary);
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    /* ===== QUEUE CARDS ===== */
    .queue-card {
        background: linear-gradient(135deg, rgba(75, 85, 99, 0.6), rgba(31, 41, 55, 0.6));
        padding: 1.25rem 1.5rem;
        border-radius: var(--radius-lg);
        box-shadow: var(--shadow-sm);
        margin: 0 0 1rem 0 !important;
        border: 1px solid var(--border);
        border-left: 4px solid var(--border);
        transition: var(--transition-smooth);
        display: flex !important;
        flex-direction: column;
        justify-content: space-between;
        width: 100% !important;
        min-height: 150px; /* Set a minimum height for consistency */
    }
    
    .queue-card:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
        border-left-color: var(--accent-primary);
    }
    
    .best-queue {
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.18), rgba(16, 185, 129, 0.08));
        border-color: var(--success);
        border-left: 4px solid var(--success);
    }
    
    .worst-queue {
        background: linear-gradient(135deg, rgba(248, 113, 113, 0.18), rgba(220, 38, 38, 0.08));
        border-color: var(--error);
        border-left: 4px solid var(--error);
    }
    
    .queue-title {
        font-size: 1.2rem;
        font-weight: 600;
        color: var(--text-primary) !important;
        margin-bottom: 0.5rem;
    }
    
    /* ===== SECTION TITLES ===== */
    .section-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 1.5rem;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid var(--border);
    }
    
    /* ===== BUTTONS ===== */
    .stButton>button {
        background: var(--accent-gradient) !important;
        color: white !important;
        border-radius: var(--radius-lg) !important;
        font-weight: 600 !important;
        height: 3rem !important;
        box-shadow: var(--shadow-sm);
        transition: var(--transition-smooth) !important;
        border: none;
        font-size: 1rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: var(--shadow-md);
    }
    
    /* ===== VIDEO & GRAPH CONTAINERS ===== */
    .video-container, .graph-container, .recommendation-box {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-xl);
        padding: 1.5rem;
        box-shadow: var(--shadow-sm);
        margin-bottom: 2rem;
    }

    /* ===== HIDE STREAMLIT BRANDING ===== */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'audio_enabled' not in st.session_state:
    st.session_state.audio_enabled = False
if 'selected_language' not in st.session_state:
    st.session_state.selected_language = 'en'
if 'last_announcement_time' not in st.session_state:
    st.session_state.last_announcement_time = 0
if 'audio_interval' not in st.session_state:
    st.session_state.audio_interval = 30
if 'last_refresh_time' not in st.session_state:
    st.session_state.last_refresh_time = 0

# Language options
LANGUAGES = {
    'en': '🇬🇧 English',
    'hi': '🇮🇳 Hindi (हिन्दी)',
    'ta': '🇮🇳 Tamil (தமிழ்)',
    'te': '🇮🇳 Telugu (తెలుగు)',
    'bn': '🇮🇳 Bengali (বাংলা)',
    'mr': '🇮🇳 Marathi (मराठी)',
    'gu': '🇮🇳 Gujarati (ગુજરાતી)',
    'kn': '🇮🇳 Kannada (ಕನ್ನಡ)',
    'ml': '🇮🇳 Malayalam (മലയാളം)',
    'pa': '🇮🇳 Punjabi (ਪੰਜਾਬੀ)',
    'ur': '🇮🇳 Urdu (اردو)',
    'or': '🇮🇳 Odia (ଓଡ଼ିଆ)',
    'as': '🇮🇳 Assamese (অসমীয়া)',
    'sa': '🇮🇳 Sanskrit (संस्कृतम्)'
}

# Audio templates
AUDIO_TEMPLATES = {
    "en": "Queue number {queue_num} is fastest with {people} people waiting. Wait time {minutes} minutes.",
    "hi": "क्यू नंबर {queue_num} सबसे तेज़ है, {people} लोग इंतज़ार कर रहे हैं। प्रतीक्षा समय {minutes} मिनट।",
    "ta": "வரிசை எண் {queue_num} வேகமானது, {people} பேர் காத்திருக்கின்றனர். காத்திருப்பு நேரம் {minutes} நிமிடங்கள்.",
    "te": "క్యూ నంబర్ {queue_num} వేగంగా ఉంది, {people} మంది వేచి ఉన్నారు। వేచి ఉండే సమయం {minutes} నిమిషాలు.",
    "bn": "সারি নম্বর {queue_num} সবচেয়ে দ্রুত, {people} জন অপেক্ষা করছে। অপেক্ষার সময় {minutes} মিনিট।",
    "mr": "रांग क्रमांक {queue_num} सर्वात वेगवान आहे, {people} लोक वाट पाहत आहेत। प्रतीक्षा वेळ {minutes} मिनिटे।",
    "gu": "કતાર નંબર {queue_num} સૌથી ઝડપી છે, {people} લોકો રાહ જોઈ રહ્યા છે। રાહ જોવાનો સમય {minutes} મિનિટ।",
    "kn": "ಸರತಿ ಸಂಖ್ಯೆ {queue_num} ವೇಗವಾಗಿದೆ, {people} ಜನರು ಕಾಯುತ್ತಿದ್ದಾರೆ। ಕಾಯುವ ಸಮಯ {minutes} ನಿಮಿಷಗಳು.",
    "ml": "ക്യൂ നമ്പർ {queue_num} വേഗതയേറിയതാണ്, {people} പേർ കാത്തിരിക്കുന്നു. കാത്തിരിപ്പ് സമയം {minutes} മിനിറ്റ്.",
    "pa": "ਕਤਾਰ ਨੰਬਰ {queue_num} ਸਭ ਤੋਂ ਤੇਜ਼ ਹੈ, {people} ਲੋਕ ਇਨਤਜ਼ਾਰ ਕਰ ਰਹੇ ਹਨ। ਉਡੀਕ ਦਾ ਸਮਾਂ {minutes} ਮਿੰਟ।",
    "ur": "قطار نمبر {queue_num} سب سے تیز ہے، {people} لوگ انتظار کر رہے ہیں۔ انتظار کا وقت {minutes} منٹ۔",
    "or": "ଧାଡ଼ି ନମ୍ବର {queue_num} ଦ୍ରୁତତମ, {people} ଜଣ ଅପେକ୍ଷା କରୁଛନ୍ତି। ଅପେକ୍ଷା ସମୟ {minutes} ମିନିଟ୍।",
    "as": "শাৰী নম্বৰ {queue_num} আটাইতকৈ দ্ৰুত, {people} জনে অপেক্ষা কৰিছে। অপেক্ষাৰ সময় {minutes} মিনিট।",
    "sa": "पंक्ति संख्या {queue_num} द्रुततम अस्ति, {people} जना: प्रतीक्षा कुर्वन्ति। प्रतीक्षा काल: {minutes} निमेषा:।"
}

# Edge-TTS voice mapping
EDGE_VOICES = {
    'en': 'en-US-GuyNeural',
    'hi': 'hi-IN-SwaraNeural',
    'ta': 'ta-IN-PallaviNeural',
    'te': 'te-IN-ShrutiNeural',
    'bn': 'bn-IN-TanishaaNeural',
    'mr': 'mr-IN-AarohiNeural',
    'gu': 'gu-IN-DhwaniNeural',
    'kn': 'kn-IN-SapnaNeural',
    'ml': 'ml-IN-SobhanaNeural',
    'pa': 'pa-IN-VaaniNeural',
    'ur': 'ur-IN-GulNeural',
    'or': 'or-IN-SubhasiniNeural',
    'as': 'as-IN-YashicaNeural',
    'sa': 'hi-IN-SwaraNeural'
}

# UI Translations
UI_TRANSLATIONS = {
    'en': {
        'title': 'Live Queue Dashboard',
        'subtitle': 'Real-time AI-powered queue analytics',
        'total_people': 'Total People',
        'active_queues': 'Active Queues',
        'best_queue': 'Best Queue',
        'avoid_queue': 'Avoid Queue',
        'live_view': 'Live Detection View',
        'recommendation': 'Smart Recommendation',
        'queue_details': 'Queue Details',
        'people': 'People',
        'wait_time': 'Est. Wait',
        'minutes': 'min',
        'best_choice': 'Best Choice',
        'avoid': 'Avoid',
        'normal': 'Normal',
        'queue': 'Queue'
    },
    'hi': {
        'title': 'लाइव क्यू डैशबोर्ड',
        'subtitle': 'रियल-टाइम एआई-संचालित क्यू विश्लेषण',
        'total_people': 'कुल लोग',
        'active_queues': 'सक्रिय क्यू',
        'best_queue': 'सर्वश्रेष्ठ क्यू',
        'avoid_queue': 'बचें',
        'live_view': 'लाइव डिटेक्शन व्यू',
        'recommendation': 'स्मार्ट सिफारिश',
        'queue_details': 'क्यू विवरण',
        'people': 'लोग',
        'wait_time': 'प्रतीक्षा',
        'minutes': 'मिनट',
        'best_choice': 'सर्वश्रेष्ठ विकल्प',
        'avoid': 'बचें',
        'normal': 'सामान्य',
        'queue': 'क्यू'
    },
    'ta': {
        'title': 'நேரடி வரிசை டாஷ்போர்டு',
        'subtitle': 'நேரடி AI-இயக்கப்படும் வரிசை பகுப்பாய்வு',
        'total_people': 'மொத்த மக்கள்',
        'active_queues': 'செயலில் வரிசைகள்',
        'best_queue': 'சிறந்த வரிசை',
        'avoid_queue': 'தவிர்க்க',
        'live_view': 'நேரடி காட்சி',
        'recommendation': 'பரிந்துரை',
        'queue_details': 'வரிசை விவரங்கள்',
        'people': 'மக்கள்',
        'wait_time': 'காத்திருப்பு',
        'minutes': 'நிமிடங்கள்',
        'best_choice': 'சிறந்த தேர்வு',
        'avoid': 'தவிர்க்க',
        'normal': 'சாதாரண',
        'queue': 'வரிசை'
    }
}

# Add English as fallback for other languages
for lang_code in LANGUAGES.keys():
    if lang_code not in UI_TRANSLATIONS:
        UI_TRANSLATIONS[lang_code] = UI_TRANSLATIONS['en']

# Sidebar
with st.sidebar:
    st.markdown("## 📊 Dashboard Settings")
    st.markdown("###")
    
    # Language selection
    st.markdown("### 🌐 Language")
    selected_lang = st.selectbox(
        "Select Language",
        options=list(LANGUAGES.keys()),
        format_func=lambda x: LANGUAGES[x],
        index=list(LANGUAGES.keys()).index(st.session_state.selected_language),
        key="lang_select"
    )
    if selected_lang != st.session_state.selected_language:
        st.session_state.selected_language = selected_lang
        st.rerun()
    
    # Audio toggle
    st.markdown("### 🔊 Audio Announcements")
    if AUDIO_AVAILABLE and PYGAME_AVAILABLE:
        audio_enabled = st.checkbox("Enable Audio", value=st.session_state.audio_enabled, 
                                   help="Announce best queue periodically")
        st.session_state.audio_enabled = audio_enabled
        
        if audio_enabled:
            # Audio interval slider
            audio_interval = st.slider("Announcement Interval (seconds)", 
                                      min_value=10, max_value=120, 
                                      value=st.session_state.audio_interval, 
                                      step=5,
                                      help="How often to announce the best queue",
                                      key="audio_interval_slider")
            
            # Update if changed
            if audio_interval != st.session_state.audio_interval:
                st.session_state.audio_interval = audio_interval
            
            st.info(f"🗣️ Speaking in: {LANGUAGES[st.session_state.selected_language]}")
            
            # Show time until next announcement
            current_time = time.time()
            time_since_last = current_time - st.session_state.last_announcement_time
            time_until_next = max(0, st.session_state.audio_interval - time_since_last)
            
            if st.session_state.last_announcement_time == 0:
                st.success("⏱️ **Ready for first announcement**")
            elif time_until_next <= 1:
                st.success("🔊 **Announcing...**")
            else:
                st.caption(f"⏱️ Next announcement in: **{int(time_until_next)}** seconds")
            
            # Debug info
            with st.expander("🔧 Debug Info"):
                st.caption(f"Last announced: {time_since_last:.1f}s ago")
                st.caption(f"Interval: {st.session_state.audio_interval}s")
                st.caption(f"Should announce: {time_since_last >= st.session_state.audio_interval}")
    else:
        st.warning("⚠️ Audio not available. Install: `pip install edge-tts pygame`")
    
    st.markdown("---")
    
    # Auto-refresh toggle
    st.markdown("### 🔄 Refresh Settings")
    st.markdown("")
    auto_refresh = st.toggle("🔄 Auto Refresh", value=True, help="Automatically update dashboard")
    
    if auto_refresh:
        refresh_rate = st.slider("Update Interval", 
                                min_value=1, max_value=10, value=2,
                                help="Seconds between updates",
                                key="refresh_interval_slider")
        
        # Use st_autorefresh with the selected interval
        count = st_autorefresh(interval=refresh_rate * 1000, key="datarefresh")
        
        st.markdown(f"""
        <div style='background: rgba(255,255,255,0.1); padding: 0.8rem; border-radius: 8px; font-size: 0.85rem;'>
            ⚡ Every {refresh_rate}s<br>
            📊 Refreshes: {count}
        </div>
        """, unsafe_allow_html=True)
    else:
        count = 0
        st.caption("⏸️ Manual mode")
    
    st.markdown("---")
    
    # View options
    st.markdown("### 👁️ Display Options")
    show_video = st.checkbox("📹 Live Video", value=True)
    show_metrics = st.checkbox("📊 Metrics Cards", value=True)
    show_chart = st.checkbox("📈 Analytics Chart", value=True)
    
    st.markdown("---")
    
    # Quick Navigation
    st.markdown("### 🧭 Quick Navigation")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🏠", use_container_width=True, help="Home"):
            st.switch_page("app.py")
    with col2:
        if st.button("⚙️", use_container_width=True, help="Setup"):
            st.switch_page("pages/2_🎥_Video_Upload.py")
    
    if st.button("🔄 Refresh Now", type="primary", use_container_width=True):
        st.rerun()
    
    st.markdown("---")
    st.markdown("### ℹ️ Status")
    
    data_dir = Path(__file__).parent.parent.parent / 'data'
    json_path = data_dir / 'queues.json'
    
    if json_path.exists():
        st.success("🟢 System Active")
    else:
        st.error("🔴 No Data")

# Get current language translations
lang = st.session_state.selected_language
ui_text = UI_TRANSLATIONS.get(lang, UI_TRANSLATIONS['en'])

# Dashboard Header
st.markdown(f"""
<div class="dashboard-header">
    <div class="dashboard-title">📊 {ui_text["title"]}</div>
    <div class="dashboard-subtitle">{ui_text["subtitle"]}</div>
</div>
""", unsafe_allow_html=True)

# Data paths
data_dir = Path(__file__).parent.parent.parent / 'data'
frame_path = data_dir / 'live_frame.jpg'
json_path = data_dir / 'queues.json'

# Check if data exists
if not json_path.exists():
    st.warning("⚠️ No detection data available")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.info("""
        ### 🚀 Get Started
        
        No queue data detected. To start:
        
        1. Go to **Setup & Process** page
        2. Upload a video
        3. Draw queue zones
        4. Start detection
        
        Then return here to see live analytics!
        """)
        
        if st.button("➡️ Go to Setup", type='primary', use_container_width=True):
            st.switch_page("pages/2_🎥_Video_Upload.py")
    st.stop()

# Load data
try:
    with open(json_path) as f:
        data = json.load(f)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Audio announcement function
def make_announcement_sync(queue_num, people_count, wait_minutes, language):
    """Generate and play audio announcement synchronously"""
    try:
        import asyncio
        
        template = AUDIO_TEMPLATES.get(language, AUDIO_TEMPLATES['en'])
        text = template.format(queue_num=queue_num, people=people_count, minutes=wait_minutes)
        voice = EDGE_VOICES.get(language, EDGE_VOICES['en'])
        
        # Generate audio file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
            tmp_path = tmp_file.name
        
        # Run edge-tts in sync mode
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
        async def generate_audio():
            communicate = edge_tts.Communicate(text, voice)
            await communicate.save(tmp_path)
        
        loop.run_until_complete(generate_audio())
        loop.close()
        
        # Play audio
        if PYGAME_AVAILABLE and os.path.exists(tmp_path):
            pygame.mixer.music.load(tmp_path)
            pygame.mixer.music.play()
            
            # Wait for audio to finish
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
        
        # Cleanup
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        
        return True
    except Exception as e:
        print(f"Audio error: {e}")
        return False

def play_announcement_thread(queue_num, people_count, wait_minutes, language):
    """Thread wrapper for audio announcement"""
    try:
        make_announcement_sync(queue_num, people_count, wait_minutes, language)
    except Exception as e:
        print(f"Thread error: {e}")

# Make audio announcement if enabled
if st.session_state.audio_enabled and AUDIO_AVAILABLE and PYGAME_AVAILABLE:
    current_time = time.time()
    announcement_interval = st.session_state.audio_interval
    time_since_last = current_time - st.session_state.last_announcement_time
    
    # Simple check: has enough time passed?
    if time_since_last >= announcement_interval:
        best_queue = data.get('best_queue', 1)
        queue_counts = data.get('queue_counts', [])
        
        if queue_counts and best_queue <= len(queue_counts):
            people = queue_counts[best_queue - 1]
            wait_time = people * 2
            
            # Update timestamp BEFORE starting thread to prevent multiple triggers
            st.session_state.last_announcement_time = current_time
            
            # Start announcement in separate thread (non-blocking)
            announcement_thread = threading.Thread(
                target=play_announcement_thread,
                args=(best_queue, people, wait_time, st.session_state.selected_language),
                daemon=True
            )
            announcement_thread.start()

# Main metrics at top
if show_metrics:
    st.markdown('<div class="section-header"><h2 class="section-title">📊 Real-Time Metrics</h2></div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4, gap="large")
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">👥 {ui_text['total_people']}</div>
            <div class="metric-value">{data.get('total_people', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🎯 {ui_text['active_queues']}</div>
            <div class="metric-value">{data.get('total_queues', 0)}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        best_q = data.get('best_queue', 1)
        st.markdown(f"""
        <div class="metric-card" style="border-top: 4px solid #10b981;">
            <div class="metric-label">✅ {ui_text['best_queue']}</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #10b981 0%, #059669 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">#{best_q}</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        worst_q = data.get('worst_queue', 1)
        st.markdown(f"""
        <div class="metric-card" style="border-top: 4px solid #ef4444;">
            <div class="metric-label">⚠️ {ui_text['avoid_queue']}</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">#{worst_q}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("###")

# Main content area
col1, col2 = st.columns([3, 2])

with col1:
    if show_video:
        st.markdown('<div class="section-header"><h2 class="section-title">📹 Live Video Feed</h2></div>', unsafe_allow_html=True)
        if frame_path.exists():
            st.markdown('<div class="video-container">', unsafe_allow_html=True)
            st.image(str(frame_path), use_column_width=True)
            
            # Add timestamp below video with Figma styling
            timestamp = data.get('timestamp', '')
            if timestamp:
                try:
                    time_str = timestamp.split('T')[1].split('.')[0]
                    date_str = timestamp.split('T')[0]
                    st.markdown(f"""
                    <div style='text-align: center; padding: 12px; margin-top: 12px;
                                background: var(--accent-light); border-radius: var(--radius-md);
                                border: 1px solid var(--accent-primary);'>
                        <span style='color: var(--accent-primary); font-size: 14px; font-weight: 600;'>
                            🕒 {time_str} &nbsp;|&nbsp; 📅 {date_str}
                        </span>
                    </div>
                    """, unsafe_allow_html=True)
                except:
                    pass
            
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.warning('⚠️ No live frame available')

with col2:
    st.markdown('<div class="section-header"><h2 class="section-title">🎯 Smart Recommendations</h2></div>', unsafe_allow_html=True)
    
    queue_counts = data.get('queue_counts', [])
    best_q = data.get('best_queue', 1)
    
    # Recommendation box
    recommendation = data.get('recommendation', 'Processing...')
    st.markdown(f"""
    <div style='background: linear-gradient(135deg, rgba(16, 185, 129, 0.2) 0%, rgba(16, 185, 129, 0.05) 100%); 
                backdrop-filter: blur(10px);
                padding: 2rem; border-radius: 16px; 
                box-shadow: 0 8px 30px rgba(16, 185, 129, 0.4);
                border: 1px solid rgba(16, 185, 129, 0.4);
                margin-bottom: 1.5rem;
                position: relative;
                overflow: hidden;'>
        <div style='position: absolute; top: -50%; right: -50%; width: 200%; height: 200%;
                    background: radial-gradient(circle, rgba(16, 185, 129, 0.1) 0%, transparent 70%);'></div>
        <div style='font-size: 1.2rem; font-weight: 700; color: #10b981; margin-bottom: 0.8rem; position: relative; z-index: 1;'>
            ✅ Smart Recommendation
        </div>
        <div style='font-size: 1.1rem; color: #e0f2fe; font-weight: 600; position: relative; z-index: 1;'>
            {recommendation}
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("###")
    
    # Queue details
    st.markdown("""
    <div style='background: rgba(30, 41, 59, 0.5); backdrop-filter: blur(10px);
                padding: 1rem 1.8rem; border-radius: 14px; 
                box-shadow: 0 4px 20px rgba(0,0,0,0.4);
                border: 1px solid rgba(99, 102, 241, 0.3);
                margin-bottom: 1rem;'>
        <h3 style='color: #f1f5f9; margin: 0.5rem 0; font-size: 1.4rem; font-weight: 700;'>📋 Queue Analysis</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for i, count in enumerate(queue_counts):
        queue_num = i + 1
        wait_time = count * 2  # Estimate
        
        if queue_num == best_q:
            status = f"✅ {ui_text['best_choice']}"
            card_class = "queue-card best-queue"
        elif count == max(queue_counts):
            status = f"⚠️ {ui_text['avoid']}"
            card_class = "queue-card worst-queue"
        else:
            status = f"⚪ {ui_text['normal']}"
            card_class = "queue-card"
        
        # Each queue card in its own container with clear separation
        st.markdown(f"""
        <div class="{card_class}" style="margin-bottom: 1.5rem; display: block; width: 100%; clear: both;">
            <div class="queue-title" style="clear: both;">
                {ui_text['queue']} {queue_num}
                <span style="float: right; font-size: 1rem; font-weight: 600; color: #cbd5e1;">{status}</span>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; margin-top: 1rem; clear: both;">
                <div style="font-size: 1rem; color: #94a3b8;">
                    👥 <strong style="color: #f1f5f9;">{count}</strong> {ui_text['people']}
                </div>
                <div style="font-size: 1rem; color: #94a3b8;">
                    ⏱️ <strong style="color: #f1f5f9;">~{wait_time}</strong> {ui_text['minutes']}
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
# Visualization Chart
st.markdown("###")
if show_chart:
    st.markdown('<div class="section-header"><h2 class="section-title">📈 Queue Comparison Chart</h2></div>', unsafe_allow_html=True)
    
    queue_counts = data.get('queue_counts', [])
    
    if len(queue_counts) > 0:
        # Figma-style graph container
        st.markdown('<div class="graph-container">', unsafe_allow_html=True)
        
        fig = go.Figure()
        
        # Figma-style minimal colors
        colors = ['#00c853' if c == min(queue_counts) else '#ff3b30' if c == max(queue_counts) else '#5551ff' 
                 for c in queue_counts]
        
        fig.add_trace(go.Bar(
            x=[f"Queue {i+1}" for i in range(len(queue_counts))],
            y=queue_counts,
            marker=dict(
                color=colors,
                line=dict(color='#ffffff', width=0),
                opacity=1
            ),
            text=queue_counts,
            textposition='outside',
            textfont=dict(size=16, color='#e5e7eb', family='Inter', weight=600),
            hovertemplate='<b>%{x}</b><br>People: <b>%{y}</b><br>Est. Wait: <b>~%{y:.0f} min</b><extra></extra>',
        ))
        
        fig.update_layout(
            title={
                'text': '<b>Queue Occupancy</b>', 
                'x': 0,
                'xanchor': 'left',
                'font': {'size': 20, 'color': '#e5e7eb', 'family': 'Inter'}
            },
            xaxis=dict(
                title=None,
                tickfont=dict(size=13, color='#cbd5e1', family='Inter'),
                gridcolor='transparent',
                showgrid=False,
                linecolor="#4b5563",
                linewidth=1,
                showline=True
            ),
            yaxis=dict(
                title=dict(
                    text='People',
                    font=dict(size=13, color='#cbd5e1', family='Inter')
                ),
                tickfont=dict(size=12, color='#cbd5e1', family='Inter'),
                gridcolor="#374151",
                showgrid=True,
                linecolor="#4b5563",
                linewidth=1,
                showline=True,
                zeroline=True,
                zerolinecolor="#4b5563",
                zerolinewidth=1
            ),
            height=400,
            showlegend=False,
            margin=dict(l=60, r=40, t=60, b=40),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(family='Inter', size=13, color='#e5e7eb'),
            hovermode='x unified',
            hoverlabel=dict(
                bgcolor='#111827',
                font_size=13,
                font_family='Inter',
                font_color='#ffffff',
                bordercolor='transparent'
            ),
            bargap=0.3
        )
        
        st.plotly_chart(fig, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("📊 No queue data available for chart")
