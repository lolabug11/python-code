import datetime as date
import time as t
import random as r


repeat = 'yes'
while repeat == 'yes':
    current_year = date.datetime.now().year
    name = input('What is your name: ')
    birthday =  input('Is it your birthday today: ')

    if 'y' in birthday:
        brithyear = int(input('What year were you born: '))
        age = current_year - brithyear
        print('Happy ' + str(age) + 'th Birthday! :)')
        t.sleep(0.5)
        print('Happy Birthday to you,')
        t.sleep(0.5)
        print('Happy Birthday to you,')
        t.sleep(0.5)
        print('Happy Birthday dear ' + name + ',')
        t.sleep(0.5)
        print("Happy Birthday to youuuuuuuu!!!!")
        t.sleep(0.5)
        guess = 1
        while guess < age + 1:
            print('Are you ' + str(guess))
            guess = guess + 1
            t.sleep(0.5)
        print('*You say* STOP')

        if guess > 60:
            print('Wow Your old')

        elif guess > 116:
            print("You are tied for the world recod of oldedt person alive!")
        else:
            print("Have a good birthdy")
        repeat = input('do you want to repeat:')
    else:
        print('Have a good day, ' + name)
        repeat = input('do you want to repeat:')