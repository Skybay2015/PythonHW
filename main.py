import math as m
import sys

# Федор Царенко Мит 11 5 вариант

a = float(input('Enter A: '))
b = float(input('Enter B: '))
c = float(input('Enter C: '))
x1 = float(input('Enter X1: '))
x2 = float(input('Enter X2: '))
step = float(input('Enter step: '))

if step <= 0:
    print("Step can't be less or equal 0")
    sys.exit()

elif x1 > x2:
    print("x1 can't be more than x2")
    sys.exit()

while x1 < x2:
    if c < 0 and b != 0:
        print('F =', round(a * m.pow(x1, 2) - m.pow(b, 2) * x1, 2), ' when x =', x1)

    elif c > 0 and b == 0:
        if x1 + c == 0:
            print('When x= ', x1, 'and c=', c, 'it makes an error')
            sys.exit()

        else:
            print('F =', round((x1+a)/(x1+c), 2), ' when x =', x1)

    else:
        if c == 0:
            print("C can't be equal 0")
            sys.exit()

        else:
            print('F =', round(x1/c, 2), ' when x =', x1)

    x1 = round(step + x1, 2)
