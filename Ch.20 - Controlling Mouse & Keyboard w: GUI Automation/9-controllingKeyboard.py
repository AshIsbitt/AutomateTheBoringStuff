# Controlling the keyboard

import pyautogui as pyag

# Make sure you get the focus of the right window
pyag.click(100,200, button='left')

pyag.write('Hello world')
pyag.write(['a', 'b', 'left', 'left', 'x', 'y'])

pyag.keyDown('shift')
pyag.press('4')
pyag.keyUp('shift')
