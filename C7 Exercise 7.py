# Exercise 7
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 December 2017
# Mr. Veera

def isPerfect(integer, total):
    for factor in range (1, integer):
        if (integer%factor == 0):
            total+=factor
    if (total == integer):
        print (integer)

for integer in range (1, 101):
    total = 0
    isPerfect(integer, total)
