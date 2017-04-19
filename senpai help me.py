n = int(input())
lowest = 9999999

for i in range (1, int(n ** (1/2) + 1)):
    b = n/i
    if b % 1 == 0:
        if 2*b + 2*i < lowest:
            lowest = 2*b + 2*i
print(int(lowest))
