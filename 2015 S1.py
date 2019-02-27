# 2015 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

k = int(input())
l = []
new = []
total = 0

for num in range (k):
    l.append(int(input()))

for num in range (len(l)):
    new.append(l[num])
    
    if (l[num] == 0):
        new.pop()
        new.pop()

for num in new:
    total+=num

print (total)
