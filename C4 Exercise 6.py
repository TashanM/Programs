# Exercise 6
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 2 October 2017
# Mr. Veera

change = float(input('Enter the change in cents:'))

quarters = change//25
remainder1 = change%25
dimes = remainder1//10
remainder2 = remainder1%10
nickels = remainder2//5
pennies = remainder2%5

print ('The minimum number of coins is:')
print (' '*8 + 'Quarters: %i' %(quarters))
print (' '*8 + 'Dimes: %i' %(dimes))
print (' '*8 + 'Nickels: %i' %(nickels))
print (' '*8 + 'Pennies: %i' %(pennies))
