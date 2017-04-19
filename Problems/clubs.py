n = int(input())
clubs = []
for i in range(int(input())):
    clubs.append(int(input()))
    clubs.sort()
    clubs.reverse()
def findmin(d,s):
    if d == n:
        return s
    else:
        return min([findmin(i+d,s+1) for i in clubs])
