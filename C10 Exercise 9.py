# Exercise 9
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 15 January 2017
# Mr. Veera

consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
count = 0

text = input('Enter text: ')

for letter in text:
    if letter in consonants:
        count+=1

print ('The number of consonants in %s is %i' %(text, count))
