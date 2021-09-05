# Launching other programs with python

import subprocess

# This line works differently based on which OS you're on
subprocess.Popen(['open', '/Applications/Discord.app'])
