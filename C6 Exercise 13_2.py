# Exercise 13_2
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 1 November 2017
# Mr. Veera

count1 = 0
count2 = 0
number_store = 0

start = int(input('Enter a start:'))
limit = int(input('Enter a limit:'))

for number in range (start, limit+1):
    print (' ')
    print (number)
    print (' ')

    number2 = number
    count1 = 0
    
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

        count1+=1

    if (count2 < count1):
        count2 = count1
        number_store = number2

print (' ')
print ('%i has the highest iteration count of %i.' %(number_store, count2))
