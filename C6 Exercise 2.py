# Exercise 2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 26 October 2017
# Mr. Veera

number = int(input('Enter a number:'))

count = 2

while (count <= number):
    if (number % count == 0):
        print(count)
        number = number / count
    else:
        count+=1
