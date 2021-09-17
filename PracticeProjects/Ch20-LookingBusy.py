# Make the mouse move when you go idle

import pyautogui as pyag
import random
import time

while True:
    # Get current mouse location
    x, y = pyag.position()
    print(pyag.position())

    # Get random number
    waitLen = random.randint(1, 10)
    print(f'Waiting length: {waitLen}')

    # Wait for length of randint
    time.sleep(waitLen)

   # If mouse location changes, restart
    if pyag.position() != (x, y):
        continue

    # Move mouse slightly
    pyag.move(50, 0, duration=0.1)
    print("Mouse Moved")
