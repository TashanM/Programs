# Exercise 1_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 26 October 2017
# Mr. Veera

number = int(input('Enter the lower number:'))
number2 = int(input('Enter the higher number:'))

if (number == 1):
    num = number+1
else:
    num = number
while (num <= number2):
    count = 2
    flag = True
    while (count < num):
        if (num%count == 0):
            flag = False
        count+=1
    if (flag == True):
        print (num)
    num+=1
