# 2015 S2
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 5 Febuary 2019
# Mr. Veera

j = int(input())
a = int(input())
size = []
player = []
count = 0

for i in range (j):
    size.append(input())

for i in range (a):
    player.append(input())

for play in range (a):
    for s in range (j):
        if (player[play][0] == 'L'):
            if (size[s] == 'L'):
                if (player[play][2] == str(s)):
                    count+=1
        if (player[play][0] == 'L' or player[play][0] == 'M'):
            if (size[s] == 'L' or size[s] == 'M'):
                if (player[play][2] == str(s)):
                    count+=1
        if (player[play][0] == 'L' or player[play][0] == 'M' or player[play][0] == 'S'):
            if (size[s] == 'L' or size[s] == 'M' or size[s] == 'S'):
                if (player[play][2] == str(s)):
                    count+=1

print (count)
