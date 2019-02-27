l = [int(num) for num in input().split()]
n = l[0]
q = l[1]
grid = []
event = []

for num in range (n):
    grid.append([])
    for num1 in range (n):
        grid[num].append(0)

print (grid)

for num in range (q):
    for number in input().split():
        event.append(int(number))

for num in range (0, len(event), 3):
    if (event[num] == 2):
        print (grid[event[num+1]][event[num+2]])
    else:
        for num1 in range (n):
            if (grid[num1][event[num+2]] == 0):
                grid[num1][event[num+2]] = 1
            if (grid[num1][event[num+2]] == 1):
                grid[num1][event[num+2]] = 0
        for num2 in range (n):
            if (grid[event[num+1]][num2] == 0):
                grid[event[num+1]][num2] = 1
            if (grid[event[num+1]][num2] == 1):
                grid[event[num+1]][num2] = 0
        grid[event[num+1]][event[num+2]] == 0
        
        if (grid[event[num+1]][event[num+2]] == 1):
            grid[event[num+1]][event[num+2]] = 0
        elif (grid[event[num+1]][event[num+2]] == 0):
            grid[event[num+1]][event[num+2]] = 1
