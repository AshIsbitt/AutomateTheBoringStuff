# Moving the mouse with code

import pyautogui as pyag

for i in range(10):
    # Without the third argument, this will just teleport your mouse
    pyag.moveTo(100,100, duration=0.25)
    pyag.moveTo(200,100, duration=0.25)
    pyag.moveTo(200,200, duration=0.25)
    pyag.moveTo(100,200, duration=0.25)
