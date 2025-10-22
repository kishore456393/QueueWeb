# QueueGuidance-Web Complete Integration Guide

## 🎯 All Features Integrated!

### ✅ What's Included:

#### 1. **Video Upload & Processing** 🎥
- Upload queue videos (MP4, AVI, MOV, MKV)
- Video preview before processing
- Step-by-step workflow

#### 2. **Interactive Polygon Drawing** ✏️
- Opens external window for drawing queue zones
- Left click: Add points
- Right click: Complete polygon
- Middle click: Delete last
- S key: Save and continue
- Automatic polygon saving

#### 3. **Live Queue Detection** 🎯
- Real-time person detection using YOLO
- Queue-specific counting
- Automatic data updates every 2 seconds

#### 4. **Real-Time Dashboard** 🧠
- Auto-refreshing live view (2-second intervals)
- Current detection frame display
- Queue statistics and metrics
- Best/worst queue recommendations
- Visual bar charts
- Color-coded queue status

#### 5. **System Testing** 🧪
- Complete system test page
- Run individual or all tests
- Status tracking
- Interactive checklist

#### 6. **Analytics** 📊
- Historical data tracking
- Trend visualization
- Performance insights

## 🚀 How to Use:

### Step 1: Start the Web Application
```bash
cd QueueGuidance-Web
streamlit run frontend/app.py
```
Or visit: http://localhost:8501

### Step 2: Upload Video
1. Go to **🎥 Video Upload** page
2. Click "Choose a video file"
3. Select your queue video
4. Video preview will appear

### Step 3: Draw Queue Zones
1. Click **"✏️ Open Polygon Drawing"** button
2. A new window will open showing the first frame
3. Draw polygons around each queue area:
   - **Left click** to add points
   - **Right click** when done with one queue
   - Repeat for all queues
4. Press **"S"** key to save and close
5. Return to web page

### Step 4: Start Detection
1. Click **"🎯 Start Detection"** button
2. Detection will begin in a separate window
3. Data updates automatically

### Step 5: View Live Dashboard
1. Go to **🧠 Live Dashboard** page
2. Watch real-time updates (auto-refreshes every 2 seconds)
3. See queue counts, recommendations, and visual analytics

## 📋 Features in Detail:

### Polygon Drawing Window
- **Professional interface** with visual feedback
- **Color-coded zones** (each queue has different color)
- **Queue numbering** (Q1, Q2, Q3, etc.)
- **Semi-transparent overlays** for better visibility
- **Auto-save** after each polygon completion
- **Undo capability** (middle-click to delete last)

### Live Dashboard Features
- **Auto-refresh**: Updates every 2 seconds automatically
- **Live frame display**: See current detection in real-time
- **Queue metrics**: Total people, best queue, worst queue
- **Smart recommendations**: Tells users which queue to join
- **Visual comparisons**: Bar charts showing queue occupancy
- **Color coding**: Green (best), Red (worst), Blue (others)
- **Estimated wait times**: Based on queue length

### Detection System
- **YOLO-based** person detection (yolov8s.pt or yolov8m.pt)
- **Polygon-based** queue assignment
- **Bottom-center tracking**: Uses person's foot position
- **Confidence threshold**: 0.25 for reliable detection
- **Performance optimized**: Processes every 2nd frame
- **Continuous loop**: Video restarts automatically

## 🔧 Technical Details:

### Backend (`detection_engine.py`)
- **WebPolygonDrawer**: Interactive polygon drawing class
- **WebQueueDetector**: Real-time detection and counting
- **Point-in-polygon algorithm**: Ray casting method
- **Data persistence**: JSON format for easy access
- **Frame export**: Saves annotated frames as JPEG

### Frontend Pages
1. **app.py**: Main landing page with navigation
2. **1_🏠_Home.py**: Welcome and quick start guide
3. **2_🎥_Video_Upload.py**: Complete workflow (upload → draw → detect)
4. **3_🧠_Live_Dashboard.py**: Real-time monitoring with auto-refresh
5. **4_📊_Analytics.py**: Historical data and trends
6. **5_🧪_System_Test.py**: Comprehensive system testing

### Data Files
- **data/polygons.json**: Stores queue zone definitions
- **data/queues.json**: Current queue statistics
- **data/live_frame.jpg**: Latest detection frame
- **data/queue_data.db**: Historical analytics (SQLite)

## 🎨 Workflow Integration:

```
┌─────────────┐
│Upload Video │
└──────┬──────┘
       │
       v
┌─────────────────┐
│ Draw Polygons   │ ← Opens external window
│ (Interactive)   │   with video frame
└──────┬──────────┘
       │
       v
┌─────────────────┐
│ Save Polygons   │ ← Press 'S' key
└──────┬──────────┘
       │
       v
┌─────────────────┐
│Start Detection  │ ← Opens detection window
│  (YOLO + Counting)
└──────┬──────────┘
       │
       v
┌─────────────────┐
│ Live Dashboard  │ ← Auto-updates every 2s
│ (Real-time view)│   Shows current frame + stats
└─────────────────┘
```

## 🌟 Key Improvements:

1. **Seamless Integration**: All QueueGuidance features now accessible via web
2. **Auto-Refresh Dashboard**: No manual refresh needed
3. **Visual Feedback**: Color-coded queues, real-time charts
4. **User-Friendly**: Step-by-step guided workflow
5. **Professional UI**: Modern Streamlit design with emojis and formatting
6. **Status Tracking**: Always know what step you're on
7. **Error Handling**: Helpful error messages and warnings
8. **Flexible**: Can run polygon drawing and detection separately

## 📦 Requirements:
- All packages from QueueGuidance project
- streamlit-autorefresh (for auto-refresh feature)
- Access to QueueGuidance folder (for models and utilities)

## 🎉 Complete Feature List:

✅ Video upload and preview
✅ Interactive polygon drawing (external window)
✅ Real-time person detection (YOLO)
✅ Queue-specific counting
✅ Live dashboard with auto-refresh
✅ Visual analytics and charts
✅ Best/worst queue recommendations
✅ Estimated wait times
✅ Color-coded queue status
✅ Historical data tracking
✅ System testing interface
✅ Status indicators and progress tracking
✅ Error handling and user guidance

## 🔗 Navigation:
- **🏠 Home**: Overview and quick start
- **🎥 Video Upload**: Complete workflow (upload → draw → detect)
- **🧠 Live Dashboard**: Real-time monitoring
- **📊 Analytics**: Historical trends
- **🧪 System Test**: Run all tests

---

**All QueueGuidance features are now integrated into one unified web interface!** 🎉
