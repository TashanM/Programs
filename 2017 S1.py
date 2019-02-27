# 2017 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input())
swift = 0
sema = 0
k = 0

swiftscore = [int(num) for num in input().split()]
semascore = [int(num) for num in input().split()]

for i in range (n):
    swift+=swiftscore[i]
    sema+=semascore[i]

    if (swift == sema):
        k = i+1

print (k)
