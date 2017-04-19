coins = int(input())
first = int(input())
second = int(input())
third = int(input())
last = 3
timesPlayed = 0

while coins > 0:
    coins -= 1
    timesPlayed += 1
    if last == 3:
        last = 1
        if first % 35 == 0:
            coins += 35
        first += 1
    pass
    if last == 1:
        last = 2
        if second % 100 == 0:
            coins += 60
        second += 1
    pass
    if last == 2:
        last = 3
        if third % 10 == 0:
            coins += 9
        third += 1
    pass
print ('Martha plays ' + str(timesPlayed) + ' times before going broke.')
