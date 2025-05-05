from fractions import Fraction
import time as t
import math as m
import re
from collections import Counter
extrarepeat= {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,}
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

timesrepeated = 0

ans=0
repeat = 'yes'
while 'y' in repeat:

    numprob = input('Do you want to evaluate an expression or do extra functions (This is case sensitive): ')
    numprob = numprob.lower()

    if 'extra' in numprob:
        maththing = int(input('1 for Decimal to Fraction\n2 for Fraction to decimal\n3 for factorial\n4 for a fibonacci sequence\n5 for exponents\n6 for a percent of a number\n7 for the pythagorean theorem\n8 for  E=MC^2\n9 for binary converter\n10 for percent chance in words\n11 for unit conversion\n12 for Unit Rate\n13 for Center of Middle\nEnter your decision: '))
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
            extrarepeat[6] += 1
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

            convirsion = int(input('1 for binary to intager\n2 for intager to binary\nEnter your dicision: '))
            if convirsion == 1:
                start = input('What is your binary string: ')
                ans = int(start, 2)
                print(str(start)+' in intager form is '+str(ans))
            else:
                start = int(input('What number do you want in binary: '))
                ans = bin(start)
                ans = ans[2:]
                print('Your number in binary is ' + str(ans))
        elif maththing == 10:
            decimal = float(input('What is the percent as a decimal: '))
            decimal = decimal / 100
            percent = Fraction(decimal).limit_denominator()
            print(str(percent.numerator) + ' in ' + str(percent.denominator))
        elif maththing == 11:

            type = int(input('1 for lenth\n2 for weight/mass\n3 for tempature\nEnter your decision: '))
            if type == 1:
                convirsion = int(input('1 for customary to metric\n2 for metric to customary\nEnter your decision: '))
                if convirsion == 1 :
                    inches = float(input('How many inches: '))
                    cm = inches*2.54
                    print(str(inches) + ' in is ' + str(cm) + ' cm')
                else:
                    cm = float(input('How many centameters: '))
                    inches  = cm/2.54
                    print(str(cm)+' cm is ' +str(inches)+' in')
            elif type == 2:
                convirsion = int(input('1 for customary to metric\n2 for metric to customary\nEnter your decision: '))
                if convirsion == 1:
                    lbs = float(input('How many pounds: '))
                    kg = lbs/2.20462
                    print(str(lbs)+' pound(s) is '+str(kg)+' kilogram(s)')
                else:
                    g = float(input('How many grams: '))
                    lbs = g/453.592
                    print(str(g)+ ' gram(s) is '+str(lbs)+' pound(s)')
            elif type == 3:
                convirsion = int(input('1 for °F to °C\n2 for °C to °F\nEnter your decision: '))
                if convirsion ==1:
                    f = float(input('How many °F: '))
                    c = (f - 32)*(5/9)
                    print(str(f)+'° F is '+str(c)+'° C')
                else:
                    c = float(input('How many °C: '))
                    f = (c*1.8)+32
                    print(str(c)+'°C is ' +str(f)+'° F')
        elif maththing == 12:
            #y=kx

            known = int(input('What do you know\n1 k and y\n2 k and x\n3 y and x\nEnter your decision: '))
            if known == 1:
                k = float(input('What is k: '))
                y = float(input('What is y: '))
                x = y/k
                print('x = ' + str(x))
            elif known == 2:
                k = float(input('What is k: '))
                x = float(input('What is x: '))
                y = k*x
                print('y = '+str(y))
            elif known == 3:
                y = float(input('What is y: '))
                x = float(input('What is x: '))
                k = y/x
                print('k = '+str(k))
        elif maththing == 13:
            
            type = int(input('What center of middle do you want to use\n1 mean\n2 median\n3 mode\nEnter your decision: '))
            if type == 1:
                i = int(input('How many intagers are in your data set: '))
                e = 1
                ifi = i
                dataset = {}
                add = 0
                while i > 0:

                    intagersa = float(input('What is the intager: '))
                    dataset[str(e)] = intagersa
                    add += intagersa
                    i = i - 1
                    e = e + 1
                print(dataset)
                mean = add/ifi
                print('The mean of your data set is '+str(mean))
            elif type == 2:
                aod = int(input('How many data points are in your data set: '))
                i = aod
                e = 1
                data = {}
                if aod % 2 == 0:
                    lowmid = aod/2
                    lowmid = m.floor(lowmid)
                    highmid = aod/2
                    highmid += 1
                    while i > 0:
                        data[e] = float(input('What is your data point (from lowest to highest): '))
                        i -= 1
                        e += 1
                    highmid = data[highmid]
                    lowmid = data[lowmid]
                    mid = (highmid + lowmid)/2
                    print(mid)
#C10H15N
                elif aod % 2 != 0:
                    mid = aod/2
                    mid = m.ceil(mid)
                    while i > 0:
                        data[e] = float(input('What is your data point (from lowest to highest): '))
                        i -= 1
                        e += 1
                    print(data[mid])
            elif type == 3:
                i = int(input('How many numbers are in your data set: '))
                data = {}
                for e in range(1, i + 1):
                    intager = float(input('What is your data point: '))
                    data[e] = intager
                    print(dataset)

                data_values = list(dataset.values())
                value_counts = Counter(data_values)
                most_common = value_counts.most_common()

                print('Value Counts:', value_counts)
                print('Most Common (value, frequency):', most_common)

                if most_common:
                    max_frequency = most_common[0][1]
                    modes = [value for value, frequency in most_common if frequency == max_frequency]

                    if len(modes) == 1:
                        print('The mode of your data set is:', modes[0])
                    else:
                        print('The modes of your data set are:', modes)
                else:
                    print('No data to calculate the mode.')
            else:
                print('Invalid input')


    elif 'evaluate' in numprob:
        problem = input("Enter your expression: ")
        result = evaluate_expression(problem)
        ans = result
        print(f"{problem} = {result}")
    elif 'corn' in numprob:
        print('"Your that type of guy" - Jack Ford')
    elif 'will' in numprob:
        print('Midget')
    elif 'jack' in numprob:
        print('C10H15N')
    
    repeat = input('Do you want to do another problem (yes or no): ')
    if 'y' in repeat:
        timesrepeated+=1
statyn = input('Do you want to see your stats: ')
if 'y' in statyn:
    print('You have repeated the calculator '+str(timesrepeated)+' time(s)')
    print('You have done each extra feature (feature:times)')
    print(extrarepeat)
print('Goodbye!')
