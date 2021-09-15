# Controlling mouse interaction

import pyautogui as pyag
import time

# Click on the screen at the given location
# Use the button arg to specify left, middle or right click
#pyag.click(100,500, button='right')

# mouseDown and mouseUp take the same arguments as above
# pyag.mouseDown(100,100)
# pyag.mouseUp(300,100)

# Scrolling the mouse
# Pos goes up, neg goes down
print('scrolling')
time.sleep(1)
pyag.scroll(50)

# open the interactive shell and type the below for info on mouse position
# import pyautogui
# pyautogui.mouseInfo()
