# 2018 S4
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input())
count = 0

for num1 in range (2,n+1):
    for num2 in range (1,n+1):
        total = num1*num2

        if (total >= n/2 and total <= n):
            count+=1

print (count)
