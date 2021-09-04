# date arithmetic

import datetime as dt

ddt = dt.datetime.now()
print(ddt)

thousandDays = dt.timedelta(days=1000)
print(ddt + thousandDays)

oct21_2019 = dt.datetime(2019, 10, 21, 0, 0, 0)
aboutThirtyYears = dt.timedelta(days=365 * 30)

print(oct21_2019)
print(oct21_2019 - (2 * aboutThirtyYears))
