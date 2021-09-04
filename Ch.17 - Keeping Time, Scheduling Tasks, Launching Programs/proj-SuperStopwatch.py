# Project - super stopwatch

import time

# Display instruction
print('Press ENTER to begin. Afterwards, press ENTER to click the stopwatch. Press CTRL+C to quit')
input()
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print(f' Lap #{lapNum} {totalTime} ({lapTime})')
        
        lapNum += 1
        lastTime = time.time()

# If user quits program
except KeyboardInterrupt:
    print('Done')
