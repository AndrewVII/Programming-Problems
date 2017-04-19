from math import ceil

a = int(input())
b = [int(i) for i in input().split()]
c = []

b.sort()

mid = int(ceil(len(b)/2) - 1)

for i in range(int(len(b)/2)+1):
    if i == 0:
        c.append(b[mid])
    else:
        c.append(b[mid+i])
        c.append(b[mid-i])

if len(c) > len(b):
    c.pop(-1)

c = map(str, c)
c = ' '.join(c)
print(c)
