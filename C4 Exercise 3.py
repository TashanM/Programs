# Exercise 3
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 2 October 2017
# Mr. Veera

tuition = int(input('Enter the tuition costs:'))
living = int(input('Enter the living costs:'))
books = int(input('Enter the supply costs:'))
food = int(input('Enter the food costs:'))
offset = int(input('Enter the offset costs:'))

total = (tuition + living + books + food) - offset

print ('Your cost to go to college or university is: %i' %(total))
