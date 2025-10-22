# QueueGuidance-Web

A web-based intelligent queue management system built with Streamlit.

## Features
- 🎥 Video Upload & Processing
- 🧠 Real-time Queue Analysis
- 📊 Analytics Dashboard
- 🔊 Multi-language Audio Announcements

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
streamlit run frontend/app.py
```

Or use the helper script:
```bash
python run.py
```

## Project Structure
```
QueueGuidance-Web/
├── frontend/          # Streamlit UI
│   ├── app.py        # Main app
│   ├── pages/        # Page modules
│   └── assets/       # Static files
├── backend/          # Detection engine
├── data/            # Videos, frames, DB
├── models/          # YOLO models
└── requirements.txt
```

## Usage
1. Navigate to **Video Upload** page
2. Upload your queue video
3. Click **Run Detection**
4. View results in **Live Dashboard**
5. Check historical data in **Analytics**
