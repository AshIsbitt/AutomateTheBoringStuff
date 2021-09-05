# Prettified stopwatch

import time
import pyperclip

# Display instruction
input('Press ENTER to begin. Afterwards, press ENTER to click the stopwatch. Press CTRL+C to quit')
print('Started')

startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()

        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        lapOutput = (
            f'Lap #{lapNum} {str(totalTime).rjust(5)} ({str(lapTime).rjust(3)})', end="")
        print(lapOutput)

        lapNum += 1
        lastTime = time.time()
        pyperclip.copy(lapOutput)

# If user quits program
except KeyboardInterrupt:
    print('Done')
    print('Final lap copied to clipboard')
