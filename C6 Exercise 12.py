# Exercise 12
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 6 November 2017
# Mr. Veera

num1 = int(input('Enter the first starting number:'))
num2 = int(input('Enter the second starting number:'))

numstore1 = num1
numstore2 = num2

while (True):
    print(str(num1), str(num2), '', end='')
    
    num1 = (num1 + num2) % 10
    num2 = (num1 + num2) % 10
    
    if (num1 == numstore1 and num2 == numstore2):
        print(str(num1), str(num2), ' ', end='')
        break
