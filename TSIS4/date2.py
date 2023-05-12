import datetime

#Write a Python program to subtract five days from current date.

x = datetime.datetime.now()
y = datetime.datetime(x.year, x.month, x.day - 5)
print(y.strftime("%x"), "\n")

#Write a Python program to print yesterday, today, tomorrow.

yst = datetime.datetime(x.year, x.month, x.day - 1)
tmw = datetime.datetime(x.year, x.month, x.day + 1)
print(yst.strftime("%x"), x.strftime("%x"), tmw.strftime("%x"), "\n")

#Write a Python program to drop microseconds from datetime.

print(x.strftime("%x"), x.strftime("%X") + ":" + x.strftime("%f"))

#Write a Python program to calculate two date difference in seconds.

y = int(input("Enter year: "))
m = int(input("Enter month: "))
d = int(input("Enter day: "))

s = ((((y*12) + m)*30) + d)*24*3600
sNow = ((((x.year*12) + x.month)*30) + x.day)*24*3600 + x.hour*3600 + x.minute*60

print(abs(s - sNow))