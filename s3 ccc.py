import collections

n = int(input())
r = []
h1 = []
h2 = []
c1 = 0
c2 = 0
one = 0
two = 0

for num in range (n):
    r.append(int(input()))

t = collections.Counter(r)
srt = sorted(r, key=lambda x: (t[x],x), reverse=True)

for num in range (len(srt)):
    if (srt.count(srt[0]) >= c1):
        h1.append(srt[0])
        c1 = srt.count(srt[0])

        i = srt[0]
        for num1 in range (len(srt)):
            if (i in srt):
                srt.remove(i)
        
    elif (srt.count(srt[0]) >= c2):
        h2.append(srt[0])
        c2 = srt.count(srt[0])

        i = srt[0]
        for num1 in range (len(srt)):
            if (i in srt):
                srt.remove(i)

    if (srt == []):
        break

h1.sort()
h2.sort()

if (h2 == []):
    one = h1[0]
    two = h1[len(h1)-1]
    
else:
    for num in h1:
        for num1 in h2:
            if (abs(num1 - num) > abs(one - two)):
                one = num
                two = num1

print (abs(one-two))
