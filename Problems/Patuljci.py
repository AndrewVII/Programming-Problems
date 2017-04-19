dwarves = []
dwarves8 = []
dwarves7 = []
current = []

for i in range (9):
    dwarves.append(int(input()))
print(dwarves)

for i in range(9):
    current = dwarves[0:10]
    current.pop(i)
    dwarves8.append(current)
    print(dwarves)

for i in range(9):
    for ii in range(7):
        current2 = dwarves8[i][0:10]
        current2.remove(current2[ii])
        dwarves7.append(current2)

for i in range(len(dwarves7)):
    if sum(dwarves7[i]) == 100:
        correct = dwarves7[i]

for i in range(7):
    print(correct[i])

