from collections import Counter

n = input()
a = input()

first = Counter(n)
second = Counter(a)
stored = []

good = True

for i in range(len(n)):
    if n[i] in stored:
        pass
    elif first[n[i]] != second[n[i]]:
        if second['*'] > 0:
            second['*'] -= (first[n[i]] - second[n[i]])
        else:
            good = False
            break
        stored.append(n[i])
             
if good:
    print('A')
else:
    print('N')
    
