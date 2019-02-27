# Exercise 10
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 31 October 2017
# Mr. Veera

number1 = int(input('Enter a number:'))
number2 = int(input('Enter the second number:'))

while (number2 > 0):
    temp = number2 % number1
    number1 = number2
    number2 = temp

print ('The GCD is %i.' %(number1))
