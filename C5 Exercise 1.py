# Exercise 1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 October 2017
# Mr. Veera

copies = int(input('Enter the number of copies to be printed:'))

if (copies > 1000):
    price = 0.25
elif (copies >= 750):
    price = 0.26
elif (copies >= 500):
    price = 0.27
elif (copies >= 100):
    price = 0.28
else:
    price = 0.30

total = copies*price
print ('Price per copy is: $%.2f' %(price))
print ('Total cost is: $%.2f' %(total))
