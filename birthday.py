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
        higherguees = int(input('Do you want to play a game of higher or lower or do you just want me to guess(1 for minygame): '))
        if higherguees == 1:
            if age > 30:
                guess = age - 20
            elif age < 10:
                guess = age - 1
            else:
                guess = age - 6
            print('Are you ' + str(guess) + '?')
            higherorlower = input('Am i to high or to low or am i correct: ')
            higherorlower = higherorlower.lower()
            if 'h' in higherorlower:
                guess = guess - 5
                print('Are you ' + str(guess) + '?')
                higherorlower= input('Was I on point a little high or a little low: ')
                if 'h' in higherorlower:
                    guess = guess - 5
                    print('Are you ' + str(guess) + '?')
                    higherorlower= input('Was I on point a little high or a little low: ')
                elif 'l':
                    guess = guess + 5
            elif 'l' in higherorlower:
                guess = guess + 5
                print('Are you ' + str(guess) + '?')
                higherorlower = input('Am i to high or to low or am i correct: ')     
                if 'h' in higherorlower:
                    guess = guess - 5
                    print('Are you ' + str(guess) + '?')
                    higherorlower= input('Was I on point a little high or a little low: ')
                elif 'l' in higherorlower:
                    guess = guess + 5
                    print('Are you ' + str(guess) + '?') 
                    higherorlower= input('Was I on point a little high or a little low: ')
                    if 'h' in higherorlower:
                        guess = guess - 5
                        print('Are you ' + str(guess) + '?')
                        higherorlower = input('Was I on point a little high or a little low: ')
                        print('My final guess is ' + str(age))
                    elif 'l' in higherorlower:
                        guess = guess + 5
                        print('Are you ' + str(guess) + '?')
                        higherorlower= input('Was I on point a little high or a little low: ')
                        print('My final guess is ' + str(age))
        else:
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