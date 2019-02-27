# Exercise 20
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 13 November 2017
# Mr. Veera

text = input('Enter text: ')
text_store = text.lower()
count = 0

for letter in text_store:
    if (letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y'):
        count+=1

print ('The number of vowels in %s is %i' %(text, count))
