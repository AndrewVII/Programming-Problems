n = int(input())
m = int(input())
x = 2
numbers = [n, m]

for i in range(99999999999999):
    if numbers[i + 1] <= numbers[i]:
        numbers.append(numbers[i] - numbers[i + 1])
        x += 1
    else:
        break
print(x)
        

