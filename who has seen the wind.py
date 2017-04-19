h = int(input())
m = int(input())
t = 0

while ((-6*(t**3))+(h*(t**2))+(2*t)+1) > 0:
    t += 1
if t > m:
    print("The balloon does not touch ground in the given time.")
else:
    print("The balloon first touches ground at hour:")
    print(t)
