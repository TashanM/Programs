n = int(input())
yesterday = input()
today = input()

count = 0
same = 0

while (count < n):
    if (yesterday[count] == today[count] and yesterday[count] == 'C'):
        same+=1
    
    count+=1

print (same)
