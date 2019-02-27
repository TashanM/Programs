# Exercise 21
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 20 November 2017
# Mr. Veera

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

for letter in 'ABCDEFGHI':
    if (last_name.startswith(letter)):
        print ('%s %s is assigned to Group 1.' %(first_name, last_name))

for letter in 'JKLMNOPQRS':
    if (last_name.startswith(letter)):
        print ('%s %s is assigned to Group 2.' %(first_name, last_name))
     
for letter in 'TUVWXYZ':
    if (last_name.startswith(letter)):
       print ('%s %s is assigned to Group 3.' %(first_name, last_name))
