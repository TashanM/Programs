n = int(input())
l = []

for num in range (n):
    l.append(int(input()))

for rate in l:
    if (rate < 1000):
        print ('Newbie')
    if (rate >= 1000 and rate < 1200):
        print ('Amateur')
    if (rate >= 1200 and rate < 1500):
        print ('Expert')
    if (rate >= 1500 and rate < 1800):
        print ('Candidate Master')
    if (rate >= 1800 and rate < 2200):
        print ('Master')
    if (rate >= 2200 and rate < 3000):
        print ('Grandmaster')
    if (rate >= 3000 and rate < 4000):
        print ('Target')
    if (rate > 4000):
        print ('Rainbow Master')
