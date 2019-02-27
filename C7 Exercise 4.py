# Exercise 4
# Tashan Maniyalaghan
# 693776
# ICS3U0-B
# 1 December 2017
# Mr. Veera

def drawBar(layer, spaces):
    print (layer)
    layer = layer + '**'
    addSpaces(spaces, layer)

def addSpaces(spaces, layer):
    while (spaces != 0):
        spaces-=1
        blank = ' '*spaces
        print (blank, end ='')
        drawBar(layer, spaces)
        break

num = int(input('Enter the size: '))

layer = '*'
addSpaces(num, layer)

