from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
li = deque()
ids = {}

for i in range(n):
    a = input().split( )
    if a[0] != 'R':
        ids[a[1]] = i
        if a[0] == 'F':
            li.appendleft([a[1],i])
        else:
            li.append([a[1],i])
    elif a[0] == 'R':
        ids[a[1]] = -1
    
for i in li:
    if ids[i[0]] == i[1]:
        print(i[0])
