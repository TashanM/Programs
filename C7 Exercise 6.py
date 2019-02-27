# Exercise 6
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 December 2017
# Mr. Veera

import math

def PerfectSquare(a, b):
            total = a**2 + b**2
            for squareroot in range (1, total+1):
                c = math.sqrt(total)
                if (c == squareroot):
                    print ('%i**2 + %i**2 = %i**2' %(a, b, c))

for a in range (1, 100):
    for b in range (1, 100):
        PerfectSquare(a, b)
