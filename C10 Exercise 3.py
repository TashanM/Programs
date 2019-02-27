# Exercise 3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 January 2017
# Mr. Veera

import random

count = 1
numbers = []
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0
count8 = 0
count9 = 0

while (count <= 500):
    integer = random.randint(0,9)

    numbers.append(integer)

    count+=1

for num in numbers:
    if (num == 0):
        count0+=1
        
    if (num == 1):
        count1+=1

    if (num == 2):
        count2+=1
        
    if (num == 3):
        count3+=1

    if (num == 4):
        count4+=1
        
    if (num == 5):
        count5+=1

    if (num == 6):
        count6+=1
        
    if (num == 7):
        count7+=1

    if (num == 8):
        count8+=1
        
    if (num == 9):
        count9+=1

print ('Numbers          Occurrences')
print ('0               ', count0)
print ('1               ', count1)
print ('2               ', count2)
print ('3               ', count3)
print ('4               ', count4)
print ('5               ', count5)
print ('6               ', count6)
print ('7               ', count7)
print ('8               ', count8)
print ('9               ', count9)
