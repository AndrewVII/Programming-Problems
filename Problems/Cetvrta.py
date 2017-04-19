from collections import Counter

a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]

x = [a[0],b[0],c[0]]
y = [a[1],b[1],c[1]]

times = Counter(x)
times2 = Counter(y)

xval = 0
yval = 0

for i in range(3):
    if times[x[i]] == 1:
        xval = x[i]
for i in range(3):
    if times2[y[i]] == 1:
        yval = y[i]
print(xval, yval)
