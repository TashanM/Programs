# Exercise 5
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 2 October 2017
# Mr. Veera

mass = int(input('Enter the mass in kilograms:'))

energy = mass*(3.0*10**8)**2

lightbulbs = energy//360000

print ('The energy produced in Joules is: %.1E' %(energy))
print ('The number of 100-watt ligh bulbs powered is: %.1E' %(lightbulbs))
