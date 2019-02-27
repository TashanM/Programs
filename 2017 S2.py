# 2017 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input())
measurements = [int(num) for num in input().split()]
low = []
high = []
order = []

measurements.sort()

for num in range (n):
    if (num < int(n/2)):
        low.append(measurements[num])
    else:
        high.append(measurements[num])

high.sort()
low.sort(reverse = True)
print (high)
print (low)

for num in range (n//2):
    order.append(low[num])
    order.append(high[num])

print (order)
