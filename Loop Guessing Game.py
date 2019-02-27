# Loop Guessing Game
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 24 October 2017
# Mr. Veera

count = 1
SECRET = 5

while (count < 5):
    guess = int(input('Guess a number:'))

    if (guess == SECRET):
        print('Congratulations you guessed it!')
        print('You guess the correct answer in %i tries'%(count))
        break
    
    elif (guess < SECRET and count < 4):
        print ('Your guess is too low, try again.')

    elif (count < 4):
        print ('Your guess is too high, try again.')

    count+=1

if (count == 5):
  print ('Sorry you exhausted your changes.')
