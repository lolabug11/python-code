from fractions import Fraction
import time as t
import math as m
import re
ans = 0
def is_valid_expression(expr):
        #Allow digits, operators, and whitespace
    return bool(re.fullmatch(r'[\d+\-*/ ().ans]+|\*\*', expr))

def evaluate_expression(expr):
    if not is_valid_expression(expr):
        raise ValueError("Invalid expression: contains illegal characters.")
    try:
        # Use eval carefully after validation
        return eval(expr)
    except Exception as e:
        raise ValueError(f"Error evaluating expression: {e}")
def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)



ans=0
repeat = 'yes'
while 'y' in repeat:

    numprob = input('Do you want to evaluate an expression or do extra functions (This is case sensitive): ') 
    if 'extra' in numprob:
        maththing = int(input('Do you want to turn a decimal into a Fraction, a Fraction to a decimal, a factorial, a set amount of the fibonacci sequence, exponents, a percent of a number,  the pythagorean theorem, finding the energy of an obgect, converting an intager to binary, or converting a percent to words'
        ' (1 for Decimal to Fraction, 2 for Fraction to decimal, 3 for factorial, 4 for a fibonacci sequence, 5 for exponents, 6 for a percent of a number,7 for the pythagorean theorem, 8 for  E=MC^2, 9 for binary converter, 10 for percent chance in words): '))
        if maththing == 1:
            decimal = float(input('What decimal do you want to into a Fraction: '))
            frac = Fraction(decimal).limit_denominator()
            print(frac)
        elif maththing == 2: 
            numarator = int(input("What is your numarator: "))
            demominator = int(input('What is your demominator: '))
            print(numarator/demominator)
        elif maththing == 3:
            n = int(input('What number do you want factorial: '))
            a = factorial(n)
            print(a)
        elif maththing == 4:
            a = 1
            b = 1
            c = int(input("How many numbers do you want: "))
            print('')
            while c > 0:
                if c % 2 != 0:
                    a = a+b
                    c = c - 1
                    print(a)
                    t.sleep(0.25)
                    if c > 1:
                        b = a + b
                        c = c - 1
                        print(b)
                        t.sleep(0.25)
                    else:
                        break
                else:
                    a = a+b
                    print(a)
                    c = c - 1
                    t.sleep(0.25)
                    b = a + b
                    print(b)
                    t.sleep(0.25)
                    c = c - 1
                    
            print('Done')

        elif maththing == 5:
            base = float(input('What number do you want as your base: '))
            power = int(input('What power do you want to use: '))
            result = base**power
            fracresult = Fraction(result).limit_denominator()
            print(str(result) + ' and as a fraction ' + str(fracresult))
        elif maththing == 6:
            mainnum= float(input('What number do want a percent of: '))
            percentage = int(input('What percent of the number above do you want: '))
            percentage = percentage / 100
            Answer = mainnum * percentage
            print('Your answer is ' + str(Answer))
        elif maththing == 7:
            a = float(input('What is the first side of the right triangle: '))
            b = float(input('What is the second side of the right triange: '))
            a = a**2
            b =  b**2
            c = a+b
            c = m.sqrt(c)
            print('The hypotonuce of your right triange is ' + str(c) )
        elif maththing == 8:
            mass = int(input('What is the mass of your object in grams: '))
            c = 89875517873681760
            e = mass*c
            frace = Fraction(e).limit_denominator()
            print('Your object has the energy (in J) of ' + str(e) + ' or as a fraction ' + str(frace))
        elif maththing == 9:
            start = int(input('What number do you want in binary: '))
            ans = bin(start)
            ans = ans[2:]
            print('Your number in binary is ' + str(ans))
        elif maththing == 10:
            decimal = float(input('What is the percent as a decimal: '))
            decimal = decimal / 100
            percent = Fraction(decimal).limit_denominator()
            print(str(percent.numerator) + ' in ' + str(percent.denominator))


    # if numprob == '2':
    #     twonumprob()
    # if numprob == '3':
    #     threenumprob()
    # if numprob == '4':
    #     fournumprob()
    # if numprob == '5':
    #     fivenumprob()
    elif 'evaluate' in numprob:
        problem = input("Enter your expression: ")
        result = evaluate_expression(problem)
        ans = result
        print(f"{problem} = {result}")

    repeat = input('Do you want to do another problem (yes or no): ')
print('Goodbye!') 
