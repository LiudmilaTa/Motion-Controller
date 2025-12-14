"""
Camera and initialization utilities for Motion Controller
"""

import cv2
import time
from ui_helpers import show_loading_screen
from config import CAMERA_INDEX

def initialize_camera():
    """Initialize camera with error handling"""
    show_loading_screen("Connecting to camera...", 60)
    cap = cv2.VideoCapture(CAMERA_INDEX)
    
    if not cap.isOpened():
        show_loading_screen("ERROR: Camera not found!", 60)
        time.sleep(2)
        print("ERROR: Camera not found or access blocked!")
        print("Check camera connection and system permissions.")
        cv2.destroyAllWindows()
        return None
    
    show_loading_screen("Camera connected successfully!", 80)
    print("✓ Camera connected successfully!")
    print("Controls: hands left/right, hands up (or space) to jump, hands down")
    print("💡 Both hands spread = mouse click (for game menus)")
    print("Press ESC to exit")
    time.sleep(0.4)
    
    return cap

def create_ui_callback(state):
    """Create mouse callback function with state closure"""
    def mouse_callback(event, x, y, flags, param):
        """Handle mouse clicks on UI elements"""
        if event == cv2.EVENT_LBUTTONDOWN:
            frame_h = param['frame_h']
            frame_w = param['frame_w']
            
            # Check if click is on hints checkbox (bottom right corner)
            if x > frame_w - 150 and x < frame_w - 30 and y > frame_h - 120 and y < frame_h - 90:
                state['show_hints'] = not state['show_hints']
            # Check if click is on mouse mode checkbox (bottom right corner, above hints)
            elif x > frame_w - 150 and x < frame_w - 30 and y > frame_h - 80 and y < frame_h - 50:
                state['mouse_enabled'] = not state['mouse_enabled']
                if state['mouse_enabled']:
                    print("✓ Mouse control mode enabled")
                    print("  Right hand - cursor movement")
                    print("  Left hand left - hold left mouse button (drag)")
                else:
                    print("✓ Keyboard control mode enabled")
                    # Release mouse button when exiting mouse mode
                    if state.get('gesture_controller'):
                        if state['gesture_controller'].keys_pressed.get('mouse_click', False):
                            import pyautogui
                            pyautogui.mouseUp()
                            state['gesture_controller'].keys_pressed['mouse_click'] = False
            # Check if click is on help button (bottom right corner, topmost)
            elif x > frame_w - 150 and x < frame_w - 30 and y > frame_h - 40 and y < frame_h - 10:
                state['show_instructions'] = not state['show_instructions']
                if state['show_instructions']:
                    print("📖 Instructions opened")
                else:
                    print("📖 Instructions closed")
    
    return mouse_callback

def extract_landmarks(results, mp_pose):
    """Extract and organize pose landmarks"""
    if not results.pose_landmarks:
        return None
    
    lm = results.pose_landmarks.landmark
    
    landmarks = {
        'nose': lm[mp_pose.PoseLandmark.NOSE.value],
        'left_wrist': lm[mp_pose.PoseLandmark.LEFT_WRIST.value],
        'right_wrist': lm[mp_pose.PoseLandmark.RIGHT_WRIST.value],
        'left_hip': lm[mp_pose.PoseLandmark.LEFT_HIP.value],
        'right_hip': lm[mp_pose.PoseLandmark.RIGHT_HIP.value],
    }
    
    # Add mirrored coordinates
    landmarks['nose_mirror'] = 1 - landmarks['nose'].x
    landmarks['left_wrist_mirror'] = 1 - landmarks['left_wrist'].x
    landmarks['right_wrist_mirror'] = 1 - landmarks['right_wrist'].x
    
    return landmarks