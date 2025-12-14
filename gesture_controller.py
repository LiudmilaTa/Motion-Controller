"""
Gesture recognition logic for Motion Controller
Handles pose detection and gesture interpretation
"""

import pyautogui
from config import DEADZONE, UP_THRESHOLD, DOWN_THRESHOLD, MIN_Z, MAX_Z
from input_helpers import press_key, release_key

class GestureController:
    """Manages gesture recognition and input control"""
    
    def __init__(self):
        self.keys_pressed = {
            'left': False,
            'right': False,
            'up': False,
            'down': False,
            'space': False,
            'mouse_click': False,
            'both_sides': False
        }
        self.last_mouse_x = None
        self.last_mouse_y = None
    
    def check_depth(self, nose_z):
        """Check if user is at correct distance from camera"""
        if nose_z < MIN_Z:
            return "too_close", "Move back (too close)"
        elif nose_z > MAX_Z:
            return "too_far", "Move closer (too far)"
        return "ok", "Position OK"
    
    def handle_keyboard_mode(self, landmarks, nose_x_mirror, frame_h, show_hints, screen_width, screen_height):
        """Process gestures in keyboard control mode"""
        lw = landmarks['left_wrist']
        rw = landmarks['right_wrist']
        lh = landmarks['left_hip']
        rh = landmarks['right_hip']
        
        lw_x_mirror = landmarks['left_wrist_mirror']
        rw_x_mirror = landmarks['right_wrist_mirror']
        
        # Check for both hands spread (mouse click gesture)
        both_hands_out = (lw_x_mirror < nose_x_mirror - DEADZONE) and (rw_x_mirror > nose_x_mirror + DEADZONE)
        
        if both_hands_out:
            if not self.keys_pressed['both_sides']:
                pyautogui.click(screen_width // 2, screen_height // 2)
                self.keys_pressed['both_sides'] = True
                print("🖱️ Mouse click (both hands spread)")
            return "MOUSE CLICK"
        else:
            self.keys_pressed['both_sides'] = False
        
        active_gesture = None
        
        # LEFT gesture
        if lw_x_mirror < nose_x_mirror - DEADZONE and not both_hands_out:
            if not self.keys_pressed['left']:
                press_key('left')
                self.keys_pressed['left'] = True
            active_gesture = "LEFT"
        else:
            if self.keys_pressed['left']:
                release_key('left')
                self.keys_pressed['left'] = False
        
        # RIGHT gesture
        if rw_x_mirror > nose_x_mirror + DEADZONE and not both_hands_out:
            if not self.keys_pressed['right']:
                press_key('right')
                self.keys_pressed['right'] = True
            active_gesture = "RIGHT"
        else:
            if self.keys_pressed['right']:
                release_key('right')
                self.keys_pressed['right'] = False
        
        # UP gesture
        if lw.y < landmarks['nose'].y - UP_THRESHOLD or rw.y < landmarks['nose'].y - UP_THRESHOLD:
            if not self.keys_pressed['up']:
                press_key('up')
                self.keys_pressed['up'] = True
            if not self.keys_pressed['space']:
                press_key('space')
                self.keys_pressed['space'] = True
            active_gesture = "UP"
        else:
            if self.keys_pressed['up']:
                release_key('up')
                self.keys_pressed['up'] = False
            if self.keys_pressed['space']:
                release_key('space')
                self.keys_pressed['space'] = False
        
        # DOWN gesture
        waist_y = (lh.y + rh.y) / 2
        if lw.y > waist_y + DOWN_THRESHOLD or rw.y > waist_y + DOWN_THRESHOLD:
            if not self.keys_pressed['down']:
                press_key('down')
                self.keys_pressed['down'] = True
            active_gesture = "DOWN"
        else:
            if self.keys_pressed['down']:
                release_key('down')
                self.keys_pressed['down'] = False
        
        return active_gesture
    
    def handle_mouse_mode(self, landmarks, nose_x_mirror, screen_width, screen_height, mouse_smoothing):
        """Process gestures in mouse control mode"""
        rw = landmarks['right_wrist']
        lw_x_mirror = landmarks['left_wrist_mirror']
        
        # Right hand controls cursor
        target_x = int((1 - rw.x) * screen_width)
        target_y = int(rw.y * screen_height)
        
        # Initialize mouse position if needed
        if self.last_mouse_x is None:
            self.last_mouse_x = screen_width // 2
            self.last_mouse_y = screen_height // 2
        
        # Smooth movement
        new_x = int(self.last_mouse_x + (target_x - self.last_mouse_x) * mouse_smoothing)
        new_y = int(self.last_mouse_y + (target_y - self.last_mouse_y) * mouse_smoothing)
        
        pyautogui.moveTo(new_x, new_y)
        self.last_mouse_x = new_x
        self.last_mouse_y = new_y
        
        # Left hand left - hold mouse button
        active_gesture = None
        if lw_x_mirror < nose_x_mirror - DEADZONE:
            if not self.keys_pressed['mouse_click']:
                pyautogui.mouseDown()
                self.keys_pressed['mouse_click'] = True
            active_gesture = "CLICK HOLD"
        else:
            if self.keys_pressed['mouse_click']:
                pyautogui.mouseUp()
                self.keys_pressed['mouse_click'] = False
        
        return active_gesture
    
    def release_all(self):
        """Release all pressed keys and buttons"""
        for k in self.keys_pressed:
            if self.keys_pressed[k]:
                if k == 'mouse_click':
                    pyautogui.mouseUp()
                elif k != 'both_sides':
                    release_key(k)
                self.keys_pressed[k] = False
