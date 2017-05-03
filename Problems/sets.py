n = int(input())
vals = {i: [] for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
names = set()
for i in range(n):
    a = list(map(str, input().split(' contains ')))
    vals[a[0]].append(a[1])
    names.add(a[0])
    if a[1].isupper():
        names.add(a[1])
final = {}
for i in names:
    visited = {i: False for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    final[i] = set()
    s = [i]
    while len(s) > 0:
        current = s.pop(0)
        for x in vals[current]:
            if x in vals:
                if not visited[x]:
                    s.append(x)
                    visited[x] = True
                else:
                    pass
            else:
                final[i].add(x)
finals = {}
order = []
for i in final:
    finals[i] = []
    order.append(i)
    while len(final[i]) > 0:
        a = min(final[i])
        finals[i].append(a)
        final[i].remove(a)
order.sort()
for i in order:
    print(i,'=','{'+','.join(finals[i])+'}')
