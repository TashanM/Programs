# Exercise 8_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 December 2017
# Mr. Veera

import random

points = 1000
play = 'y'
guessamount = 0

def HiLo(number, guess):
        if ((number < 7 and guess == 0) or (number > 7 and guess == 1)):
            answer = 'yes'
        else:
            answer = 'no'

        return answer

print ('High Low Game')
print ()
print ('RULES')
print ('Numbers 1 through 6 are Low')
print ('Numbers 8 through 13 are High')
print ('Number 7 is neither high or low')
print ()

while (play != 'n' and points > 0):
        number = random.randint(1, 13)
        print ('You have %i points.' %(points))
        print ()
        risk = int(input('Enter points to risk: '))
        print ()
        guess = int(input('Predict <1 - High, 0 - Low>: '))
        guessamount+=1
        print ('Number is %i' %(number))
        
        answer = HiLo(number, guess)
        
        if (answer == 'yes'):
            print ('You win!')
            points = points + (risk*2)
        else:
            print ('You lose.')
            points-=risk

        play = input('Play again? ')

print ('Thank you for playing! You had a total of %i guesses' %(guessamount))
