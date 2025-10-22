# 🎨 Queue Guidance Web - Figma-Inspired Design Specification

## 📐 Design System Overview

This document outlines the design system for the Queue Guidance web application, inspired by a clean, modern, and professional aesthetic similar to Figma's user interface.

---

## 🎯 Design Philosophy
- **Clean & Minimal**: A clutter-free interface that prioritizes content and functionality.
- **Professional**: A corporate-grade UI suitable for business and analytics environments.
- **Gradient Accents**: Use of subtle gradients to add a touch of modernism and visual interest.
- **Clarity & Consistency**: Systematic use of spacing, colors, and typography for a predictable and easy-to-navigate user experience.

---

## 🌈 Color Palette (Design Tokens)

### Background Colors
```
--bg-primary: #f8f9fd (Light lavender-white for main background)
--bg-secondary: #eef2ff (Lighter purple-blue for gradient end)
--surface: #ffffff (Pure White - for cards, sidebar, and main content areas)
```

### Text Colors
```
--text-primary: #1a202c (Almost black for headings and primary text)
--text-secondary: #718096 (Cool gray for body text, descriptions, and subtitles)
```

### Accent Colors
```
--accent-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%) (Primary gradient for active states and highlights)
--accent-primary: #667eea (The start color of the gradient, used for highlights)
```

### Border Color
```
--border: #e2e8f0 (Light gray for borders and dividers)
```

### Status Colors
```
--success: #00c853 (Green for success states, e.g., 'Best Queue')
--success-light: #e8f5e9 (Light green background for success highlights)
--error: #ff3b30 (Red for warning states, e.g., 'Avoid Queue')
--error-light: #ffebee (Light red background for error highlights)
```

---

## ✒️ Typography

- **Font Family**: 'Inter', sans-serif. A clean, readable, and modern sans-serif font.
- **Import URL**: `https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap`

### Font Weights
- **Normal**: 400
- **Medium**: 500 (Used for sidebar navigation)
- **Semi-Bold**: 600 (Used for card titles and section headers)
- **Bold**: 700 (Used for main titles and large metric values)

---

## 📏 Spacing & Sizing

### Radii (Border Radius)
```
--radius-xl: 1rem (16px) - For large containers like headers and main cards.
--radius-lg: 0.75rem (12px) - For smaller cards and sidebar navigation items.
```

### Layout
- **Sidebar Width**: `280px`
- **Max Container Width**: `1440px`
- **Standard Padding**: `2rem 2.5rem` (32px top/bottom, 40px left/right)

---

## 🧩 Component Styles

### Sidebar
- **Background**: `var(--surface)`
- **Border**: `1px solid var(--border)` on the right.
- **Navigation**: Uses `st.radio` styled as individual buttons.
  - **Default State**: Transparent background, `var(--text-primary)` color.
  - **Hover State**: Light blue-gray background (`#fafbff`).
  - **Active State**: `var(--accent-gradient)` background, white text.

### Main Header (`.main-header`, `.page-header`, `.dashboard-header`)
- **Background**: `var(--surface)`
- **Padding**: `2rem` or `2.5rem`
- **Border**: `1px solid var(--border)`
- **Border Radius**: `var(--radius-xl)`
- **Shadow**: `var(--shadow-sm)`

### Cards (`.feature-card`, `.metric-card`, `.queue-card`, `.step-container`)
- **Background**: `var(--surface)`
- **Border**: `1px solid var(--border)`
- **Border Radius**: `var(--radius-xl)` or `var(--radius-lg)`
- **Shadow**: `var(--shadow-sm)`
- **Hover Effect**: `transform: translateY(-2px)` or `translateY(-4px)`, `box-shadow: var(--shadow-md)`.

### Buttons (`.stButton > button`)
- **Primary Button**: `var(--accent-gradient)` background, white text.
- **Secondary/Default Button**: `var(--surface)` background, `var(--text-primary)` text, `1px solid var(--border)`.
- **Hover (Secondary)**: Border color `var(--accent-primary)`, text color `var(--accent-primary)`.

