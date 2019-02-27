# Review Code 2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input('Enter the number of adjectives: '))
m = int(input('Enter the number of nouns; '))
adjectives = []
nouns = []

for num1 in range (n):
    adjectives.append(input('Enter an adjective: '))

for num2 in range (m):
    nouns.append(input('Enter a noun: '))

for num3 in range (n):
    for num4 in range (m):
        print (adjectives[num3] + ' as ' + nouns[num4])
