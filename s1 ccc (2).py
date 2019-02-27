n = int(input())
r = []
c1 = 0
c2 = 0
h1 = 0
h2 = 0

for num in range (n):
    r.append(int(input()))

r.sort()

while (True):
    num = r.count(r[0])

    if (num > c1):
        h2 = h1
        c2 = c1
        h1 = r[0]
        c1 = num
        for num1 in range (len(r)):
            if (h1 in r):
                r.remove(h1)

    elif (num > c2):
        h2 = r[0]
        c2 = num
        for num1 in range (len(r)):
            if (h2 in r):
                r.remove(h2)

    elif (num == c2):
        if (abs(r[0] - h1) > abs(h2 - h1)):
            h2 = r[0]
            c2 = num
            for num1 in range (len(r)):
                if (h2 in r):
                    r.remove(h2)
        else:
            t = r[0]
            for num1 in range (len(r)):
                if (t in r):
                    r.remove(t)
    
    elif (num == c1):
        if (abs(r[0] - h2) > abs(h1 - h2)):
            h1 = r[0]
            c1 = num
            for num1 in range (len(r)):
                if (h1 in r):
                    r.remove(h1)
        else:
            t = r[0]
            for num1 in range (len(r)):
                if (t in r):
                    r.remove(t)

    if (r == []):
        break
    
total = h1 - h2

print (abs(total))