### Status-Specific Cards (`.best-queue`, `.worst-queue`)
- **Best Queue**: `var(--success-light)` background, with a `4px` solid left border of `var(--success)`.
- **Worst Queue**: `var(--error-light)` background, with a `4px` solid left border of `var(--error)`.

---

## 📄 Page-Specific Implementations

### `app.py` (Home Page)
- Uses `.main-header` for the title section.
- Features are displayed in `.feature-card` components.
- The "Quick Start Guide" is within an `st.expander` styled to match the card aesthetic.

### `2_🎥_Video_Upload.py` (Setup Page)
- Uses `.page-header`.
- Each step is encapsulated in a `.step-container`.
- Step numbers are styled with a circular gradient background (`.step-number`).
- Metrics are shown in `.metric-card` elements.

### `3_🧠_Live_Dashboard.py` (Dashboard Page)
- Uses `.dashboard-header`.
- Key statistics (Total People, Best Queue, etc.) are in `.metric-card`s.
- Individual queue details are shown in `.queue-card`s, with conditional classes `.best-queue` and `.worst-queue`.
- The live video and graph are in `.video-container` and `.graph-container` respectively, which share the same card styling.
- Section titles (`.section-title`) have a bottom border to create clear visual separation.

---

## 🎬 Animation & Transitions

### Standard Transitions
```
All interactive elements:
transition: all 0.2s ease

Hover effects:
- Cards: translateY(-2px) or translateX(4px)
- Buttons: translateY(-1px)
- Duration: 0.2s
- Easing: ease or cubic-bezier(0.4, 0, 0.2, 1)
```

### No Heavy Animations
- No spinning loaders (use subtle pulse)
- No sliding panels (instant show/hide)
- No fade-ins longer than 200ms
- Keep it snappy and professional

---

## 📱 Responsive Breakpoints

```
Mobile: < 768px
Tablet: 768px - 1024px
Desktop: 1024px - 1440px
Large Desktop: > 1440px
```

### Responsive Adjustments:

**Mobile (< 768px)**:
- Sidebar: Collapse to hamburger menu
- Columns: Stack vertically (1 column)
- Padding: Reduce to 16px
- Font sizes: Reduce by 10-15%
- Container padding: 16px 20px

**Tablet (768px - 1024px)**:
- Sidebar: 240px width
- Columns: 2 columns max
- Padding: 24px 32px

**Desktop (> 1024px)**:
- Full layout as specified
- Max-width: 1440px centered

---

## 🎨 Figma Design Tips

### 1. **Set up Design Tokens First**
- Create color styles for all colors
- Create text styles for all typography
- Create effect styles for shadows

### 2. **Use Auto Layout**
- Set all components to use auto layout
- Define spacing using padding tokens
- Use gap property for consistent spacing

### 3. **Create Components**
- Button (Primary, Secondary variants)
- Card (Default, Best, Worst variants)
- Alert (Info, Success, Warning, Error variants)
- Form elements (Input, Select, Checkbox)

### 4. **Use Constraints**
- Cards: Left & Right constraints
- Sidebar: Fixed width, left constraint
- Main content: Center constraint with max-width

### 5. **Typography Hierarchy**
```
H1: 32px / Bold / -0.5px
H2: 20px / Semibold / -0.3px
H3: 18px / Semibold / -0.2px
Body: 14px / Regular / 0px
Caption: 13px / Medium / 0.5px (uppercase)
Large Number: 40px / Bold / -1px
```

---

## 📊 Page Layouts

### Dashboard Page Layout
```
┌─────────────────────────────────────────────┐
│  Sidebar (280px)  │  Main Content          │
│                   │                         │
│  • Settings       │  Dashboard Header       │
│  • Language       │                         │
│  • Audio          │  [Metric Cards Row]     │
│  • Navigation     │  [4 cards × 1 row]      │
│                   │                         │
│                   │  Content Grid (3:2)     │
│                   │  ┌───────┬──────────┐   │
│                   │  │ Video │ Queue    │   │
│                   │  │       │ Cards    │   │
│                   │  │       │          │   │
│                   │  └───────┴──────────┘   │
│                   │                         │
│                   │  Graph Section          │
│                   │  [Full width chart]     │
│                   │                         │
└─────────────────────────────────────────────┘
```

