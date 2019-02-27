# Exercise 10
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 16 January 2017
# Mr. Veera

text = input('Enter a string: ')
cipher = int(input('Enter cipher value: '))

ciphered = ''

for i in text:
    if (i != ' '):
        asciival = ord(i)
        asciival+=cipher
        
        while (asciival > 122):
            asciival-=26

        while (asciival < 97):
            asciival+=26

        ciphered+=(chr(asciival))
    else:
        ciphered+=' '
        
print ('Encoded Message: %s' %(ciphered))
