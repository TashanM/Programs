# Exercise 3_1_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 December 2017
# Mr. Veera

def isPrime(number):
    count = 2
    flag = False

    while(count<number):
        remainder = number % count
        if (remainder == 0):
            flag = True
        count+=1

    return flag

num = int(input('Enter a number:'))
print ()

numtype = isPrime(num)

if (numtype == True):
    print ('This is a composite number.')
else:
    print ('This is a prime number.')
