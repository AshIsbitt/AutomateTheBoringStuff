# Dragging the mouse onscreen

import pyautogui as pyag
import time

print('Move mouse over drawing window')
time.sleep(5)
pyag.click()

distance = 300
change = 20

while distance > 0:
    pyag.drag(distance, 0, duration=0.2, button='left')
    distance = distance - change
    pyag.drag(0, distance, duration=0.2, button='left')
    pyag.drag(-distance, 0,  duration=0.2, button='left')
    distance = distance - change
    pyag.drag(0, -distance, duration=0.2, button='left')


print('done')
