t = int(input())
c = int(input())
times = []
total = 0
amount = 0

for i in range(c):
    a = int(input())
    times.append(a)

times.sort()

for i in range(c):
    if(total + times[i]) <= t:
        total += times[i]
        amount += 1
    else:
        break
print(amount)
