n = int(input())
word = input()
maxlen = 0
starting = 0
for i in range(1,n):
    if i+1 < n:
        if word[i-1] == word[i+1]:
            curlen = 1
            ii = 1
            for ii in range(1,i+1):
                try:
                    x = word[i-ii]
                    y = word[i+ii]
                except:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
                if x == y:
                    curlen += 2
                else:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
                if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
        elif word[i] == word[i-1]:
            curlen = 2
            ii = 1
            for ii in range(1,i+1):
                try:
                    j = word[i+ii]
                    k = word[i-ii-1]
                except:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
                if j == k:
                    curlen += 2
                    
                else:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
            if curlen > maxlen:
                    maxlen = curlen
                    starting = i - ii
    else:
        if word[i] == word[i-1]:
            curlen = 2
            ii = 1
            for ii in range(1,i+1):
                try:
                    j = word[i+ii]
                    k = word[i-ii-1]
                except:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
                if j == k:
                    curlen += 2
                    
                else:
                    if curlen > maxlen:
                        maxlen = curlen
                        starting = i - ii
                        break
                    else:
                        break
            if curlen > maxlen:
                    maxlen = curlen
                    starting = i - ii
print(word[starting:starting+maxlen])
print(maxlen)