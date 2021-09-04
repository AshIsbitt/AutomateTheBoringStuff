# Converting datetimes to strings

# https://strftime.org

import datetime as dt

oct21_2019 = dt.datetime(2019, 10, 21, 0, 0, 0)

# Using this method, you an format your datetime info into a string
print(oct21_2019.strftime('%Y/%m/%d %H:%M:%S'))
print(oct21_2019.strftime('%I:%M %p'))
print(oct21_2019.strftime("%B of '%y"))

print('--' * 10)

# To convert from a string to a datetime object
# You need to tell the code what the format is using the same formatting strings

print(dt.datetime.strptime('October 21, 2019', '%B %d, %Y'))
print(dt.datetime.strptime('2019/10/21 16:29:00', "%Y/%m/%d %H:%M:%S"))
print(dt.datetime.strptime("October of '19", "%B of '%y"))
