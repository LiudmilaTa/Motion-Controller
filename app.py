"""
Motion Controller - Gesture-based game controller using webcam
Controls keyboard and mouse through body pose detection
"""

import cv2
import mediapipe as mp
import pyautogui
import time

from ui_helpers import show_loading_screen, draw_instructions, draw_control_zones, draw_ui_controls
from input_helpers import init_input_system
from camera_utils import initialize_camera, create_ui_callback, extract_landmarks
from gesture_controller import GestureController
from config import (
    DEADZONE, UP_THRESHOLD, DOWN_THRESHOLD,
    HAND_COLOR_LEFT, HAND_COLOR_RIGHT,
    SCREEN_WIDTH, SCREEN_HEIGHT, MOUSE_SMOOTHING,
    PYAUTOGUI_PAUSE, PYAUTOGUI_FAILSAFE,
    MIN_DETECTION_CONFIDENCE, MIN_TRACKING_CONFIDENCE
)

# Create loading window
cv2.namedWindow('Motion Controller', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Motion Controller', cv2.WND_PROP_TOPMOST, 1)

# Loading screen - Initialization
show_loading_screen("Initializing...", 10)
time.sleep(0.3)

# Initialize input system
if init_input_system():
    show_loading_screen("Loading DirectInput module...", 25)
else:
    show_loading_screen("Loading standard input...", 25)

time.sleep(0.3)
show_loading_screen("Loading MediaPipe...", 40)

mp_pose = mp.solutions.pose

time.sleep(0.2)

# Initialize camera
cap = initialize_camera()
if cap is None:
    exit()

show_loading_screen("Initializing pose detector...", 90)
time.sleep(0.3)

show_loading_screen("Ready!", 100)
time.sleep(0.5)

# Application state
state = {
    'show_hints': True,
    'mouse_enabled': False,
    'show_instructions': False,
    'gesture_controller': None
}

# Initialize gesture controller
gesture_controller = GestureController()
state['gesture_controller'] = gesture_controller

# Disable pyautogui delays for faster response
pyautogui.PAUSE = PYAUTOGUI_PAUSE
pyautogui.FAILSAFE = PYAUTOGUI_FAILSAFE

# Create and set mouse callback
mouse_callback = create_ui_callback(state)
cv2.setMouseCallback('Motion Controller', mouse_callback, {'frame_w': 640, 'frame_h': 480})

# Main loop
with mp_pose.Pose(min_detection_confidence=MIN_DETECTION_CONFIDENCE, 
                  min_tracking_confidence=MIN_TRACKING_CONFIDENCE) as pose:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break

        frame_h, frame_w, _ = frame.shape
        
        # Update callback parameters with actual frame dimensions
        cv2.setMouseCallback('Motion Controller', mouse_callback, {'frame_w': frame_w, 'frame_h': frame_h})

        # Mirror frame for display only
        image = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        hint_text = ""
        active_gesture = None

        # Extract landmarks
        landmarks = extract_landmarks(results, mp_pose)
        
        if landmarks:
            nose = landmarks['nose']
            lw = landmarks['left_wrist']
            rw = landmarks['right_wrist']
            nose_x_mirror = landmarks['nose_mirror']

            # Draw control zones (if hints enabled)
            if state['show_hints']:
                # Calculate screen coordinates for zones
                nose_x_screen = frame_w - int(nose.x * frame_w)
                nose_y_screen = int(nose.y * frame_h)
                waist_y = (landmarks['left_hip'].y + landmarks['right_hip'].y) / 2
                waist_y_screen = int(waist_y * frame_h)
                
                draw_control_zones(image, frame_w, frame_h, nose_x_screen, nose_y_screen, 
                                 waist_y_screen, DEADZONE, UP_THRESHOLD, DOWN_THRESHOLD, 
                                 state['mouse_enabled'])

            # Check depth (distance from camera)
            depth_status, hint_text = gesture_controller.check_depth(nose.z)
            
            if depth_status != "ok":
                # User too close or too far - release all controls
                gesture_controller.release_all()
            else:
                # Process gestures based on mode
                if state['mouse_enabled']:
                    active_gesture = gesture_controller.handle_mouse_mode(
                        landmarks, nose_x_mirror, SCREEN_WIDTH, SCREEN_HEIGHT, MOUSE_SMOOTHING
                    )
                    if state['show_hints']:
                        if active_gesture:
                            cv2.putText(image, active_gesture, (50, frame_h - 50), 
                                      cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                        cv2.putText(image, "MOUSE MODE", (50, frame_h - 150), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
                else:
                    active_gesture = gesture_controller.handle_keyboard_mode(
                        landmarks, nose_x_mirror, frame_h, state['show_hints'], 
                        SCREEN_WIDTH, SCREEN_HEIGHT
                    )
                    if state['show_hints'] and active_gesture:
                        # Determine text position based on gesture
                        y_positions = {
                            "MOUSE CLICK": frame_h - 250,
                            "LEFT": frame_h - 150,
                            "RIGHT": frame_h - 100,
                            "UP": frame_h - 50,
                            "DOWN": frame_h - 200
                        }
                        colors = {
                            "MOUSE CLICK": (255, 0, 255),
                            "LEFT": HAND_COLOR_LEFT,
                            "RIGHT": HAND_COLOR_RIGHT,
                            "UP": (0, 255, 0),
                            "DOWN": (0, 255, 255)
                        }
                        y_pos = y_positions.get(active_gesture, frame_h - 100)
                        color = colors.get(active_gesture, (255, 255, 255))
                        cv2.putText(image, active_gesture, (50, y_pos), 
                                  cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

            # Draw hands with mirrored coordinates for display (only if hints shown)
            if state['show_hints']:
                cv2.circle(image, (frame_w - int(lw.x * frame_w), int(lw.y * frame_h)), 
                          10, HAND_COLOR_LEFT, -1)
                cv2.circle(image, (frame_w - int(rw.x * frame_w), int(rw.y * frame_h)), 
                          10, HAND_COLOR_RIGHT, -1)

        # Display hint text
        if state['show_hints']:
            cv2.putText(image, hint_text, (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        
        # Draw UI controls in bottom right corner
        draw_ui_controls(image, frame_w, frame_h, state['show_hints'], state['mouse_enabled'])
        
        # Show instruction window if active
        if state['show_instructions']:
            instructions_img = draw_instructions()
            cv2.imshow('Instructions', instructions_img)
            # Check if window was closed by clicking X
            try:
                if cv2.getWindowProperty('Instructions', cv2.WND_PROP_VISIBLE) < 1:
                    state['show_instructions'] = False
            except cv2.error:
                state['show_instructions'] = False
        else:
            # Close instruction window if it was open
            try:
                if cv2.getWindowProperty('Instructions', cv2.WND_PROP_VISIBLE) >= 0:
                    cv2.destroyWindow('Instructions')
            except cv2.error:
                pass  # Window doesn't exist, ignore error
        
        cv2.imshow('Motion Controller', image)
        if cv2.waitKey(10) & 0xFF == 27:  # ESC key
            break

# Release all keys/buttons on exit
gesture_controller.release_all()

cap.release()
cv2.destroyAllWindows()
