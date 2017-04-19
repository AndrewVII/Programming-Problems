from fractions import Fraction

n = int(input())
d = int(input())

if(n%d == 0):
    print(int(n/d))
elif n%d != 0 and int(n/d) > 0:
    num1 = int(n/d)
    num2 = n - (num1*d)
    num2 = Fraction(num2,d)
    print(num1, num2)
else:
    num2 = n
    num2 = Fraction(num2,d)
    print(num2)
