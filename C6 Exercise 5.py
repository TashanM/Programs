# Exercise 5
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 3 November 2017
# Mr. Veera

num = int(input('Enter a positive interger: '))

power = 0

while (num//10**power != 0):
    power+=1

while (power > 0):
    num2 = num // 10**(power - 1)
    print (num2)
    num = num % 10**(power - 1)
    
    power-=1

