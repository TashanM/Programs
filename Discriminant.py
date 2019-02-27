# Discriminant
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 12 October 2017
# Mr. Veera

a = float(input('Enter the value of a:'))
b = float(input('Enter the value of b:'))
c = float(input('Enter the value of c:'))

answer = (b**2) - (4*a*c)

if (answer < 0):
    print ('No roots.')
elif (answer == 0):
    print ('One root.')
else:
    print ('Two roots.')
