import datetime
date = datetime.datetime.now()
print(date)
print(date.date())
print(date.strftime("%d-%m-%y %H:%M:%S"))
print(date.time())
print(date.year)
print(date.month)
print(date.day)
print(date.weekday())
print(date.hour)
print(date.minute)
print(date.second)
print(date.microsecond)

print('.........................calculate date time........................')

date1 = datetime.datetime(2025, 2, 5)
date2 = datetime.datetime(2024, 2, 3)
print(date1-date2)          # subtraction time
print(date1+datetime.timedelta(days = 10))   # additation time
