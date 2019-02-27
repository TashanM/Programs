n = int(input())
count = 0

for num in range (int(n/2), n+1):
    if (num <= 5):
        if (n - num <= 5):
            count+=1

if (n%2 != 0):
    count-=1

print (count)
