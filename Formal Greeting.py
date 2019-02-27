# Formal Greeting
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 November 2017
# Mr. Veera

name = input('Enter your name: ')

if (name.startswith('Mr.')):
    print ('Hello, sir.')
elif (name.startswith('Ms.') or name.startswith('Mrs.') or name.startswith('Miss')):
    print ("Hello, ma'am.")
else:
    print ('Hello, %s' %(name))
