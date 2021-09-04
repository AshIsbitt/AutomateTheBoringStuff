# Pausing until a specific date

'''
This code checks if it's halloween 2019 every 100 seconds.
'''

import datetime as dt
import time

halloween2019 = dt.datetime(2019, 10, 31, 0, 0, 0)

while dt.datetime.now() < halloween2019:
    time.sleep(100)
