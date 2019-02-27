# Exercise 11
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

from math import sqrt

a = int(input('Enter value for a:'))
b = int(input('Enter value for b:'))
c = int(input('Enter value for c:'))

discriminant = (b**2) - (4*a*c)

if (discriminant < 0):
    print ('No real roots')
else:
    root1 = (-b + sqrt(discriminant))/(2*a)
    root2 = (-b - sqrt(discriminant))/(2*a)

    if (root1 == root2):
        print ('The root is %.1f' %(root1))
    else:
        print ('The roots are %.1f and %.1f' %(root1, root2))