### Metric Cards Row
```
┌──────────┬──────────┬──────────┬──────────┐
│  Total   │  Active  │   Best   │  Refresh │
│  People  │  Queues  │  Queue   │  Time    │
│          │          │          │          │
│   [42]   │   [5]    │  [Q-2]   │  [5 sec] │
│          │          │          │          │
└──────────┴──────────┴──────────┴──────────┘
```

### Queue Cards Layout
```
┌────────────────────────┐
│ Queue 1      👥 8      │  ← Normal
│ Normal       ⏱️ ~8 min │
└────────────────────────┘

┌────────────────────────┐
│ Queue 2      👥 3      │  ← Best (Green background)
│ ✅ Best      ⏱️ ~3 min │
└────────────────────────┘

┌────────────────────────┐
│ Queue 3      👥 15     │  ← Worst (Red background)
│ ⚠️ Avoid     ⏱️ ~15min │
└────────────────────────┘
```

---

## 🎯 Key Design Principles

### 1. **Consistency**
- Use the same spacing everywhere
- Same border-radius for similar elements
- Consistent hover states
- Same shadow for same elevation

### 2. **Hierarchy**
- Size matters: Larger = more important
- Color matters: Darker = more important
- Weight matters: Bolder = more important
- Position matters: Top/left = more important

### 3. **Whitespace**
- Don't fear empty space
- Minimum 16px between sections
- Padding inside cards: 20-24px
- Margin between cards: 12px

### 4. **Alignment**
- Everything aligns to a grid
- Text left-aligns (except centered headers)
- Buttons align to container edges
- Icons align with text baseline

### 5. **Accessibility**
- Minimum contrast ratio: 4.5:1 for text
- Touch targets: Minimum 44px × 44px
- Focus indicators: 3px outline
- Color is not the only indicator

---

## 🔧 Implementation Notes

### CSS Class Names (for reference)
```
.dashboard-header
.metric-card
.queue-card
.best-queue
.worst-queue
.section-header
.video-container
.graph-container
```

### State Classes
```
:hover
:focus
:active
:disabled
.is-loading
.is-selected
```

---

## 📝 Content Examples

### Typical Data Values
- Queue counts: 0-50 people
- Wait times: 0-50 minutes
- Queue numbers: 1-10
- Timestamps: HH:MM:SS format
- Dates: YYYY-MM-DD format

### UI Text
- "Total People in All Queues"
- "Active Queue Zones"
- "Best Queue Recommendation"
- "Live Video Feed"
- "Queue Comparison Chart"
- "Smart Recommendation"
- "Real-time Monitoring & Analytics"

---

## 🎨 Export Settings for Figma

### For Development Handoff:
1. **Images**: Export as PNG @2x
2. **Icons**: Export as SVG
3. **Spacing**: Show in pixels
4. **Colors**: Show in HEX
5. **Fonts**: Specify Inter font family
6. **Shadows**: Export CSS shadow values

### Component States to Design:
- [ ] Default
- [ ] Hover
- [ ] Active/Selected
- [ ] Disabled
- [ ] Loading
- [ ] Error
- [ ] Empty state

---

## ✅ Design Checklist

When creating in Figma, ensure:
- [ ] All colors use defined color styles
- [ ] All text uses defined text styles
- [ ] All shadows use defined effect styles
- [ ] Components are created for reusable elements
- [ ] Auto layout is used for responsive behavior
- [ ] Constraints are set for all elements
- [ ] Spacing follows the spacing scale
- [ ] Border radius follows the radius scale
- [ ] All interactive elements have hover states
- [ ] Accessibility standards are met
- [ ] Mobile responsive layouts are designed

---

## 🚀 Quick Start Guide

1. **Create a new Figma file**
2. **Set up your styles** (colors, typography, effects)
3. **Create your grid** (12 columns, 24px gutter)
4. **Build the sidebar** (280px frame)
5. **Create component library** (buttons, cards, etc.)
6. **Design the dashboard layout** (1440px max-width)
7. **Add content and data**
8. **Create responsive variants**
9. **Add interactions** (hover states, etc.)
10. **Export for development**

