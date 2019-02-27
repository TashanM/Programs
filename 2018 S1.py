# 2018 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 1 Febuary 2019
# Mr. Veera

n = int(input())
villages = []
distance = []

for num in range (n):
    villages.append(int(input()))

villages.sort()

for num in range (1, n-1):
    distance.append((villages[num+1] + villages[num])/2 - (villages[num] + villages[num-1])/2)

distance.sort()

print ('%0.1f' %(distance[0]))
