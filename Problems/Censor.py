n = int(input())

for i in range(n):
    a = input().split( )
    for i in range(len(a)):
        if len(a[i]) == 4:
            a[i] = '****'
    a = ' '.join(a)
    print(a)
