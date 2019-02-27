# Hundreds, Tens, Units Algorithm
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 2 October 2017
# Mr. Veera

number = int(input('Enter a 4 digit whole number:'))

thousands = number//1000
remainder1 = number%1000
hundreds = remainder1//100
remainder2 = remainder1%100
tens = remainder2//10
units = remainder2%10

print ('The thousands is %i, the hundreds is %i, the tens is %i, and the units is %i.' %(thousands, hundreds, tens, units))
