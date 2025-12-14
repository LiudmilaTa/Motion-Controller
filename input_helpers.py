"""
Input Helper functions for Motion Controller
Contains functions for keyboard and mouse input handling
"""

import pyautogui

# Global variable to track which input method is available
use_directinput = False
pydirectinput = None


def init_input_system():
    """Initialize input system, preferring pydirectinput for game compatibility"""
    global use_directinput, pydirectinput
    try:
        import pydirectinput as pdi
        pydirectinput = pdi
        use_directinput = True
        print("✓ pydirectinput loaded - game compatibility enabled")
        return True
    except ImportError:
        use_directinput = False
        print("⚠ pydirectinput not found - using pyautogui")
        print("For game compatibility install: pip install pydirectinput")
        return False

def press_key(key):
    """Press a keyboard key"""
    if use_directinput and pydirectinput:
        pydirectinput.keyDown(key)
    else:
        pyautogui.keyDown(key)


def release_key(key):
    """Release a keyboard key"""
    if use_directinput and pydirectinput:
        pydirectinput.keyUp(key)
    else:
        pyautogui.keyUp(key)

def release_all_keys(keys_pressed):
    """Release all currently pressed keys"""
    for k in keys_pressed:
        if keys_pressed[k]:
            if k == 'mouse_click':
                pyautogui.mouseUp()
            elif k != 'both_sides':  # both_sides is a state flag, not a key
                release_key(k)