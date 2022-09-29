import datetime as dt
from this import s
from tkinter import Y

today_date = dt.datetime.today()

print("today date is :", today_date)
print("year is :", today_date.year)
print("month is :", today_date.month)
print("day is :", today_date.day)


time = dt.time(11, 4, 44, 400000 )

print(time)
print("hours :",time.hour)
print("minutes :",time.minute)
print("seconds",time.second)
print("microseconds",time.microsecond)


d1 = dt.datetime(2022,4,5,12,5,55,666666)

print(d1)
print("date is:",d1.date())
print("time is:",d1.time())

dy1 = dt.datetime.now()
dy2 = dt.datetime(2023, 8,22 , 12,00,00,000000)

cal = dy2-dy1
print(cal)

cd = dt.datetime.now()

print(cd)

str_date = cd.strftime("%A %B %d, %Y")
print(str_date)
cd1 = "20 may ,2017"

print(cd1)

str_date = dt.datetime.strptime(cd1,"%d %B ,%Y")
print(str_date)