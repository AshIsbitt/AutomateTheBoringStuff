# Timedelta

# This represents a duration of time rather than a moment of time

import time
import datetime as dt

delta = dt.timedelta(days=11, hours=10, minutes=9, seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(str(delta))
