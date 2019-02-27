# 2012 S1
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 13 Febuary 2019
# Mr. Veera

j = int(input())
com = 0

for num1 in range (1, j):
    for num2 in range (1, j):
        for num3 in range (1, j):
            players = []
            players.append(num3)
            players.append(num2)
            players.append(num1)
            players.append(j)

            if (players[0] < players[1]):
                if (players[1] < players[2]):
                    if (players[2] < players[3]):
                        com+=1

print(com)
