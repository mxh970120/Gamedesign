'''
game name: number guess
author: mxh970120
'''

import random

numberOfGuess = 0
rightAnswer = False
worryNumber = 0

print('What is your name?')
myName = input('My name is: ')

number = random.randint(1, 100)
print('Hi,' + myName + ', I have a number between 1 and 100')

i = 0
while i < 6:
    print('Take a Guess')
    guess = input('I guess: ')
    try:
        guess = int(guess)
    except ValueError:
        print('please give a number!')
        worryNumber += 1
        if worryNumber > 5:
            print('I do not play with you!')
            break
        continue

    if guess < number:
        print('Your Guess is too low.')
        i += 1
    elif guess > number:
        print('Your Guess is too high.')
        i += 1
    else:
        rightAnswer = True
        numberOfGuess = i
        break




if rightAnswer:
    numberOfGuess = str(numberOfGuess)
    print('Good Job! You try ' + numberOfGuess + ' times')
else:
    number = str(number)
    print('Nope, the number is ' + number )