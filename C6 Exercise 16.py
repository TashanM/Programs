# Exercise 16
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 November 2017
# Mr. Veera

from random import randint

greatest = 0
average = 0
trials = 1
location = 3.5
steps = 0

while (trials <= 50):

    while (location >= 1 and location <= 7):
        direction = randint(0,1)
        if (direction == 0):
            location+=1
            steps+=1
        else:
            location-=1
            steps+=1

    average+=steps
    
    if (steps > greatest):
        greatest = steps

    location = 3.5
    steps = 0

    trials+=1

average/=50

print ('The average amount of steps in 50 trials is %.1f.' %(average))
print ('the greatest amount of steps for a trial is %i.' %(greatest))
