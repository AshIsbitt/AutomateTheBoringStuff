# Get the mouse position - move the mouse around while runnning this

import pyautogui as pyag
import time

for i in range(5):
    print(pyag.position())
    time.sleep(0.5)
