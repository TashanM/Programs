# Exercise 15_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 October 2017
# Mr. Veera

principal = float(input('Enter the principal:'))
years = float(input('Enter the number of years:'))
interest = float(input('Enter the interest rate:'))

amount = principal*(1 + years*interest)

print ('The value after the term is: $%.2f' %(amount))
