# Exercise 10
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 11 December 2017
# Mr. Veera

from random import randint

def giveHint(guess, secret_num):
    if (guess > secret_num):
        return True
    elif (guess < secret_num):
        return False
    
secret_num = randint (1,20)
guess = 0

while (True):
    guess = int(input('Enter a number between 1 and 20: '))

    if (guess == secret_num):
        print ('You won!')
        break
    
    if (giveHint(guess, secret_num) == True):
        print ('Hint: Try a lower number.')
    else:
        print ('Hint: Try a higher number.')
    print()
