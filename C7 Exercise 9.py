# Exercise 9
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 7 December 2017
# Mr. Veera

import random

def isValidEntry (usertake, stones):
    if (usertake >= 4 or usertake == 0):
        return False
    if (usertake > stones):
        return False
    else:
        return True
    
def User(stones, usertake):
    stones-=usertake
    return stones

def drawStones(stones):
    if (stones <= 4 and stones != 1):
        if (stones == 4):
            comptake = 3
        elif (stones == 3):
            comptake = 2
        elif (stones == 2):
            comptake = 1
    else:
        comptake = random.randint(1,3)
        while (comptake > stones):
            comptake = random.randint(1,3)

    return comptake

def Computer(stones, comptake):
    stones-=comptake
    return stones

stones = random.randint(15, 30)

choice = int(input('Enter 1 for Single Player or 2 for Multiplayer: '))

if (choice == 1):
    while (True):
        usertake = int(input('There are %i stones. How many would you like? ' %(stones)))

        if (isValidEntry(usertake, stones) == True):
            stones = User(stones, usertake)
        
            if (stones == 0):
                print ('The computer beats the player.')
                break

            comptake = drawStones(stones)
            print ('There are %i stones. The computer takes %i stones.' %(stones, comptake))
            stones = Computer(stones, comptake)

            if (stones == 0):
                print ('The player beats the computer.')
                break

else:
    while (True):
        usertake = int(input('There are %i stones. Player 1, how many would you like? ' %(stones)))

        if (isValidEntry(usertake, stones) == True):
            stones = User(stones, usertake)

            if (stones == 0):
                print ('The Player 2 beats the PLayer 1.')
                break

            usertake = int(input('There are %i stones. Player 2, how many would you like? ' %(stones)))

            if (isValidEntry(usertake, stones) == True):
                stones = User(stones, usertake)

            if (stones == 0):
                print ('The Player 1 beats the Player 2.')
                break
