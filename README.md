# Motion Controller

A gesture-based game controller that uses your webcam and body pose detection to control keyboard and mouse inputs. Transform your body movements into game controls without any additional hardware!

## Project Information

**Course:** NI-CCC (Computer and Communication Networks)  
**University:** Czech Technical University in Prague (ČVUT)  
**Year:** 2025  
**Team Members:**
- Liudmila Taganashkina - [taganliu@fit.cvut.cz]
- Vladimir Efimov - [efimovla@fit.cvut.cz]

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

## Installation

### Prerequisites
- **Python 3.8+** (recommended: Python 3.8-3.10)
- **Webcam** connected to your computer
- **Windows OS** (for DirectInput support)

### Setup Instructions

1. **Install Python 3.8+** from [python.org](https://python.org)
   - ⚠️ Make sure to check "Add Python to PATH" during installation
   - Verify installation: `python --version`

2. **Clone or download this repository:**
   ```bash
   git clone https://github.com/LiudmilaTa/Motion-Controller.git
   cd Motion-Controller
   ```

3. **Create a clean virtual environment (recommended):**
   ```bash
   python -m venv venv
   
   # Activate on Windows:
   venv\Scripts\activate
   
   # Activate on Linux/Mac:
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   # Clean installation (recommended if you had issues)
   pip install --no-cache-dir -r requirements.txt
   
   # Or standard installation:
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python app.py
   ```

6. **Controls:**
   - Press **ESC** to exit
   - Position yourself in front of the camera
   - Follow on-screen instructions

## Requirements

### Tested Configuration
- **Python:** 3.8
- **opencv-python:** 4.8.1.78
- **mediapipe:** 0.10.8
- **pyautogui:** 0.9.54
- **pydirectinput:** 1.0.4
- **numpy:** 1.23.5

### Important Notes
- ⚠️ **Use a clean virtual environment** to avoid dependency conflicts
- If you have TensorFlow installed, there might be version conflicts (non-critical)
- MediaPipe requires specific file structures - clean installation recommended

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
- Verify camera permissions in Windows Settings

### MediaPipe errors or window closes immediately
**This is the most common issue!** If you see errors like:
```
FileNotFoundError: The path does not exist: .../mediapipe/modules/...
```

**Solution:**
1. **Uninstall all dependencies:**
   ```bash
   pip uninstall opencv-python opencv-contrib-python mediapipe pyautogui pydirectinput numpy -y
   ```

2. **Clear pip cache:**
   ```bash
   pip cache purge
   ```

3. **Reinstall with exact versions:**
   ```bash
   pip install --no-cache-dir -r requirements.txt
   ```

4. **If still failing, use a fresh virtual environment:**
   ```bash
   deactivate  # if in venv
   rm -rf venv  # or manually delete venv folder
   python -m venv venv
   venv\Scripts\activate
   pip install --no-cache-dir -r requirements.txt
   ```

### High CPU usage
- Reduce camera resolution in `camera_utils.py`
- Lower tracking confidence in `config.py`

### Input not responding
- Ensure the application window has focus
- Check if DirectInput is properly initialized
- Verify PyAutoGUI failsafe is not triggered (move mouse to corner)

### Python version issues
- Use Python 3.8-3.10 (tested and stable)
- Python 3.11+ might have compatibility issues with some dependencies

### Dependency conflicts
- Always use a **clean virtual environment**
- Don't mix with existing TensorFlow/ML installations
- If you see TensorFlow warnings, they are usually non-critical for this project

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
