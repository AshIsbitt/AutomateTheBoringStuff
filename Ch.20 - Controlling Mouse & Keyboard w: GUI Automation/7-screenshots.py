# Screenshot manipulation

import pyautogui as pyag

# Take screenshot
im = pyag.screenshot()

# Analysing colour of pixels on screen
print(pyag.pixel((0,0)))
print(pyag.pixel((50, 200)))

#Check against pre-set colour
print(pyag.pixelMatchesColor(50, 200, (130, 135, 144)))


