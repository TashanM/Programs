# 2011 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 14 Febuary 2019
# Mr. Veera

n = int(input())
s = []
a = []
count = 0

for num in range (n):
    s.append(input())

for num in range (n):
    a.append(input())

for num in range (n):
    if (s[num] == a[num]):
        count+=1

print (count)
