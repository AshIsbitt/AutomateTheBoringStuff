# Project - countdown program

import time
import subprocess

timeLeft = 60

while timeLeft > 0:
    print(timeLeft, end='')
    time.sleep(1)
    timeLeft -= 1

subprocess.Popen(['open', 'alarm.wav'], shell=True)
