# Exercise 10
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

import math

print ('Rectangular Prism')
l = float(input('Enter the length:'))
w = float(input('Enter the width:'))
h = float(input('Enter the height:'))

rectvolume = l*w*h

print (' ')
print ('Sphere')
print ('The volume is: %.2f' %(rectvolume))

r = float(input('Enter the radius:'))

d = 2*r
spherevolume = (math.pi*d**3)/6

print (' ')
print ('Cube')
print ('The volume is: %.2f' %(spherevolume))

s = float(input('Enter the length of each side:'))

cubevolume = s**3

print ('The volume is: %.2f' %(cubevolume))
