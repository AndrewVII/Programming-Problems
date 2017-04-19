a = set()
strings = []

for i in range(int(input())):
    b = input()
    if b in a and b not in strings:
        strings.append(b)
    a.add(b)

print(len(a) - len(strings))
