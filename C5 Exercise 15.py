# Exercise 15
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

from math import exp
from math import log

print ('1. Final Amount')
print ('2. Initial Amount')
print ('3. Constant <half-life>')

find = int(input('Find:'))

if (find == 1):
    intial_value = float(input('Enter the initial bacteria amount:'))
    constant = float(input('Enter a constant value for k:'))
    time = float(input('Enter the growth time period in hours:'))
    
    final_value = intial_value*(exp(-constant*time))

    print ('Final amount: %.1f' %(final_value))
elif (find == 2):
    final_value = float(input('Enter the final bacteria amount:'))
    constant = float(input('Enter a constant value for k:'))
    time = float(input('Enter the growth time period in hours:'))

    initial_value = final_value/(exp(-constant*time))

    print ('Initial amount: %.1f' %(initial_value))
else:
    initial_value = float(input('Enter the initial bacteria amount:'))
    final_value = float(input('Enter the final bacteria amount:'))
    time = float(input('Enter the growth time period in years:'))

    constant = (log(final_value/initial_value))/time

    print ('Constant <half-life>: %.5f' %(constant))
