# Exercise 3_1_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 1 December 2017
# Mr. Veera

def isPrime(number):
    count = 2
    flag = False

    while(count<number):
        remainder = number % count
        if (remainder == 0):
            flag = True
        count+=1
    
    if (flag == True):
        print ('This is a composite number.')
    else:
        print ('This is a prime number.')

num = int(input('Enter a number:'))
print ()

isPrime(num)
