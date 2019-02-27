# 2013 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 6 Febuary 2019
# Mr. Veera

w = int(input())
n = int(input())
t = []
count = 0
weight = 0

for num in range (n):
    t.append(int(input()))

for num in range (n):
    if (weight <= w):
        if (count > 3):
            weight-=t[num-4]
        weight+=t[num]
    if (weight > w):
        break
    count+=1

print(count)
