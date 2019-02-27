# Exercise 8_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 December 2017
# Mr. Veera

import random

points = 1000
play = 'y'

def HighLow(points, play):
    while (play != 'n'):
        number = random.randint(1, 14)
        print ('You have %i points.' %(points))
        print ()
        risk = int(input('Enter points to risk: '))
        print ()
        guess = int(input('Predict <1 - High, 0 - Low>: '))
        print ('Number is %i' %(number))

        if (number < 7 and guess == 0 or number > 7 and guess == 1):
            print ('You win.')
            points = points + risk*2
        else:
            print ('You lose.')
            points-=risk

        play = input('Play again? ')

    print ('Thank you for playing!')

print ('High Low Game')
print ()
print ('RULES')
print ('Numbers 1 through 6 are Low')
print ('Numbers 8 through 13 are High')
print ('Number 7 is neither high or low')
print ()

HighLow(points, play)
