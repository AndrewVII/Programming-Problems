for i in range(10):
    n = int(input())
    room = []
    treasures = 0
    keys = 0
    nums = '123456789'
    for i in range(n):
        a = list(input())
        if 'S' in a:
            start = (i, a.index('S'))
        room.append(a)
    visited = [[False for i in range(n)] for i in range(n)]
    s = [start]
    doors = []
    while len(s) > 0:
        current = s.pop(0)
        x, y = current
        using = room[x][y]
        if not visited[x][y]:
            if room[x][y] == 'K':
                keys += 1
            elif room[x][y] == 'T':
                treasures += 1
            if x - 1 >= 0:
                if room[x-1][y] in nums:
                    if int(room[x-1][y]) <= keys:
                        s.append((x-1,y))
                    else:
                        doors.append((x-1,y))
                elif room[x-1][y] != '#':
                    s.append((x-1,y))
            if x + 1 < n:
                if room[x+1][y] in nums:
                    if int(room[x+1][y]) <= keys:
                        s.append((x+1,y))
                    else:
                        doors.append((x+1,y))
                elif room[x+1][y] != '#':
                    s.append((x+1,y))
            if y - 1 >= 0:
                if room[x][y-1] in nums:
                    if int(room[x][y-1]) <= keys:
                        s.append((x,y-1))
                    else:
                        doors.append((x,y-1))
                elif room[x][y-1] != '#':
                    s.append((x,y-1))
            if y + 1 < n:
                if room[x][y+1] in nums:
                    if int(room[x][y+1]) <= keys:
                        s.append((x,y+1))
                    else:
                        doors.append((x,y+1))
                elif room[x][y+1] != '#':
                    s.append((x,y+1))
            visited[x][y] = True
        for l in doors:
            o,p = l
            if keys >= int(room[o][p]):
                s.append((o,p))
                doors.remove(l)
    print(treasures)
