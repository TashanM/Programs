# Exercise 17
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

from math import asin
from math import acos
from math import atan
from math import radians

angle = radians(int(input('Enter an angle in degrees:')))

sine = asin(angle)
cosine = acos(angle)
tangent = atan(angle)

print (' ')
print ('Sine: %.2f' %(sine))
print ('Cosine: %.2f' %(cosine))
print ('Tangent: %.2f' %(tangent))
