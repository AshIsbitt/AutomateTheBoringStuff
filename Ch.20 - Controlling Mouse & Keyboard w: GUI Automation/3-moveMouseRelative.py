# Move the mouse relative to it's starting position

import pyautogui as pyag

for i in range(10):
    pyag.move(100,0, duration=0.25)
    pyag.move(0, 100, duration=0.25)
    pyag.move(-100,0, duration=0.25)
    pyag.move(0, -100, duration=0.25)
