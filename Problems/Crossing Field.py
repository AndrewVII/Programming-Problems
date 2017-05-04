import sys
input = sys.stdin.readline

n, h = map(int, input().split())
field = []
good = False
for i in range(n):
    a = list(map(int, input().split()))
    field.append(a)
visited = [[False for i in range(n)] for i in range(n)]
s = [(0,0)]
while len(s) > 0:
    current = s.pop()
    if current == (n-1, n-1):
        print('yes')
        good = True
        break
    x, y = current
    using = field[x][y]
    if not visited[x][y]:
        if x-1 > 0:
            if abs(field[x-1][y] - using) <= h:
                s.append((x-1, y))
                visited[x][y] = True
        if y-1 > 0:
            if abs(field[x][y-1] - using) <= h:
                s.append((x, y-1))
                visited[x][y] = True
        if x+1 < n:
            if abs(field[x+1][y] - using) <= h:
                s.append((x+1, y))
                visited[x][y] = True
        if y+1 < n:
            if abs(field[x][y+1] - using) <= h:
                s.append((x, y+1))
                visited[x][y] = True
if not good:
    print('no')
