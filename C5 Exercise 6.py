# Exercise 6
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 16 October 2017
# Mr. Veera

import random

firstnumber = random.randint (1,10)
secondnumber = random.randint (1,10)
operator = random.randint (1,4)

if (operator == 1):
   answer = firstnumber + secondnumber
   guess = int(input('What is %i + %i?' %(firstnumber, secondnumber)))
elif (operator == 2):
   answer = firstnumber - secondnumber
   guess = int(input('What is %i - %i?' %(firstnumber, secondnumber)))
elif (operator == 3):
   answer = firstnumber / secondnumber
   guess = int(input('What is %i / %i?' %(firstnumber, secondnumber)))
else:
   answer = firstnumber * secondnumber
   guess = int(input('What is %i * %i?' %(firstnumber, secondnumber)))

if (guess == answer):
    print ('Correct! The answer is', answer)
else:
    print ('Incorrect. The answer is', answer)
