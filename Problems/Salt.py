from collections import Counter
n, q = map(int, input().split())
xVals = []
yVals = []
coords = set()
for i in range(n):
    x, y = map(int, input().split())
    if (x,y) in coords:
        pass
    else:
        xVals.append(x)
        yVals.append(y)
        coords.add((x,y))
xVals = Counter(xVals)
yVals = Counter(yVals)
for i in range(q):
    j,k,l = input().split()
    if int(j) == 1:
        if (int(k),int(l)) in coords:
            print('salty')
        else:
            print('bland')
    else:
        if k == 'X':
            print(xVals[int(l)])
        else:
            print(yVals[int(l)])
