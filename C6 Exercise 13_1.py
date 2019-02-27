# Exercise 13_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 1 November 2017
# Mr. Veera


for number in range (1, 201):
    print (' ')
    print (number)
    print (' ')
    
    while (number != 1):
        if (number%2 == 0):
            number = number/2
        else:
            number = number*3+1

        if (number == 1):
            print (str(int(number)), end ='')
            print (' ')
        else:
            print (str(int(number)), end = ', ')
