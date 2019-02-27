# Exercise 5
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 October 2017
# Mr. Veera

percent = int(input('Enter the percentage:'))

if (percent < 60):
    grade = 'F'
elif (percent <= 69):
    grade = 'D'
elif (percent <= 79):
    grade = 'C'
elif (percent <= 89):
    grade = 'B'
else:
    grade = 'A'

print ('The corresponding letter grade is: %s' %(grade))
