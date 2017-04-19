from collections import deque

n = int(input())
a = list(map(int,(input())))
sandwich = deque()

for i in range(n):
    if a[i] == 0:
        sandwich.append(i+1)
    else:
        sandwich.appendleft(i+1)
for i in range(len(sandwich)):
    print(sandwich[i])
