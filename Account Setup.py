# Account Setup
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 10 November 2017
# Mr. Veera

username = input('Enter a username: ')

password = input('Enter a password that is atleast 8 characters:') 

while (len(password) < 8):
    password = input('Enter a password that is atleast 8 characters:')

print ('Your username is %s and your password is %s' %(username.lower(), password.lower()))
