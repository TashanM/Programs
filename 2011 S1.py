# 2011 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 14 Febuary 2019
# Mr. Veera

n = int(input())
text = []
t = 0
s = 0

for num in range (n):
    text.append(input())

for index in text:
    for i in index:
        if (i == 't' or i == 'T'):
            t+=1
        if (i == 's' or i == 'S'):
            s+=1

if (t > s):
    print ('English')
else:
    print('French')
