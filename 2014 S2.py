# 2014 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

n = int(input())
f = []
s = []
count = 0

for name in input().split():
    f.append(name)

for name in input().split():
    s.append(name)

for num in range (n):
    if (f[num] != s[num]):
        count+=1

if (count == n):
    print('good')
else:
    print('bad')
