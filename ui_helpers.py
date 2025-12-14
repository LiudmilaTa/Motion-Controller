"""
UI Helper functions for Motion Controller
Contains functions for drawing loading screens, instructions, and UI elements
"""

import cv2
import numpy as np

def show_loading_screen(text, progress=0):
    """Display a loading screen with progress bar"""
    loading_screen = np.zeros((480, 640, 3), dtype=np.uint8)
    loading_screen[:] = (40, 40, 40)  # Dark gray background
    
    # Title
    cv2.putText(loading_screen, "MOTION CONTROLLER", (120, 100), 
                cv2.FONT_HERSHEY_DUPLEX, 1.2, (255, 255, 255), 3)
    
    # Loading text
    cv2.putText(loading_screen, text, (50, 250), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (200, 200, 200), 2)
    
    # Progress bar
    bar_width = 500
    bar_height = 30
    bar_x = 70
    bar_y = 300
    
    # Progress bar frame
    cv2.rectangle(loading_screen, (bar_x, bar_y), 
                  (bar_x + bar_width, bar_y + bar_height), (100, 100, 100), 2)
    
    # Progress bar fill
    if progress > 0:
        fill_width = int((bar_width - 4) * progress / 100)
        cv2.rectangle(loading_screen, (bar_x + 2, bar_y + 2), 
                      (bar_x + 2 + fill_width, bar_y + bar_height - 2), 
                      (0, 255, 0), -1)
    
    # Percentage
    cv2.putText(loading_screen, f"{progress}%", (bar_x + bar_width // 2 - 30, bar_y + 55), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    
    cv2.imshow('Motion Controller', loading_screen)
    cv2.waitKey(1)

def draw_instructions():
    """Draw the instruction window with stick figures showing gestures"""
    inst = np.zeros((600, 800, 3), dtype=np.uint8)
    inst[:] = (30, 30, 30)
    
    # Title
    cv2.putText(inst, "INSTRUCTIONS", (270, 40), 
                cv2.FONT_HERSHEY_DUPLEX, 1.0, (255, 255, 255), 2)
    
    # Keyboard mode section
    cv2.putText(inst, "KEYBOARD MODE:", (20, 80), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    
    # Draw stick figure - LEFT
    center_x, center_y = 120, 200
    cv2.circle(inst, (center_x, center_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (center_x, center_y - 20), (center_x, center_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (center_x, center_y), (center_x - 50, center_y + 10), (255, 0, 0), 3)
    cv2.putText(inst, "LEFT", (center_x - 80, center_y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    cv2.line(inst, (center_x, center_y), (center_x + 30, center_y + 10), (255, 255, 255), 2)
    cv2.line(inst, (center_x, center_y + 40), (center_x - 15, center_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (center_x, center_y + 40), (center_x + 15, center_y + 70), (255, 255, 255), 2)
    
    # Stick figure - RIGHT
    right_x, right_y = 260, 200
    cv2.circle(inst, (right_x, right_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (right_x, right_y - 20), (right_x, right_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (right_x, right_y), (right_x - 30, right_y + 10), (255, 255, 255), 2)
    cv2.line(inst, (right_x, right_y), (right_x + 50, right_y + 10), (0, 0, 255), 3)
    cv2.putText(inst, "RIGHT", (right_x + 55, right_y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.line(inst, (right_x, right_y + 40), (right_x - 15, right_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (right_x, right_y + 40), (right_x + 15, right_y + 70), (255, 255, 255), 2)
    
    # Stick figure for UP
    up_x, up_y = 400, 200
    cv2.putText(inst, "UP/SPACE", (up_x - 45, up_y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.circle(inst, (up_x, up_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (up_x, up_y - 20), (up_x, up_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (up_x, up_y), (up_x - 30, up_y - 30), (0, 255, 0), 3)
    cv2.line(inst, (up_x, up_y), (up_x + 30, up_y - 30), (0, 255, 0), 3)
    cv2.line(inst, (up_x, up_y + 40), (up_x - 15, up_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (up_x, up_y + 40), (up_x + 15, up_y + 70), (255, 255, 255), 2)
    
    # Stick figure for DOWN
    down_x, down_y = 540, 200
    cv2.putText(inst, "DOWN", (down_x - 30, down_y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
    cv2.circle(inst, (down_x, down_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (down_x, down_y - 20), (down_x, down_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (down_x, down_y), (down_x - 30, down_y + 40), (0, 255, 255), 3)
    cv2.line(inst, (down_x, down_y), (down_x + 30, down_y + 40), (0, 255, 255), 3)
    cv2.line(inst, (down_x, down_y + 40), (down_x - 15, down_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (down_x, down_y + 40), (down_x + 15, down_y + 70), (255, 255, 255), 2)
    
    # Stick figure for both hands spread (mouse click)
    both_x, both_y = 680, 200
    cv2.putText(inst, "CLICK", (both_x - 30, both_y - 70), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    cv2.circle(inst, (both_x, both_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (both_x, both_y - 20), (both_x, both_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (both_x, both_y), (both_x - 50, both_y + 10), (255, 0, 255), 3)
    cv2.line(inst, (both_x, both_y), (both_x + 50, both_y + 10), (255, 0, 255), 3)
    cv2.line(inst, (both_x, both_y + 40), (both_x - 15, both_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (both_x, both_y + 40), (both_x + 15, both_y + 70), (255, 255, 255), 2)
    
    # Mouse mode section
    cv2.putText(inst, "MOUSE MODE:", (20, 320), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
    
    # Stick figure for cursor control
    mouse_x, mouse_y = 200, 440
    cv2.circle(inst, (mouse_x, mouse_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (mouse_x, mouse_y - 20), (mouse_x, mouse_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (mouse_x, mouse_y), (mouse_x + 50, mouse_y + 10), (255, 255, 0), 3)
    cv2.line(inst, (mouse_x, mouse_y), (mouse_x - 30, mouse_y + 10), (255, 255, 255), 2)
    cv2.line(inst, (mouse_x, mouse_y + 40), (mouse_x - 15, mouse_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (mouse_x, mouse_y + 40), (mouse_x + 15, mouse_y + 70), (255, 255, 255), 2)
    cv2.putText(inst, "Right hand -", (mouse_x - 120, mouse_y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    cv2.putText(inst, "cursor", (mouse_x - 120, mouse_y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    
    # Stick figure for mouse click
    click_x, click_y = 500, 440
    cv2.circle(inst, (click_x, click_y - 40), 20, (255, 255, 255), 2)
    cv2.line(inst, (click_x, click_y - 20), (click_x, click_y + 40), (255, 255, 255), 2)
    cv2.line(inst, (click_x, click_y), (click_x - 50, click_y + 10), (0, 255, 0), 3)
    cv2.line(inst, (click_x, click_y), (click_x + 30, click_y + 10), (255, 255, 255), 2)
    cv2.line(inst, (click_x, click_y + 40), (click_x - 15, click_y + 70), (255, 255, 255), 2)
    cv2.line(inst, (click_x, click_y + 40), (click_x + 15, click_y + 70), (255, 255, 255), 2)
    cv2.putText(inst, "Left hand left -", (click_x - 130, click_y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(inst, "hold click", (click_x - 130, click_y - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Notes
    cv2.putText(inst, "ESC - Exit | Hints - show/hide zones | Mouse - switch mode", 
                (20, 570), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150, 150, 150), 1)
    
    return inst

def draw_control_zones(image, frame_w, frame_h, nose_x_screen, nose_y_screen, waist_y_screen, deadzone, up_threshold, down_threshold, mouse_enabled):
    """Draw control zones overlay on the image"""
    if mouse_enabled:
        # Show only click zone for left hand in mouse mode
        left_zone_x = int(nose_x_screen - (deadzone * frame_w))
        cv2.rectangle(image, (0, 0), (left_zone_x, frame_h), (0, 255, 0), 2)
        cv2.putText(image, "CLICK ZONE", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Mouse mode label (bottom center, white color)
        cv2.putText(image, "MOUSE CONTROL MODE", (frame_w // 2 - 150, frame_h - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    else:
        # LEFT zone (left side of screen)
        left_zone_x = int(nose_x_screen - (deadzone * frame_w))
        cv2.rectangle(image, (0, 0), (left_zone_x, frame_h), (255, 0, 0), 2)
        cv2.putText(image, "LEFT ZONE", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
        
        # RIGHT zone (right side of screen)
        right_zone_x = int(nose_x_screen + (deadzone * frame_w))
        cv2.rectangle(image, (right_zone_x, 0), (frame_w, frame_h), (0, 0, 255), 2)
        cv2.putText(image, "RIGHT ZONE", (frame_w - 180, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # UP zone (upper part)
        up_zone_y = int(nose_y_screen - (up_threshold * frame_h))
        cv2.line(image, (0, up_zone_y), (frame_w, up_zone_y), (0, 255, 0), 2)
        cv2.putText(image, "UP ZONE", (frame_w // 2 - 80, up_zone_y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # DOWN zone (lower part)
        down_zone_y = int(waist_y_screen + (down_threshold * frame_h))
        cv2.line(image, (0, down_zone_y), (frame_w, down_zone_y), (0, 255, 255), 2)
        cv2.putText(image, "DOWN ZONE", (frame_w // 2 - 100, down_zone_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
        
        # Keyboard mode label
        cv2.putText(image, "KEYBOARD MODE", (frame_w // 2 - 120, frame_h - 20), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def draw_ui_controls(image, frame_w, frame_h, show_hints, mouse_enabled):
    """Draw UI control checkboxes in bottom right corner"""
    checkbox_x = frame_w - 150
    
    # Draw hints toggle checkbox
    checkbox_y = frame_h - 105
    cv2.rectangle(image, (checkbox_x, checkbox_y - 10), (checkbox_x + 20, checkbox_y + 10), (255, 255, 255), 2)
    if show_hints:
        cv2.line(image, (checkbox_x + 3, checkbox_y), (checkbox_x + 8, checkbox_y + 7), (0, 255, 0), 2)
        cv2.line(image, (checkbox_x + 8, checkbox_y + 7), (checkbox_x + 17, checkbox_y - 7), (0, 255, 0), 2)
    cv2.putText(image, "Hints", (checkbox_x + 25, checkbox_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    # Draw mouse mode toggle checkbox
    checkbox_mouse_y = frame_h - 65
    cv2.rectangle(image, (checkbox_x, checkbox_mouse_y - 10), (checkbox_x + 20, checkbox_mouse_y + 10), (255, 255, 255), 2)
    if mouse_enabled:
        cv2.line(image, (checkbox_x + 3, checkbox_mouse_y), (checkbox_x + 8, checkbox_mouse_y + 7), (0, 255, 255), 2)
        cv2.line(image, (checkbox_x + 8, checkbox_mouse_y + 7), (checkbox_x + 17, checkbox_mouse_y - 7), (0, 255, 255), 2)
    cv2.putText(image, "Mouse", (checkbox_x + 25, checkbox_mouse_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    
    # Draw help button
    button_inst_y = frame_h - 25
    cv2.rectangle(image, (checkbox_x, button_inst_y - 10), (checkbox_x + 20, button_inst_y + 10), (255, 200, 0), 2)
    cv2.putText(image, "?", (checkbox_x + 5, button_inst_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 200, 0), 2)
    cv2.putText(image, "Help", (checkbox_x + 25, button_inst_y + 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 200, 0), 1)