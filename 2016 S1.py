# 2016 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

word = []
for char in input():
    word.append(char)

anagram = []
for char in input():
    anagram.append(char)

count = 0
word.sort()
anagram.sort()

for num in range (len(word)):
    if (word[num] == anagram[num] or anagram[num] == '*'):
        count+=1
        print (num)

if (count == len(word)):
    print ('Y')
else:
    print ('N')
