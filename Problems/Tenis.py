names = input().split()
n = int(input())
good = True

for i in range(n):
    good = True
    player1 = 0
    player2 = 0
    a = input().split()
    match1 = []
    match2 = []
    match3 = []
    if len(a) == 1:
        good = False
    elif len(a) == 4 or len(a) == 5:
        good = False
    else:
        if len(a) == 2:
            match1 = a[0].split(':')
            match1[0] = int(match1[0])
            match1[1] = int(match1[1])
            match2 = a[1].split(':')
            match2[0] = int(match2[0])
            match2[1] = int(match2[1])
        else:
            match1 = a[0].split(':')
            match1[0] = int(match1[0])
            match1[1] = int(match1[1])
            match2 = a[1].split(':')
            match2[0] = int(match2[0])
            match2[1] = int(match2[1])
            match3 = a[2].split(':')
            match3[0] = int(match3[0])
            match3[1] = int(match3[1])
        if match1[0] == 7:
            if match1[1] == 6 or match1[1] == 5:
                player1 += 1
            else:
                good = False
        elif match1[1] == 7:
            if match1[0] == 6 or match1[0] == 5:
                player2 += 1
            else:
                good = False
        elif match1[0] > 7 or match1[1] > 7:
            good = False
        elif match1[0] < 6 and match1[1] < 6:
            good = False
        elif match1[0] > match1[1]:
            player1 += 1
        elif match1[0] < match1[1]:
            player2 += 1
        else:
            good = False
        if match2[0] == 7:
            if match2[1] == 6 or match2[1] == 5:
                player1 += 1
            else:
                good = False
        elif match2[1] == 7:
            if match2[0] == 6 or match2[0] == 5:
                player2 += 1
            else:
                good = False
        elif match2[0] > 7 or match2[1] > 7:
            good = False
        elif match2[0] < 6 and match2[1] < 6:
            good = False
        elif match2[0] > match2[1]:
            player1 += 1
        elif match2[0] < match2[1]:
            player2 += 1
        else:
            good = False
        if player1 == player2:
            if len(a) == 3:
                if match3[0] == 6 and match3[1] < match3[0]:
                    if match3[1] > match3[0] - 2:
                        good = False
                elif match3[1] == 6 and match3[0] < match3[1]:
                    if match3[0] > match3[1] - 2:
                        good = False
                elif match3[0] > 6:
                    if match3[0] - match3[1] != 2:
                        good = False
                elif match3[1] > 6:
                    if match3[1] - match3[0] != 2:
                        good = False
                else:
                    good = False
            else:
                good = False
        elif len(a) > 2:
            good = False
        if names[0] == 'federer':
            if player2 > 0:
                good = False
        elif names[1] == 'federer':
            if player1 > 0:
                good = False
    if good:
        print("da")
    else:
        print("ne")
            
    
    
        
