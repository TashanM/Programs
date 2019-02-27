# Exercise 7_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 November 2017
# Mr. Veera

power = 0

for num in range (10, 10001):
    print (' ')
    print (num)
    print (' ')

    total = 0
    numstore = num
    
    while (num//10**power != 0):
        power+=1

    while (power > 0):
        num2 = num // 10**(power - 1)
        num2 = num2**3
        total = total + num2
        num = num % 10**(power - 1)
    
        power-=1

    print ('The sum of the cubes of the digits is: %i' %(total))
    
    if (total == numstore):
        print ('The original interger and the sum of the cubes of the digits are equal.')
    else:
        print ('The original interger and the sum of the cubes of the digits are not equal.')


