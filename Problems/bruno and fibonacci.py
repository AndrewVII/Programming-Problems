fibonacci_cache = {}
values = []
values2 = []
good = True

def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n == 1 or n == 2:
        value = 1
    else:
        value = fibonacci(n - 1) + fibonacci(n - 2)
    fibonacci_cache[n] = value
    return value

a = int(input())
b = list(input())
fibonacci(a)

for i in range(1,a):
    if fibonacci_cache[i] <= a:
        values.append(fibonacci_cache[i])
    else:
        break
for i in range(1,a):
    if i not in values:
        values2.append(i)
for i in range(len(values)):
    if b[values[i]-1] != 'A':
        good = False
        break
for i in range(len(values2)):
    if b[values2[i]-1] == 'A':
        good = False
        break

if good:
    print("That's quite the observation!")
else:
    print("Bruno, GO TO SLEEP")


