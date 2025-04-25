# def add2(a,b):
#     return a + b
# def sub2(a,b):
#     return a - b
# def mult2(a,b):
#     return a * b
# def div2(a,b):
#     return a / b
# def add3(a,b,c):
#     return a + c
# def sub3(a,b,c):
#     return a  -  c
# def mult3(a,b,c):
#     return a * c
# def div3(a,b,c):
#     return a / c
# def add4(a,b,c,d):
#     return a + d
# def sub4(a,b,c,d):
#     return a  -  d
# def mult4(a,b,c,d):
#     return a * d
# def div4(a,b,c,d):
#     return a / d
# def add5(a,b,c,d,e):
#     return a+e
# def sub5(a,b,c,d,e):
#     return a-e
# def mult5(a,b,c,d,e):
#     return a*e
# def div5(a,b,c,d,e):
#     return a/e

# result = -6.2123
# repeat = 'yes'
# print('Welcome to the code ninjas code calculator!')
# def twonumprob():
#     a = float(input('What is your first number: '))
#     op = input('What oparation do you want to do: ')
#     b = float(input('What is your second number: '))

#     if op == '+':
#         result = (add2(a,b))
#         fracresult = Fraction(result).limit_denominator()
#     elif op == '-':
#         result = (sub2(a,b))
#         fracresult = Fraction(result).limit_denominator()
#     elif op == '*':
#         result =(mult2(a,b))
#         fracresult = Fraction(result).limit_denominator()
#     elif op == '/':
#         result = (div2(a,b))
#         fracresult = Fraction(result).limit_denominator()
#     else:
#         print('Invalid input')
#     return print(str(result) + ' and as a fraction ' + str(fracresult))
# def threenumprob():
#     a = float(input('What is your first number: '))
#     op = input('what is your first oparator: ')
#     b = float(input('What is your second number: '))
#     optwo = input('what is your second oparatopr: ')
#     c = float(input('what is your third number: '))
#     if op == '+':
#         a = (add2(a,b))
#     elif op == '-':
#         a = (sub2(a,b))
#     elif op == '*':
#         a = (mult2(a,b))
#     elif op == '/':
#         a = (div2(a,b))
#     else:
#         print('input invalid')
#     if optwo == '+':
#         result = (add3(a,b,c))
#         fracresult = Fraction(result).limit_denominator()
#     elif optwo == '-':
#         result = (sub3(a,b,c))
#         fracresult = Fraction(result).limit_denominator()
#     elif optwo == '*':
#         result = (mult3(a,b,c))
#         fracresult = Fraction(result).limit_denominator()
#     elif optwo == '/':
#         result = (div3(a,b,c))
#         fracresult = Fraction(result).limit_denominator()
#     else:
#         print('input invalid')
#     return print(str(result) + ' and as a fraction ' + str(fracresult))
# def fournumprob():
#     a = float(input('What is your first number: '))
#     op = input('what is your first oparator: ')
#     b = float(input('What is your second number: '))
#     optwo = input('what is your second oparatopr: ')
#     c = float(input('what is your third number: '))
#     opthree = input('what is your third oparator: ')
#     d = float(input('what is your fourth number: '))
#     if op == '+':
#         a = (add2(a,b))
#     elif op == '-':
#         a = (sub2(a,b))
#     elif op == '*':
#         a = (mult2(a,b))
#     elif op == '/':
#         a = (div2(a,b))
#     else:
#         print('input invalid')
#     if optwo == '+':
#         a = (add3(a,b,c))
#     elif optwo == '-':
#         a = (sub3(a,b,c))
#     elif optwo == '*':
#         a = (mult3(a,b,c))
#     elif optwo == '/':
#         a = (div3(a,b,c))
#     else:
#         print('input invalid')
#         fracresult = Fraction(result).limit_denominator()
#     if opthree == '+':
#         result = (add4(a,b,c,d))
#         fracresult = Fraction(result).limit_denominator()
#     elif opthree == '-':
#         result = (sub4(a,b,c,d))
#         fracresult = Fraction(result).limit_denominator()
#     elif opthree == '*':
#         result = (mult4(a,b,c,d))
#         fracresult = Fraction(result).limit_denominator()
#     elif opthree == '/':
#         result = (div4(a,b,c,d))
#         fracresult = Fraction(result).limit_denominator()
#     return print(str(result) + ' and as a fraction ' + str(fracresult))
# def fivenumprob():
#     a = float(input('What is your first number: '))
#     op = input('what is your first operator: ')
#     b = float(input('What is your second number: '))
#     optwo = input('what is your second operator: ')
#     c = float(input('what is your third number: '))
#     opthree = input('what is your third operator: ')
#     d = float(input('what is your fourth number: '))
#     opfour = input('what is your fourth operator: ')
#     e = float(input('what is your fifth number: '))
#     if op == '+':
#         a = (add2(a,b))
#     elif op == '-':
#         a = (sub2(a,b))
#     elif op == '*':
#         a = (mult2(a,b))
#     elif op == '/':
#         a = (div2(a,b))
#     else:
#         print('input invalid')
#     if optwo == '+':
#         a = (add3(a,b,c))
#     elif optwo == '-':
#         a = (sub3(a,b,c))
#     elif optwo == '*':
#         a = (mult3(a,b,c))
#     elif optwo == '/':
#         a = (div3(a,b,c))
#     else:
#         print('input invalid')
#     if opthree == '+':
#         a = (add4(a,b,c,d))
#     elif opthree == '-':
#         a = (sub4(a,b,c,d))
#     elif opthree == '*':
#         a = (mult4(a,b,c,d))
#     elif opthree == '/':
#         a = (div4(a,b,c,d))
#     else:
#         print('input invalid')
#     if opfour == '+':
#         result = (add5(a,b,c,d,e))
#         fracresult = Fraction(result).limit_denominator()
#     elif opfour == '-':
#         result = (sub5(a,b,c,d,e))
#         fracresult = Fraction(result).limit_denominator()
#     elif opfour == '*':
#         result = (mult5(a,b,c,d,e))
#         fracresult = Fraction(result).limit_denominator()
#     elif opfour == '/':
#         result = (div5(a,b,c,d,e))
#         fracresult = Fraction(result).limit_denominator()
#     else:
#         print('input invalid')
#     return print(str(result) + ' and as a fraction ' + str(fracresult))



    # if numprob == '2':
    #     twonumprob()
    # if numprob == '3':
    #     threenumprob()
    # if numprob == '4':
    #     fournumprob()
    # if numprob == '5':
    #     fivenumprob()