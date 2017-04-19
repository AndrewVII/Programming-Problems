n,d = (list(map(int, input().split())))
a = [int(i) for i in input().split()]
highest = 999999999999
good = False

for i, x in enumerate(a):
    if d % x == 0:
        if abs(d/x) < highest:
            highest = int(abs(d/x))
            good = True

if good:
    print(highest)
else:
    print('This is not the best time for a trip.')

