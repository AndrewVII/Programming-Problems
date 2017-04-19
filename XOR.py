for i in range(int(input())):
    a,b = map(int, input().split())
    x = int(a)
    for i in range(a+1,b+1):
        x = x ^ i
    print(x)
