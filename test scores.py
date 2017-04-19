n = [int(i) for i in input().split()]
b = n[1]

a = [int(input()) for i in range(n[0])]
values = [i for i in a if i > 0]

values.sort()

if b >= len(values):
    print(sum(values))
else:
    print(sum(values[len(values)-b:]))
