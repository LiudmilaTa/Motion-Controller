"""
Configuration settings for Motion Controller
All thresholds, colors, and constants in one place
"""

import pyautogui

# Gesture detection thresholds
SIDE_THRESHOLD = 0.1  # How far from nose hand must move
UP_THRESHOLD = 0.05
DOWN_THRESHOLD = -0.05  # Below waist
DEADZONE = 0.2  # Zone width where movements don't register

# Depth limits (distance from camera)
MIN_Z = -0.7
MAX_Z = 0.2

# Hand visualization colors (BGR format)
HAND_COLOR_LEFT = (255, 0, 0)  # Blue
HAND_COLOR_RIGHT = (0, 0, 255)  # Red

# Mouse control settings
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()
MOUSE_SMOOTHING = 0.7  # Mouse movement smoothing factor (0.0 - 1.0, higher = faster response)
INITIAL_MOUSE_X = SCREEN_WIDTH // 2
INITIAL_MOUSE_Y = SCREEN_HEIGHT // 2

# PyAutoGUI settings
PYAUTOGUI_PAUSE = 0  # No delay between commands
PYAUTOGUI_FAILSAFE = False  # Disable failsafe (moving mouse to corner won't stop program)

# MediaPose settings
MIN_DETECTION_CONFIDENCE = 0.5
MIN_TRACKING_CONFIDENCE = 0.5

# Camera settings
CAMERA_INDEX = 0  # Default camera

# UI settings
CHECKBOX_REGION_WIDTH = 150  # Width of checkbox area from right edge
CHECKBOX_SPACING = 40  # Vertical spacing between checkboxes
