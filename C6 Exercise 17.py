# Exercise 17
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 10 November 2017
# Mr. Veera

password = 'soccer'

for attempts in range (1, 4):
    guess = input('Enter the password: ')
    
    if (guess == password):
        print ('Access Granted.')
        break
    else:
        print ('The password you typed is incorrect.')

print ('Access Denied.')
