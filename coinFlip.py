import random

guessList = ['heads', 'tails']
guess = ''
while guess not in guessList:
    guess = input('Guess the coin toss! Enter heads or tails:')

toss = random.choice(guessList)

if toss == str(guess):
    print('You got it!')
else:
    guess = input('Nope! Guess again!')
    if toss == str(guess):
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
