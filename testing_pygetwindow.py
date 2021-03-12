# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 22:44:30 2021

@author: DELL
"""

import pygetwindow as gw
import tkinter as tk

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

print(celeste_window)