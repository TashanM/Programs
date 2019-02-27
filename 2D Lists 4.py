# 2D Lists 4
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 10 Febuary 2019
# Mr. Veera

from random import randint

one = ['      ', '      ', '      ', '      ', '      ']
two = ['      ', '      ', '      ', '      ', '      ']
three = ['      ', '      ', '      ', '      ', '      ']
four = ['      ', '      ', '      ', '      ', '      ']
five = ['      ', '      ', '      ', '      ', '      ']
board = [one, two, three, four, five]

count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

puzzle = 0
ball = 0
game = 0
doll = 0
poster = 0

coin = 0

while (count1 < 3):
    row = randint(0, 4)
    column = randint(0, 4)

    if (board[row][column] == '      '):
        board[row][column] = 'PUZZLE'
        count1+=1

while (count2 < 3):
    row = randint(0, 4)
    column = randint(0, 4)

    if (board[row][column] == '      '):
        board[row][column] = ' BALL '
        count2+=1

while (count3 < 3):
    row = randint(0, 4)
    column = randint(0, 4)

    if (board[row][column] == '      '):
        board[row][column] = ' GAME '
        count3+=1

while (count4 < 3):
    row = randint(0, 4)
    column = randint(0, 4)

    if (board[row][column] == '      '):
        board[row][column] = ' DOLL '
        count4+=1

while (count5 < 3):
    row = randint(0, 4)
    column = randint(0, 4)

    if (board[row][column] == '      '):
        board[row][column] = 'POSTER'
        count5+=1

print (board[0])
print (board[1])
print (board[2])
print (board[3])
print (board[4])

while (coin < 10):
    coin+=1

    row = randint(0,4)
    column = randint(0,4)

    if (board[row][column] == 'PUZZLE'):
        puzzle+=1
    if (board[row][column] == ' BALL '):
        ball+=1
    if (board[row][column] == ' GAME '):
        game+=1
    if (board[row][column] == ' DOLL '):
        doll+=1
    if (board[row][column] == 'POSTER'):
        poster+=1

    board[row][column] = 'PENNY '

print ()
print (board[0])
print (board[1])
print (board[2])
print (board[3])
print (board[4])
print ()
print ('Puzzle:',puzzle)
print ('Ball:',ball)
print ('Game:',game)
print ('Doll:',doll)
print ('Poster:',poster)
        
