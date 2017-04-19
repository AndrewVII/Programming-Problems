players = {}
number = int(input())

for i in range(number):
    a,b = map(str, input().split())
    players[a] = int(b)

days = int(input())

for i in range(days*number):
    a,b = map(str, input().split())
    players[a] += int(b)

y = list(players.values())

y.sort()

n = int(input())

out = y[len(y)-n]

print({v:k for k, v in players.items()}[out])


