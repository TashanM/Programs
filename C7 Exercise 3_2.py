# Exercise 3_2_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 1 December 2017
# Mr. Veera

def isPrime(number1, number2):
    if (number1 == 1):
        num = number1+1
    else:
        num = number1
    while (num <= number2):
        count = 2
        flag = True
        for count in range (2, num):
            if (num%count == 0):
                flag = False
        if (flag == True):
            print (num)
        num+=1

num1 = int(input('Enter the lower number:'))
num2 = int(input('Enter the higher number:'))

isPrime(num1, num2)
