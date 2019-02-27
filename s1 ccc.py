n = int(input())
sw = [int(num) for num in input().split()]
se = [int(num) for num in input().split()]
tsw = 0
tse = 0
day = 0

for num in range (n):
    tsw+=sw[num]
    tse+=se[num]

    if (tsw == tse):
        day = num+1

print (day)
