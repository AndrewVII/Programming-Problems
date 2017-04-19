import sys
sys.setrecursionlimit(9999999999)

def fact(x):
    if x < 1:
        return 1
    else:
        return x * fact(x - 1)
for i in range(int(input())):
    print(fact(int(input())) % 2**(32))

