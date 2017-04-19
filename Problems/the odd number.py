numbs = []
num = 0
for i in range(int(input())):
    numbs.append(int(input()))

for i, x in enumerate(numbs):
    if numbs.count(x) & 1 == 1:
        print(x)
        break
