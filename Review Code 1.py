# Review Code 1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input('Enter the number of parking spaces: '))
y = input()
t = input()
count = 0

for num in range (n):
    yesterday = y[num]
    today = t[num]

    if (yesterday == 'C' and yesterday == today):
        count+=1

print (count)
