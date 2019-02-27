# Exercise 1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 January 2017
# Mr. Veera

import random

even = []
odd = []
count = 1

while (count <= 25):
    number = random.randint(0,99)

    if (number%2 == 0):
        even.append(number)

    else:
        odd.append(number)

    count+=1

print ('ODD:')

for e in even:
    print (e, end = ' ')

print ()
print ('EVEN:')

for o in odd:
    print (o, end = ' ')
