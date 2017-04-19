from math import floor

n = int(input())
time = 1200
fav = 0

if n > 720:
    passed = floor(n/720) * 31
    fav += passed
    n = n - floor(n/720) * 720
    for i in range(n):
        time = time + 1
        if time >= 1000:
            time = [int(i) for i in str(time)]
            if time[3] == 10:
                time[2] = time[2] + 1
                time[3] = 0
            if time[2] == 6:
                time[1] = time[1] + 1
                time[2] = 0
            if time[1] == 10:
                time[0] = time[0] + 1
                time[1] = 0
            if (time[0] - time[1]) == (time[1] - time[2]) and (time[1] - time[2]) == (time[2] - time[3]):
                fav = fav + 1
            time = int(''.join(map(str,time)))
        elif time < 1000:
            time = [int(i) for i in str(time)]
            if time [2] == 10:
                time[1] = time[1] + 1
                time[2] = 0
            if time[1] == 6:
                time[0] = time[0] + 1
                time[1] = 0
            if (time[0] - time[1]) == (time[1] - time[2]):
                fav = fav + 1
            time = int(''.join(map(str,time)))
        if time == 1300:
            time = 100
else:   
    for i in range(n):
        time = time + 1
        if time >= 1000:
            time = [int(i) for i in str(time)]
            if time[3] == 10:
                time[2] = time[2] + 1
                time[3] = 0
            if time[2] == 6:
                time[1] = time[1] + 1
                time[2] = 0
            if time[1] == 10:
                time[0] = time[0] + 1
                time[1] = 0
            if (time[0] - time[1]) == (time[1] - time[2]) and (time[1] - time[2]) == (time[2] - time[3]):
                fav = fav + 1
            time = int(''.join(map(str,time)))
        elif time < 1000:
            time = [int(i) for i in str(time)]
            if time [2] == 10:
                time[1] = time[1] + 1
                time[2] = 0
            if time[1] == 6:
                time[0] = time[0] + 1
                time[1] = 0
            if (time[0] - time[1]) == (time[1] - time[2]):
                fav = fav + 1
            time = int(''.join(map(str,time)))
        if time == 1300:
            time = 100
print(fav)
