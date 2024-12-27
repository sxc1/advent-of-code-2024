
inputGrid = []
inputFile = open('day15.txt', 'r')
HEIGHT = 1
line = inputFile.readline().strip()
while len(line) > 0:
    HEIGHT += 1

    newLine = []
    for char in line:
        if char == 'O':
            newLine.append('[')
            newLine.append(']')
        elif char == '@':
            newLine.append('@')
            newLine.append('.')
        else:
            newLine.append(char)
            newLine.append(char)

    inputGrid.append(newLine)
    line = inputFile.readline().strip()

WIDTH = len(inputGrid[0])

inputSteps = []
step = inputFile.readline().strip()
while step:
    inputSteps.append(step)
    step = inputFile.readline().strip()
inputSteps = ''.join(inputSteps)
    
inputFile.close()

# for row in inputGrid:
#     print(row)
# print('')
# print(inputSteps)

def moveBox(coord, grid, dir):
    dx, dy = dir
    swaps = []
    q = [coord]
    while q:
        x, y = q.pop(0)
        if grid[x][y] == '#':
            break
        if grid[x][y] == '.':
            continue

        x = x + dx
        y = y + dy
        swaps += [(x, y)]
        q += [(x, y)]

        if dx != 0 and grid[x][y] == '[':
            q += [(x, y+1)]
        if dx != 0 and grid[x][y] == ']':
            q += [(x, y-1)]

    # Did not run into wall, can push boxes
    if len(q) == 0 and grid[x][y] != '#':
        swapped = set()
        for x, y in swaps[::-1]:
            if (x, y) in swapped:
                continue
            swapped.add((x, y))
            grid[x][y], grid[x-dx][y-dy] = grid[x-dx][y-dy], grid[x][y]

        # Update position
        coord = (coord[0] + dx, coord[1] + dy)

    return coord, grid

def move(coord, step, grid):
    x, y = coord
    newGrid = list(grid)
    
    if step == '<':
        dx, dy = (0, -1)
    elif step == '^':
        dx, dy = (-1, 0)
    elif step == '>':
        dx, dy = (0, 1)
    elif step == 'v':
        dx, dy = (1, 0)

    if grid[x+dx][y+dy] == '.':
        newCoord = (x + dx, y + dy)

        newGrid[x][y] = '.'
        newGrid[x+dx][y+dy] = '@'
    elif grid[x+dx][y+dy] == '#':
        newCoord, newGrid = (coord, grid)
    else:
        newCoord, newGrid = moveBox(coord, grid, (dx, dy))

    # print(step, newCoord)
    # for row in newGrid:
    #     print(''.join(row))
    return (newCoord, newGrid)
        

def findRobot(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '@':
                return (i, j)

def calcCoord(x, y):
    return 100 * x + y

def calcGrid(grid):
    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == '[':
                gps = calcCoord(x, y)
                total += gps
    return total
        

grid = inputGrid
coord = findRobot(grid)
for step in inputSteps:
    coord, grid = move(coord, step, grid)

print(calcGrid(grid))