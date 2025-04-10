from fractions import Fraction
import time as t
import math as m
def factorial(n):
  if n < 0:
    raise ValueError("Factorial is not defined for negative numbers")
  elif n == 0:
    return 1
  else:
    return n * factorial(n - 1)
def add2(a,b):
    return a + b
def sub2(a,b):
    return a - b
def mult2(a,b):
    return a * b
def div2(a,b):
    return a / b
def add3(a,b,c):
    return a + c
def sub3(a,b,c):
    return a  -  c
def mult3(a,b,c):
    return a * c
def div3(a,b,c):
    return a / c
def add4(a,b,c,d):
    return a + d
def sub4(a,b,c,d):
    return a  -  d
def mult4(a,b,c,d):
    return a * d
def div4(a,b,c,d):
    return a / d
def add5(a,b,c,d,e):
    return a+e
def sub5(a,b,c,d,e):
    return a-e
def mult5(a,b,c,d,e):
    return a*e
def div5(a,b,c,d,e):
    return a/e

result = -6.2123
repeat = 'yes'
print('Welcome to the code ninjas code calculator!')
def twonumprob():
    a = float(input('What is your first number: '))
    op = input('What oparation do you want to do: ')
    b = float(input('What is your second number: '))

    if op == '+':
        result = (add2(a,b))
        fracresult = Fraction(result).limit_denominator()
    elif op == '-':
        result = (sub2(a,b))
        fracresult = Fraction(result).limit_denominator()
    elif op == '*':
        result =(mult2(a,b))
        fracresult = Fraction(result).limit_denominator()
    elif op == '/':
        result = (div2(a,b))
        fracresult = Fraction(result).limit_denominator()
    else:
        print('Invalid input')
    return print(str(result) + ' and as a fraction ' + str(fracresult))
def threenumprob():
    a = float(input('What is your first number: '))
    op = input('what is your first oparator: ')
    b = float(input('What is your second number: '))
    optwo = input('what is your second oparatopr: ')
    c = float(input('what is your third number: '))
    if op == '+':
        a = (add2(a,b))
    elif op == '-':
        a = (sub2(a,b))
    elif op == '*':
        a = (mult2(a,b))
    elif op == '/':
        a = (div2(a,b))
    else:
        print('input invalid')
    if optwo == '+':
        result = (add3(a,b,c))
        fracresult = Fraction(result).limit_denominator()
    elif optwo == '-':
        result = (sub3(a,b,c))
        fracresult = Fraction(result).limit_denominator()
    elif optwo == '*':
        result = (mult3(a,b,c))
        fracresult = Fraction(result).limit_denominator()
    elif optwo == '/':
        result = (div3(a,b,c))
        fracresult = Fraction(result).limit_denominator()
    else:
        print('input invalid')
    return print(str(result) + ' and as a fraction ' + str(fracresult))
def fournumprob():
    a = float(input('What is your first number: '))
    op = input('what is your first oparator: ')
    b = float(input('What is your second number: '))
    optwo = input('what is your second oparatopr: ')
    c = float(input('what is your third number: '))
    opthree = input('what is your third oparator: ')
    d = float(input('what is your fourth number: '))
    if op == '+':
        a = (add2(a,b))
    elif op == '-':
        a = (sub2(a,b))
    elif op == '*':
        a = (mult2(a,b))
    elif op == '/':
        a = (div2(a,b))
    else:
        print('input invalid')
    if optwo == '+':
        a = (add3(a,b,c))
    elif optwo == '-':
        a = (sub3(a,b,c))
    elif optwo == '*':
        a = (mult3(a,b,c))
    elif optwo == '/':
        a = (div3(a,b,c))
    else:
        print('input invalid')
        fracresult = Fraction(result).limit_denominator()
    if opthree == '+':
        result = (add4(a,b,c,d))
        fracresult = Fraction(result).limit_denominator()
    elif opthree == '-':
        result = (sub4(a,b,c,d))
        fracresult = Fraction(result).limit_denominator()
    elif opthree == '*':
        result = (mult4(a,b,c,d))
        fracresult = Fraction(result).limit_denominator()
    elif opthree == '/':
        result = (div4(a,b,c,d))
        fracresult = Fraction(result).limit_denominator()
    return print(str(result) + ' and as a fraction ' + str(fracresult))
def fivenumprob():
    a = float(input('What is your first number: '))
    op = input('what is your first operator: ')
    b = float(input('What is your second number: '))
    optwo = input('what is your second operator: ')
    c = float(input('what is your third number: '))
    opthree = input('what is your third operator: ')
    d = float(input('what is your fourth number: '))
    opfour = input('what is your fourth operator: ')
    e = float(input('what is your fifth number: '))
    if op == '+':
        a = (add2(a,b))
    elif op == '-':
        a = (sub2(a,b))
    elif op == '*':
        a = (mult2(a,b))
    elif op == '/':
        a = (div2(a,b))
    else:
        print('input invalid')
    if optwo == '+':
        a = (add3(a,b,c))
    elif optwo == '-':
        a = (sub3(a,b,c))
    elif optwo == '*':
        a = (mult3(a,b,c))
    elif optwo == '/':
        a = (div3(a,b,c))
    else:
        print('input invalid')
    if opthree == '+':
        a = (add4(a,b,c,d))
    elif opthree == '-':
        a = (sub4(a,b,c,d))
    elif opthree == '*':
        a = (mult4(a,b,c,d))
    elif opthree == '/':
        a = (div4(a,b,c,d))
    else:
        print('input invalid')
    if opfour == '+':
        result = (add5(a,b,c,d,e))
        fracresult = Fraction(result).limit_denominator()
    elif opfour == '-':
        result = (sub5(a,b,c,d,e))
        fracresult = Fraction(result).limit_denominator()
    elif opfour == '*':
        result = (mult5(a,b,c,d,e))
        fracresult = Fraction(result).limit_denominator()
    elif opfour == '/':
        result = (div5(a,b,c,d,e))
        fracresult = Fraction(result).limit_denominator()
    else:
        print('input invalid')
    return print(str(result) + ' and as a fraction ' + str(fracresult))

repeat = 'yes'
while 'y' in repeat:
    numprob = input('How many numbers do you want in your problem ("extra" is an option): ') 
    if 'e' in numprob:
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
    if numprob == '2':
        twonumprob()
    if numprob == '3':
        threenumprob()
    if numprob == '4':
        fournumprob()
    if numprob == '5':
        fivenumprob()
    repeat = input('Do you want to do another problem (yes or no): ')
print('Goodbye!') 
