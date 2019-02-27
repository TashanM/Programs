# 2D Lists 3
# Tashan Maniyalaghan
# 693776
# ICS4U0
# 7 Febuary 2019
# Mr. Veera

one = [78, 98, 54, 84, 100]
two = [45, 78, 56, 89, 85]
three = [78, 63, 69, 91, 74]
four = [23, 95, 49, 47, 58]
five = [98, 94, 96, 97, 91]
six = [12, 32, 65, 45, 78]
seven = [45, 78, 56, 45, 89]
eight = [78, 45, 89, 56, 45]
nine = [89, 87, 54, 89, 54]
ten = [23, 56, 89, 78, 45]
eleven = [12, 45, 98, 56, 23]
twelve = [45, 78, 45, 12, 56]
classroom = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]

function = int(input())

if (function == 1):
    for num in range (len(classroom)):
        print (classroom[num])

if (function == 2):
    student = int(input())
    student-=1
    total = 0

    for num in range (len(classroom[student])):
        total+=classroom[student][num]

    total = total/5
    print (total)

if (function == 3):
    test = int(input())
    test-=1
    total = 0

    for num in range (len(classroom)):
        total+=classroom[num][test]

    total = total/12
    print(total)
