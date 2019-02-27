n = int(input())
count = 0

for num in range (n):
    l = [int(num) for num in input().split()]

    if (l[0] >= 240 and l[0] <= 255):
        if (l[1] >= 0 and l[1] <= 200):
            if (l[2] >= 95 and l[2] <= 220):
                count+=1

print (count)
