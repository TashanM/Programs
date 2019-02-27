# Exercise 13
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 18 October 2017
# Mr. Veera

p = int(input('Principal:'))
r = float(input('Interest Rate:'))
m = int(input('Number of monthly payments:'))

monthly_payment = (p*(r/12))/(1-(1+r/12)**-m)

print ('The monthly payment is $%.2f' %(monthly_payment))
