import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("2024/8/13", "%Y/%m/%d")
print(dt + t_delta)
