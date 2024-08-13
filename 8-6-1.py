from datetime import datetime
now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dum_day= datetime(2019, 5, 1, hour=15, minute=15, second=15,microsecond=0)
print(dum_day)

#変に空白を避けないように注意↓　
print(dt2)
dt = datetime.strptime("21/11/2006 16:30", "%d/%m/%Y %H:%M")
print(dt)

dt2=dt.strftime("%Y年%m月%d日 %H時M分")
print(dt2)