---

## 📞 Support

If you need clarification on any design element:
- Color values are in HEX format (#rrggbb)
- Spacing values are in pixels (px)
- Font sizes are in pixels (px)
- Shadows are in CSS format
- All measurements are precise

---

## 🔘 Sidebar Navigation - Complete Functionality Guide

### Overview
The sidebar contains 6 main navigation buttons that control the entire application flow. Each button has specific functions and operations.

---

### 1️⃣ **HOME Button** (🏠)

**Primary Function**: Landing page and system overview

**What it does**:
- Displays welcome screen with project introduction
- Shows system status (Active/Inactive)
- Provides quick access cards to main features
- Displays recent activity summary
- Shows total queue statistics overview

**Operations**:
1. **Load Homepage**: Renders the main landing page
2. **Show Quick Stats**: Displays total people, active queues, system status
3. **Navigation Hub**: Provides buttons to navigate to Upload Video and Live Dashboard
4. **Feature Showcase**: Shows what the system can do with icons and descriptions
5. **System Health Check**: Indicates if detection is running or stopped

**User Actions Available**:
- Click "Start Monitoring" → Goes to Upload Video page
- Click "View Dashboard" → Goes to Live Dashboard
- See system capabilities (Real-time detection, AI analysis, Multi-queue support)
- Read project description and features

**Data Displayed**:
- Project title and subtitle
- Feature cards (Real-time Detection, Smart Analytics, Multi-Queue Support)
- Quick action buttons
- System status indicator

---

### 2️⃣ **UPLOAD VIDEO Button** (🎥 Video Upload)

**Primary Function**: Video upload and queue zone configuration

**What it does**:
- Allows users to upload surveillance video files
- Provides interface to draw queue zones on video frame
- Configures detection parameters
- Starts the YOLO detection engine
- Processes video and saves queue data

**Operations**:
1. **Video Upload**:
   - Accept video files (.mp4, .avi, .mov, etc.)
   - Display video file information (name, size, duration)
   - Show upload progress bar
   - Validate video format

2. **Frame Extraction**:
   - Extract first frame from uploaded video
   - Display frame for zone definition
   - Allow users to see what camera is capturing

3. **Queue Zone Definition**:
   - Provide drawing tool to define rectangular zones
   - Label each zone (Queue 1, Queue 2, etc.)
   - Show zone coordinates
   - Allow editing/deleting zones
   - Minimum: Define at least 1 queue zone
   - Maximum: Support up to 10 queue zones

4. **Configuration Settings**:
   - Set confidence threshold (default: 0.5)
   - Set IoU threshold (default: 0.45)
   - Choose detection model (YOLOv8n, YOLOv8s, etc.)
   - Set frame processing rate

5. **Start Detection**:
   - Save queue zone coordinates to JSON
   - Launch detection_engine.py in background
   - Run headless (no video window popup)
   - Process video frame by frame
   - Count people in each queue zone
   - Generate live_frame.jpg continuously
   - Update queues.json in real-time

6. **Progress Tracking**:
   - Show current processing status
   - Display progress percentage
   - Show frames processed / total frames
   - Estimated time remaining

**User Actions Available**:
- Upload new video file
- Draw queue zones by clicking corners
- Adjust zone boundaries
- Delete zones
- Start detection process
- Stop detection process
- Navigate to Live Dashboard to see results

**Data Generated**:
- Saved video file location
- Queue zone coordinates (x1, y1, x2, y2)
- Zone labels (Queue 1, Queue 2, etc.)
- Detection parameters
- queues.json (updated continuously)
- live_frame.jpg (updated every frame)

---

### 3️⃣ **LIVE DASHBOARD Button** (🧠 Live Dashboard)

**Primary Function**: Real-time queue monitoring and analytics

**What it does**:
- Displays live video feed with detection boxes
- Shows real-time people count in each queue
- Provides smart queue recommendations
- Displays analytics charts
- Supports audio announcements
- Multi-language interface

**Operations**:

**1. Real-Time Video Display**:
- Load live_frame.jpg every 5 seconds (auto-refresh)
- Show detection bounding boxes around people
- Display queue zone boundaries
- Show timestamp of last frame update
- Render video with proper aspect ratio

**2. Metric Cards Display**:
- **Total People**: Sum of all people across all queues
- **Active Queues**: Number of queues currently being monitored
- **Best Queue**: Queue with lowest count (recommended)
- **Refresh Rate**: How often data updates (5 seconds default)

**3. Queue Status Cards**:
- Display each queue as individual card
- Show queue number/name
- Display people count with icon (👥)
- Calculate wait time (~1 min per person)
- Color coding:
  * **Green background**: Best queue (lowest count)
  * **Red background**: Worst queue (highest count)
  * **White background**: Normal queues
- Status labels: "✅ Best Choice" or "⚠️ Avoid" or "Normal"

**4. Smart Recommendation**:
- Analyze all queue counts
- Identify queue with minimum people
- Display recommendation alert
- Show in prominent accent color (#5551ff)
- Update recommendation when counts change

**5. Analytics Chart**:
- Bar chart showing all queue occupancy
- X-axis: Queue numbers (Queue 1, Queue 2, etc.)
- Y-axis: Number of people
- Color bars:
  * Green: Best queue
  * Red: Worst queue
  * Purple: Normal queues
- Interactive hover tooltips
- Shows estimated wait time per queue

**6. Audio Announcements**:
- Text-to-speech using edge-tts
- Announce best queue periodically
- Support for 14 languages:
  * English, Hindi, Tamil, Telugu, Bengali
  * Marathi, Gujarati, Kannada, Malayalam
  * Punjabi, Urdu, Odia, Assamese, Sanskrit
- Configurable announcement interval (10-120 seconds)
- Toggle on/off functionality
- Example: "Queue 2 is the best choice with 3 people waiting"

**7. Language Selection**:
- Dropdown with 14 language options
- Changes all UI text instantly
- Affects audio announcements
- Saves language preference in session

**8. Sidebar Controls**:
- **Home Button** (🏠): Return to homepage
- **Setup Button** (⚙️): Go back to video upload
- **Refresh Now**: Manual data refresh
- **Language Selector**: Change interface language
- **Audio Toggle**: Enable/disable announcements
- **Audio Interval Slider**: Set announcement frequency
- **System Status**: Shows if data is available

**User Actions Available**:
- View live video feed
- Monitor queue counts in real-time
- Read smart recommendations
- Check analytics chart
- Enable audio announcements
- Change language
- Adjust announcement interval
- Navigate to other pages
- Manually refresh data

**Data Displayed**:
- Live video frame with detections
- Total people count across all queues
- Individual queue counts
- Best queue recommendation
- Worst queue warning
- Wait time estimates
- Timestamp of last update
- Bar chart visualization
- System status (Active/No Data)

---

### 4️⃣ **ANALYTICS Button** (📊 Analytics)

**Primary Function**: Historical data analysis and insights

**What it does**:
- Shows queue trends over time
- Displays peak hours analysis
- Provides queue utilization statistics
- Generates comparison reports
- Exports data for further analysis

**Operations**:

**1. Historical Data Display**:
- Load queues.json history (if stored)
- Show queue counts over past hour/day/week
- Line charts showing trends
- Time-series data visualization

**2. Peak Hours Analysis**:
- Identify busiest times of day
- Show average queue length per hour
- Highlight peak congestion periods
- Compare weekdays vs weekends

**3. Queue Performance Metrics**:
- Average people per queue
- Maximum capacity reached
- Minimum occupancy times
- Queue efficiency score (how evenly distributed)

**4. Comparison Reports**:
- Compare queue performance
- Best performing queue (most balanced)
- Worst performing queue (most congested)
- Recommendation for queue optimization

**5. Data Export**:
- Export queue data to CSV
- Download charts as PNG
- Generate PDF reports
- Share analytics via email

**6. Filters and Controls**:
- Date range selector
- Queue filter (select specific queues)
- Time interval (hourly, daily, weekly)
- Chart type selector (line, bar, pie)

**User Actions Available**:
- View historical trends
- Filter by date range
- Select specific queues to analyze
- Export data in various formats
- Download reports
- Compare queue performance

**Data Displayed**:
- Historical queue counts
- Trend lines and patterns
- Peak/off-peak hours
- Average wait times
- Queue efficiency metrics
- Occupancy heatmaps

---

### 5️⃣ **SYSTEM Button** (⚙️ Settings/System)

**Primary Function**: System configuration and settings management

**What it does**:
- Configure detection parameters
- Manage system preferences
- Control video processing settings
- Set up notifications
- Manage user preferences

**Operations**:

**1. Detection Settings**:
- **Confidence Threshold**: Adjust detection sensitivity (0.1 - 1.0)
- **IoU Threshold**: Set overlap threshold for detections (0.1 - 1.0)
- **Model Selection**: Choose YOLO model (YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l)
- **Frame Skip**: Process every Nth frame (for performance)
- **Max Detections**: Limit maximum people detected per frame

**2. Video Processing Settings**:
- **Resolution**: Set processing resolution (480p, 720p, 1080p)
- **FPS**: Target frames per second
- **Codec**: Video codec selection
- **Quality**: Processing quality (Low, Medium, High)

**3. Refresh Settings**:
- **Auto-refresh interval**: Set dashboard update frequency (1-60 seconds)
- **Frame update rate**: How often to save live_frame.jpg
- **JSON update rate**: How often to update queues.json

**4. Audio Settings**:
- **Default Language**: Set default announcement language
- **Voice Gender**: Male/Female voice (if available)
- **Speech Rate**: Slow/Normal/Fast
- **Volume**: Set announcement volume (0-100%)
- **Default Interval**: Set default announcement frequency

**5. Notification Settings**:
- **Email Notifications**: Send alerts when queue exceeds threshold
- **SMS Notifications**: Text message alerts
- **Threshold Alerts**: Set maximum queue length before alert
- **Admin Email**: Configure recipient email

**6. Display Settings**:
- **Theme**: Light/Dark mode (if implemented)
- **Default Page**: Set which page loads on startup
- **Show Video**: Toggle video feed on dashboard
- **Show Chart**: Toggle analytics chart display

**7. System Information**:
- **Software Version**: Current application version
- **Python Version**: Python interpreter version
- **YOLO Model**: Currently loaded model
- **GPU Status**: CUDA availability (if GPU present)
- **Memory Usage**: System resource usage
- **Detection FPS**: Current processing speed

**8. Data Management**:
- **Clear Cache**: Remove old video frames
- **Reset Zones**: Clear all queue zone definitions
- **Export Configuration**: Save settings to file
- **Import Configuration**: Load settings from file
- **Backup Data**: Create backup of queues.json

**User Actions Available**:
- Adjust detection parameters
- Change video processing settings
- Configure auto-refresh rates
- Set up audio preferences
- Enable/disable notifications
- View system information
- Manage data and cache
- Export/import configurations

**Data Displayed**:
- Current configuration values
- System resource usage
- Model information
- Processing statistics
- Storage usage
- Version information

---

### 6️⃣ **TEST Button** (🧪 Test/Debug)

**Primary Function**: System testing and debugging tools

**What it does**:
- Test detection accuracy
- Verify queue zone definitions
- Check system components
- Simulate different scenarios
- Debug issues

**Operations**:

**1. Detection Test**:
- **Upload Test Image**: Test detection on single image
- **Test Video Clip**: Test on short video segment
- **Show Detection Boxes**: Visualize bounding boxes
- **Confidence Display**: Show detection confidence scores
- **Performance Metrics**: FPS, processing time, accuracy

**2. Queue Zone Verification**:
- **Preview Zones**: Overlay zones on video frame
- **Test Zone Accuracy**: Check if people are counted correctly
- **Adjust Zones**: Fine-tune zone boundaries
- **Zone Overlap Check**: Ensure zones don't overlap improperly

**3. System Component Test**:
- **Camera Connection**: Test if video source is accessible
- **YOLO Model**: Verify model loads correctly
- **JSON Writer**: Test data file writing
- **Audio System**: Test TTS functionality
- **Database**: Check data storage (if used)

**4. Simulation Mode**:
- **Mock Data**: Generate fake queue counts for testing
- **Load Test**: Simulate high traffic scenarios
- **Stress Test**: Test system under load
- **Random Data**: Create random queue scenarios

**5. Debugging Tools**:
- **View Logs**: Display system logs
- **Error Messages**: Show recent errors
- **Stack Traces**: Debug information for crashes
- **Console Output**: Real-time console messages

**6. Performance Profiling**:
- **FPS Counter**: Real-time frames per second
- **CPU Usage**: Processor utilization
- **Memory Usage**: RAM consumption
- **GPU Usage**: Graphics card utilization (if available)
- **Latency**: Detection delay measurements

**7. Data Validation**:
- **Check JSON Format**: Verify queues.json structure
- **Validate Coordinates**: Ensure zone coordinates are valid
- **Count Verification**: Compare manual vs automatic counts
- **Timestamp Check**: Verify time data accuracy

**8. Export Test Results**:
- **Save Test Report**: Export test results to file
- **Screenshot Tool**: Capture current state
- **Log Export**: Download system logs
- **Diagnostic Report**: Generate comprehensive system report

**User Actions Available**:
- Run detection tests
- Verify zone setup
- Check system components
- Simulate scenarios
- View debug information
- Profile performance
- Export test results
- Generate diagnostic reports

**Data Displayed**:
- Test results and status
- Detection accuracy metrics
- System health indicators
- Performance statistics
- Error logs and warnings
- Debug information
- Profiling data

---

## 🔄 Navigation Flow

### User Journey Map:

```
1. START → Home Page
   ↓
2. Click "Start Monitoring" → Upload Video Page
   ↓
3. Upload Video → Draw Queue Zones → Start Detection
   ↓
4. Detection Running → Click "Live Dashboard"
   ↓
5. View Real-Time Data → Monitor Queues → Get Recommendations
   ↓
6. (Optional) Analytics → View Historical Data
   ↓
7. (Optional) Settings → Adjust Parameters
   ↓
8. (Optional) Test → Debug/Verify System
```

---

## 🎯 Button Interaction Summary

| Button | Icon | Primary Action | Secondary Actions |
|--------|------|----------------|-------------------|
| **Home** | 🏠 | Load homepage | Show stats, navigate to features |
| **Upload Video** | 🎥 | Upload & configure | Draw zones, start detection, save config |
| **Live Dashboard** | 🧠 | Monitor queues | View video, get recommendations, enable audio |
| **Analytics** | 📊 | View trends | Export data, filter results, compare queues |
| **System** | ⚙️ | Configure settings | Adjust parameters, manage data, view info |
| **Test** | 🧪 | Test system | Debug issues, verify accuracy, profile performance |

---

## 💡 Key Features Per Page

### Home Page Features:
- Welcome message
- System overview
- Quick stats
- Feature showcase
- Call-to-action buttons
- Navigation hub

### Upload Video Features:
- Drag-and-drop upload
- File validation
- Frame preview
- Interactive zone drawing
- Zone editing tools
- Configuration panel
- Start/Stop detection
- Progress tracking

### Live Dashboard Features:
- Auto-refreshing video feed
- Real-time people counting
- Smart recommendations
- Queue status cards
- Analytics chart
- Audio announcements
- Multi-language support
- Manual refresh button

### Analytics Features:
- Historical data charts
- Trend analysis
- Peak hours detection
- Performance metrics
- Data export
- Custom date ranges
- Queue comparison

### System Features:
- Detection configuration
- Video settings
- Refresh intervals
- Audio preferences
- Notification setup
- System information
- Data management

### Test Features:
- Detection testing
- Zone verification
- Component checks
- Simulation tools
- Debug console
- Performance profiling
- Diagnostic reports

---

**Design System Version**: 1.0  
**Last Updated**: October 21, 2025  
**Status**: Production Ready ✅

---

This specification provides everything needed to recreate the exact design in Figma or any design tool. Follow these guidelines precisely for pixel-perfect results! 🎨
