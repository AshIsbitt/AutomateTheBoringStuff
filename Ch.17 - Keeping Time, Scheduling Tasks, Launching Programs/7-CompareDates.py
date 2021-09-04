# Comparison between different datetime objects

import datetime as dt
import time

halloween2019 = dt.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = dt.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = dt.datetime(2019, 10, 31, 0, 0, 0)

print(halloween2019 == oct31_2019)
print(halloween2019 > newyears2020)
print(newyears2020 > halloween2019)
print(newyears2020 != oct31_2019)
