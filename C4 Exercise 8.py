# Exercise 8
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 3 October 2017
# Mr. Veera

interger1 = int(input('Enter an interger:'))
interger2 = int(input('Enter a second interger:'))

equation1 = interger1//interger2
equation2 = interger1%interger2
equation3 = interger2//interger1
equation4 = interger2%interger1

print ('%i // %i = %i' %(interger1, interger2, equation1))
print (interger1 + ' % ' + interger2 + ' = ' + equation2)
print ('%i // %i = %i' %(interger2, interger1, equation3))
print (interger2 + ' % ' + interger1 + ' = ' + equation4)
