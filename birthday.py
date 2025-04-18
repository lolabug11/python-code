import datetime as date
import time as t
import random


repeat = 'yes'
while 'y' in repeat:
    current_year = date.datetime.now().year
    name = input('What is your name: ')
    FirstLetter = name[0]
    name = name[1:]
    FirstLetter = FirstLetter.capitalize()
    name = FirstLetter + name
    birthday =  input('Is it your birthday today: ')
    birthday = birthday.lower()
    if 'y' in birthday:
        brithyear = int(input('What year were you born: '))
        age = current_year - brithyear
        if age < 0:
            print('You probably arnt able to even breathe let alone type so get lost you randon person from the future usin gmy code from 2025')
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
        
        a = int(age)/2
        b = int(age)*2
        holder = 0
        guess = random.randint(int(a),int(b))
        print(guess)
        def guess():
            if age < 0:
                age = int(age) * -1
            guess = random.randint(0, 100)
            a = age/2
            b = age*2
            while guess != age:
                guess = random.randint(int(a), int(b))
                inputv = input('Are you ' + str(guess)+ '?')
            return print('')
        guess()
        repeat = input('')
    else:
        print('Have a good day, ' + name)
        repeat = input('')
