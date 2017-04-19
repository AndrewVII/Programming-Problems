n = input()
n = [int(i) for i in n.split()]
v = 0
x = 0
y = 0

while v == 0:
    a = input()
    a = [int(i) for i in a.split()]
    if a[0] == 0 and a[1] == 0:
        v = 1
    else:
        if (x + a[0] >= 0 and x + a[0] <= n[0]):
            x += a[0]
        elif x + a[0] < 0:
            x = 0
        elif x + a[0] > n[0]:
            x = n[0]
        if (y + a[1] >= 0 and y + a[1] <= n[1]):
            y += a[1]
        elif y + a[1] < 0:
            y = 0
        elif y + a[1] > n[1]:
            y = n[1]
        print(x, y)
