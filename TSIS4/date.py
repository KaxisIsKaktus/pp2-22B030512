'''
1. Write a Python program to subtract five days from current date.

2. Write a Python program to print yesterday, today, tomorrow.

3. Write a Python program to drop microseconds from datetime.

4. Write a Python program to calculate two date difference in seconds.
'''

import datetime

# 1
x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day - 5)
print(y.strftime("%x"))

# 2
x = datetime.datetime.now()
print(x.day - 1, x.day, x.day + 1)

# 3
x = datetime.datetime.today().replace(microsecond=0)
print(x)

# 4
x = datetime.datetime.now()
year = int(input())
month = int(input())
day = int(input())

if (x.year != year):
    year = ((x.year - year) * 365 * 24 * 60)
elif (x.year == year):
    year = 0

if (x.month != month):
    month = ((x.month - month) * 30 * 24 * 60)
elif (x.month == month):
    month = 0

if (x.day != day):
    day = ((x.day - day) * 24 * 60)
elif (x.day == day):
    day = 0

diff = ((day + month + year) * 60) + x.minute * 60
print(diff)