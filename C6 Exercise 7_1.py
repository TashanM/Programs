# Exercise 7_1
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 5 November 2017
# Mr. Veera

num = int(input('Enter a positive interger: '))

power = 0
total = 0

while (num//10**power != 0):
    power+=1

while (power > 0):
    num2 = num // 10**(power - 1)
    num2 = num2**3
    total = total + num2
    num = num % 10**(power - 1)
    
    power-=1

print ('The sum of the cubes of the digits is: %i' %(total))
