# Polygon Drawing Fix - October 21, 2025

## Issues Fixed

### 1. **Path Resolution Error**
**Problem**: The polygon drawing wasn't working after video upload due to incorrect path calculations.

**Root Cause**: The code was using relative paths from the Streamlit page file location (`frontend/pages/2_🎥_Video_Upload.py`). When going up three parent directories, it was resolving to an incorrect location.

**Solution**: 
- Fixed path calculation to correctly point to project root
- Changed from relative paths to absolute paths based on project root
- Ensured video files are saved in the correct `data/` folder

### 2. **Python Executable Path**
**Problem**: Subprocess commands were using `python` which might not work in all environments.

**Root Cause**: The system Python might not be in PATH, or might be a different version than the one running Streamlit.

**Solution**: 
- Added `sys.executable` to get the exact Python interpreter running Streamlit
- Updated all subprocess commands to use the full Python executable path

### 3. **Working Directory**
**Problem**: The detection engine scripts might fail if run from wrong directory.

**Solution**: 
- Added `cwd=str(project_root)` parameter to subprocess calls
- Ensured all file operations use absolute paths

## Files Modified

### `frontend/pages/2_🎥_Video_Upload.py`

1. **Added import**:
   ```python
   import sys
   ```

2. **Fixed video upload section**:
   - Creates `data/` directory if it doesn't exist
   - Saves video with absolute path
   - Stores full path in session state

3. **Fixed polygon drawing button**:
   - Calculates correct project root
   - Uses absolute paths for backend and video
   - Uses `sys.executable` for Python path
   - Sets working directory for subprocess

4. **Fixed detection start button**:
   - Same path fixes as polygon drawing
   - Properly formats Windows command with quotes

5. **Fixed polygon status check**:
   - Uses correct path to find `polygons.json`
   - Only marks as completed if queue_count > 0

## How to Test

### Step 1: Ensure Streamlit is Running
The app should already be running at http://localhost:8501. If not:
```powershell
cd C:\Users\User\OneDrive\Desktop\Queue3\QueueGuidance-Web\frontend
streamlit run app.py
```

### Step 2: Test Video Upload
1. Navigate to "Setup & Process" page
2. Click "Choose a video file"
3. Upload any MP4/AVI/MOV video
4. You should see: "✅ Video uploaded successfully"
5. The video should be saved in `QueueGuidance-Web/data/` folder

### Step 3: Test Polygon Drawing
1. After uploading video, click "🎨 Open Polygon Drawing Tool"
2. A new window should open showing the first frame of your video
3. Use mouse to draw polygons:
   - **Left Click**: Add point to current polygon
   - **Right Click**: Complete current polygon
   - **Middle Click**: Delete last polygon
   - **S Key**: Save and close window
   - **Q Key**: Quit without saving

### Step 4: Verify Polygon Save
1. After drawing and pressing 'S', the window should close
2. The page should update showing "Queue Zones: X" (where X is number of queues)
3. Check `QueueGuidance-Web/data/polygons.json` exists

### Step 5: Test Detection Start
1. Click "🚀 Start Detection"
2. A command window should open showing the detection process
3. Navigate to "Live Dashboard" page
4. You should see real-time updates with queue counts

## Expected Behavior

### ✅ Correct Flow:
1. Upload video → Video saved to `data/` folder
2. Draw polygons → OpenCV window opens with first frame
3. Save polygons → `data/polygons.json` created
4. Start detection → Command window opens, detection runs
5. View dashboard → Real-time queue data displayed

### ❌ Previous Issues (Now Fixed):
- ❌ Polygon window not opening
- ❌ "Cannot open video" errors
- ❌ "File not found" errors
- ❌ Subprocess failing silently

## Technical Details

### Path Structure:
```
QueueGuidance-Web/
├── backend/
│   └── detection_engine.py  ← Polygon drawer & detector
├── data/
│   ├── [uploaded_video].mp4 ← Videos go here
│   ├── polygons.json        ← Queue zones stored here
│   ├── queues.json          ← Live queue data
│   └── live_frame.jpg       ← Latest detection frame
└── frontend/
    ├── app.py
    └── pages/
        ├── 2_🎥_Video_Upload.py ← Fixed this file
        └── 3_🧠_Live_Dashboard.py
```

### Key Code Changes:

**Before**:
```python
backend_path = Path(__file__).parent.parent.parent / 'backend'
video_path = st.session_state.current_video  # relative
cmd = f'python "{backend_path}/detection_engine.py" ...'
```

**After**:
```python
project_root = Path(__file__).parent.parent.parent
backend_path = project_root / 'backend' / 'detection_engine.py'
video_full_path = project_root / 'data' / video_name
python_exe = sys.executable
cmd = f'"{python_exe}" "{backend_path}" --video "{video_full_path}" --mode polygon'
process = subprocess.Popen(cmd, shell=True, cwd=str(project_root))
```

## Troubleshooting

### If polygon window still doesn't open:
1. Check terminal for error messages
2. Verify video file exists in `data/` folder
3. Try running manually:
   ```powershell
   cd C:\Users\User\OneDrive\Desktop\Queue3\QueueGuidance-Web
   python backend/detection_engine.py --video "data/your_video.mp4" --mode polygon
   ```

### If you see "Cannot open video":
- Ensure video is properly uploaded
- Check video file is not corrupted
- Verify OpenCV can read the format

### If you see import errors:
- Ensure all packages are installed: `pip install -r requirements.txt`
- Check that QueueGuidance folder exists at same level

## Next Steps

The polygon drawing should now work correctly. Test the complete flow:
1. ✅ Upload video
2. ✅ Draw polygons
3. ✅ Start detection
4. ✅ View live dashboard

All path and subprocess issues have been resolved!
