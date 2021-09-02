# Limit, Timeout, Default

import pyinputplus as pyin

#This will crash after two failed inputs
# pyinputplus.RetryLimitException
response = pyin.inputNum(limit=2)
print(response)

#This will crash if the user waits too long to enter input
response2 = pyin.inputNum(timeout=10)
print(response2)

#Instead of crashing like line 7 does, this will set response3 to "N/A" after two failed attempts
response3 = pyin.inputNum(limit=2, default="N/A")
print(response3)