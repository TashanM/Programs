# Exercise 11
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 3 October 2017
# Mr. Veera

burgers = int(input('Enter the number of burgers:'))
fries = int(input('Enter the number of fries:'))
sodas = int(input('Enter the number of sodas:'))

notaxprice = burgers*1.69 + fries*1.09 + sodas*0.99
tax = notaxprice*0.065
total = tax + notaxprice

print ('Total before tax: $%.2f' %(notaxprice))
print ('Tax: $%.2f' %(tax))
print ('Final total: $%.2f' %(total))

paid = float(input('Enter amount tendered: $'))

change = paid - total

print ('Change: $%.2f' %(change))
