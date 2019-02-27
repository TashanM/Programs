# CircleCircumference
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 11 October 2017
# Mr. Veera

radius = int(input('Enter the radius of a circle:'))

if (radius < 0):
    print ('Negative radii are illegal.')
else:
    circumference = 2*3.14159*radius
    print ('The circumference of the circle is: %.2f' %(circumference))
