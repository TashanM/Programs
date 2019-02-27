# 2015 S3
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

g = int(input())
p = int(input())
l = []
new = []
count = 0

for num in range (p):
    l.append(int(input()))

for num in range (g):
    new.append(0)

for num in (l):
    if (new[num - g -1] == 0):
        new[num - g -1] = num
        count+=1

print (count)
    
