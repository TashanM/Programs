# Exercise 9
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 17 October 2017
# Mr. Veera

from random import randint

secret_num = randint (1,20)

guess = int(input('Enter a number between 1 and 20:'))

if (guess == secret_num):
    print ("Computer's Number: %i" %(secret_num))
    print ("Player's Number: %i" %(guess))
    print ('Good Job!')
else:
    print ("Computer's Number: %i" %(secret_num))
    print ("Player's Number: %i" %(guess))
    print ('Better luck next time.') 
