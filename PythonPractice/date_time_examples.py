import datetime

d = datetime.datetime(1994,12,25,7,30,55)
print(d)
print(d.date())
print(d.time())
print(d.year)
print(d.month)
print(d.day)
print(d.hour)
print(d.minute)
print(d.second)

# Date Format Codes - https://www.w3schools.com/python/python_datetime.asp
print(d.strftime("%dth %B,%Y"))  # 25th December,1994

today = datetime.datetime.now()
print(today.strftime("%d-%b-%Y"))  # Today
