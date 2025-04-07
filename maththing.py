from fractions import Fraction
import time
def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)
maththing = int(input('Do you want to turn a decimal into a Fraction or a Fraction to a decimal or an factorial (1 for Decimal to Fraction, 2 for Fraction to decimal, 3 for factorial, 4 for a fibinachy sequence): '))
if maththing == 2:
    frac = float(input('What decimal do you want to into a Fraction'))
    frac = Fraction(frac).limit_denominator()
    print(frac)
elif maththing == 1: 
    numarator = int(input("What is your numarator"))
    demominator = int(input('What is your demominator'))
    print(numarator/demominator)
elif maththing == 3:
    n = int(input('What number do you want factorial: '))
    a = factorial(n)
    print(a)
elif maththing == 4:
    a = 1
    b = 1
    c = int(input("How many numbers do you want (Even Numbers Only): "))
    print('')
    while c > 0:
        a = a+b
        print(a)
        c = c - 1
        time.sleep(0.5)
        b = a + b
        print(b)
        time.sleep(0.5)
        c = c - 1
    print('Done')
