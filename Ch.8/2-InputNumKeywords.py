# Integer Keyword Arguements

import pyinputplus as pyin

response = pyin.inputNum('Enter Num: ', min=4)
print(response)

response2 = pyin.inputNum('Enter Num: ', greaterThan=4)
print(response2)

response3 = pyin.inputNum('Enter Num: ', min=4, lessThan=6)
print(response3)

response4 = pyin.inputNum('Enter Num: ', blank=True)
print(response4)