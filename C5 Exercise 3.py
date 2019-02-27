# Exercise 3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 October 2017
# Mr. Veera

eggs = int(input('Enter the number of eggs purchased:'))

if (eggs >= 132):
    price = 0.35
elif (eggs >= 72):
    price = 0.40
elif (eggs >= 48):
    price = 0.45
else:
    price = 0.50

dozen = eggs//12
extraeggs = eggs%12
remainder = price/12
bill = price*dozen + remainder*extraeggs

print ('The bill is equal to: $%.2f' %(bill))
