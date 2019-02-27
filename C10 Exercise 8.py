# Exercise 8
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 16 January 2017
# Mr. Veera

text = input('Enter text: ').lower()

text = text.replace(' ', '')

palindrome = text[-1::-1]

if (palindrome == text):
    print ('This is a palindrome.')

else:
    print ('This is not a palindrome.')
