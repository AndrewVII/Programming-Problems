import datetime

a = input()
x = 1
a = a.split(':')

a = datetime.datetime(100, 1, 1, int(a[0]), int(a[1]))

for i in range(120):
    if (a.time() >= datetime.time(7,0) and a.time() < datetime.time(10,0)) or (a.time() >= datetime.time(15,0) and a.time() < datetime.time(19,0)):
        a += datetime.timedelta(minutes = 2)
    else:
        a += datetime.timedelta(minutes = 1)
print(str(a.time())[:5])
