# 2016 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

q = int(input())
n = int(input())
d = [int(num) for num in input().split()]
p = [int(num) for num in input().split()]
total = 0

if (q == 1):
    d.sort()
    p.sort()

    for num in range (n):
        if (d[num] > p[num]):
            total+=d[num]
        else:
            total+=p[num]
    print (total)

if (q == 2):
    d.sort()
    p.sort(reverse = True)

    for num in range (n):
        if (d[num] > p[num]):
            total+=d[num]
        else:
            total+=p[num]
    print (total)
