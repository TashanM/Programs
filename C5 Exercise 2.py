# Exercise 2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 October 2017
# Mr. Veera

weight = float(input('Enter package weight in kilograms:'))
length = float(input('Enter package length in centimeters:'))
width = float(input('Enter package width in centimeters:'))
height = float(input('Enter package height in centimeters:'))

weightrounded = int(weight*100)
lengthrounded = int(length*100)
widthrounded = int(width*100)
heightrounded = int(height*100)

volume = lengthrounded*widthrounded*heightrounded

if (volume < 10000000000 and weightrounded < 2700):
    print ('Good to go.')
elif (volume > 10000000000 and weightrounded > 2700):
    print ('Too heavy and too large.')
elif (volume > 10000000000):
    print ('Too large.')
elif (weightrounded > 2700):
    print ('Too heavy.')
