# Motion Controller

A gesture-based game controller that uses your webcam and body pose detection to control keyboard and mouse inputs. Transform your body movements into game controls without any additional hardware!

## Project Information

**Course:** NI-CCC (Computer and Communication Networks)  
**University:** Czech Technical University in Prague (ČVUT)  
**Year:** 2025  
**Team Members:**
- Student Name 1 - [student1@fit.cvut.cz]
- Student Name 2 - [student2@fit.cvut.cz]

## Features

- **Real-time Pose Detection** - Uses MediaPipe for accurate body tracking
- **Gesture-based Controls** - Map body movements to keyboard and mouse actions
- **Low Latency** - Optimized for responsive gaming experience
- **Customizable Zones** - Configure control areas on screen
- **Visual Feedback** - See your pose skeleton and control zones in real-time
- **No Special Hardware Required** - Works with any standard webcam

## How It Works

The application captures video from your webcam and uses MediaPipe's pose detection to track your body position. Based on the position of your hands and body, it translates movements into keyboard and mouse inputs:

- **Left Hand** - WASD movement controls
- **Right Hand** - Mouse movement and actions
- **Body Position** - Jump, crouch, and other actions
- **Gestures** - Special actions based on pose combinations

## Start. Manual Launch via Python

1. **Install Python 3.7+** from [python.org](https://python.org)
   - ⚠️ Make sure to check "Add Python to PATH" during installation

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   python app.py
   ```

## Requirements

### Software
- Python 3.7 or newer
- Dependencies (automatically installed):
  - opencv-python >= 4.5.0
  - mediapipe >= 0.8.0
  - pyautogui >= 0.9.0
  - pydirectinput >= 1.0.0
  - numpy >= 1.19.0

## Controls

### Default Mapping

| Body Part | Position | Action |
|-----------|----------|--------|
| Left Hand | Left Zone | Move Left (A) |
| Left Hand | Right Zone | Move Right (D) |
| Left Hand | Up Zone | Move Forward (W) |
| Left Hand | Down Zone | Move Backward (S) |
| Right Hand | Movement | Mouse Cursor |
| Right Hand | Close to Body | Left Click |
| Body | Jump Motion | Spacebar |

### Customization

Control mappings and sensitivity can be adjusted in `config.py`:
- `DEADZONE` - Minimum movement threshold
- `UP_THRESHOLD` / `DOWN_THRESHOLD` - Control zone boundaries
- `MOUSE_SMOOTHING` - Mouse movement smoothing factor

## roject Structure

```
Controller/
├── app.py                  # Main application entry point
├── camera_utils.py         # Camera initialization and utilities
├── config.py               # Configuration settings
├── gesture_controller.py   # Gesture recognition and mapping
├── input_helpers.py        # Input system initialization
├── ui_helpers.py           # UI drawing functions
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Configuration

Edit `config.py` to customize:

```python
# Screen resolution
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

# Control sensitivity
DEADZONE = 0.1
MOUSE_SMOOTHING = 0.3

# Detection confidence
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5
```

## Troubleshooting

### Camera not detected
- Check if camera is connected and not used by another application
- Try running as administrator

### High CPU usage
- Reduce camera resolution in `camera_utils.py`
- Lower tracking confidence in `config.py`

### Input not responding
- Ensure the application window has focus
- Check if DirectInput is properly initialized
- Verify PyAutoGUI failsafe is not triggered (move mouse to corner)

### Dependencies installation fails
- Run command prompt as administrator
- Update pip: `python -m pip install --upgrade pip`
- Install dependencies one by one to identify the problematic package

## Technical Details

### Pose Detection
- Uses MediaPipe Pose for 33 body landmarks detection
- Processes frames at 30 FPS (configurable)
- Normalized coordinates for resolution independence

### Input Simulation
- Primary: pydirectinput (for games)
- Fallback: pyautogui (for general use)
- Supports both keyboard and mouse events

### Performance Optimization
- Frame skipping for low-end systems
- Smoothing algorithms for stable cursor movement
- Dead zones to prevent input jitter

## License

This project is created for educational purposes as part of NI-CCC course at CTU.

## Acknowledgments

- **MediaPipe** - Google's pose detection framework
- **OpenCV** - Computer vision library
- **PyAutoGUI** - Input automation library

*Developed as part of NI-CCC course project at Czech Technical University in Prague, 2025*
