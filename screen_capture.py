# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 21:51:17 2021

@author: Ayan Gangopadhyay
"""
import pyautogui
import cv2 
import numpy as np
import tkinter as tk
import pygetwindow as gw


# Get sceen resolution
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Define resolution
resolution = (screen_width, screen_height)

# Get the 'Celeste' window
celeste_window = None

for window in  gw.getWindowsWithTitle('Celeste'):
    if window.title == 'Celeste':
        celeste_window = window
        break

# Adjust the width and height and put to top left
CELESTE_WIDTH = 774
CELESTE_HEIGHT = 465

celeste_window.resizeTo(CELESTE_WIDTH, CELESTE_HEIGHT)
celeste_window.moveTo(0, 0)
  
# Create an Empty window, this will show our capture
cv2.namedWindow("Live", cv2.WINDOW_NORMAL) 
  
# Resize this window and move to top right 
location_xy = [int(screen_width*0.6), 0]
cv2.resizeWindow("Live", (int(screen_width*0.4), int(screen_height*0.4)))
cv2.moveWindow("Live", *location_xy)

# Capture Screen
while True: 
    # Take screenshot using PyAutoGUI 
    celeste_reigon = (0, 0, CELESTE_WIDTH, CELESTE_HEIGHT)
    img = pyautogui.screenshot(region=celeste_reigon) 
  
    # Convert the screenshot to a numpy array 
    frame = np.array(img) 
  
    # Convert it from BGR(Blue, Green, Red) to 
    # Greyscale 
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Edge detection routine
    frame = cv2.Canny(frame, 40, 140)
    
    # Optional: Display the recording screen 
    cv2.imshow('Live', frame) 
      
    # Stop recording when we press 'q' 
    if cv2.waitKey(1) == ord('q'): 
        break
  
# Destroy all windows 
cv2.destroyAllWindows()



