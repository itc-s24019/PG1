from datetime import date

day_now = date.today()
print(day_now)

xday = date(2006, 2,21)
td = day_now - xday
print(td)
