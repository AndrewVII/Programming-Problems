a = 0
b = -1
for i in range(int(input())):
    a += 1
    b += 2
    if a % 7 == 0 and a % 13 != 0:
        c = 'Fizz'
    elif a % 13 == 0 and a % 7 != 0:
        c = 'Fuzz'
    elif a % 7 == 0 and a % 13 == 0:
        c = 'Fizz Fuzz'
    else:
        c = int(a)
    if b % 7 == 0 and b % 13 != 0:
        d = 'Fizz'
    elif b % 13 == 0 and b % 7 != 0:
        d = 'Fuzz'
    elif b % 7 == 0 and b % 13 == 0:
        d = 'Fizz Fuzz'
    else:
        d = int(b)
    print(c, d)
