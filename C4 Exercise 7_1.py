# Hundreds, Tens, Units Algorithm
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 2 October 2017
# Mr. Veera

number = int(input('Enter a 3 digit whole number:'))

hundreds = number//100
remainder = number%100
tens = remainder//10
units = remainder%10

print ('The hundreds is %i, the tens is %i, and the units is %i.' %(hundreds, tens, units))
