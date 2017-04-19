n = int(input())
a = input()
current = 0
unknown = False

a = list(map(int, a.split()))

b = a.index(min(a))
c = a.index(max(a))

for i in range(b,c):
    if a[i] > current:
        current = a[i]
    else:
        unknown = True
        break
if not unknown and c > b:
    print(a[c]-a[b])
else:
    print("unkown")
