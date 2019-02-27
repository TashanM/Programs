# Exercise 14
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

from math import exp

n = int(input('Enter the initial bacteria amount:'))
k = float(input('Enter a constant value for k:'))
t = int(input('Enter the growth time period in hours:'))

y = n*(exp(k*t))

print ('%.1f bacteria will be present after %.1f hours.' %(y, t))
