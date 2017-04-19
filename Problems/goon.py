n = input()

n = list(map(int, n.split('-')))

first = [int(i) for i in str(n[0])]
second = [int(i) for i in str(n[1])]
third = [int(i) for i in str(n[2])]


if sum(first) == sum(second) == sum(third):
    print('Goony!')
else:
    print('Pick up the phone!')
