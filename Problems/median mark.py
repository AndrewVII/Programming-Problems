n = int(input())
a = []
for i in range(n):
    p = int(input())
    a.append(p)
a.sort()
if n % 2 == 0:
    b = int(len(a)/2)
    x = (a[b] + a[b-1])/2
    if x % 0.5 == 0 and x % 1 != 0:
        print(int(x+1))
    else:
        print(int(x))
else:
    print(a[int(n/2)])

