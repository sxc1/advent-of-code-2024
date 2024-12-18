inputGrid = []
inputFile = open('day15.txt', 'r')
inputGrid.append(inputFile.readline().strip())
WIDTH = len(inputGrid[0])
HEIGHT = 1

while inputGrid[-1] != inputGrid[0] or len(inputGrid) == 1:
    HEIGHT += 1
    inputGrid.append(inputFile.readline().strip())
inputGrid = [list(s) for s in inputGrid]

inputFile.readline()
inputSteps = []
step = inputFile.readline()
while step:
    inputSteps.append(step.strip())
    step = inputFile.readline()
inputSteps = ''.join(inputSteps)
inputFile.close()

def moveChar(coord1, coord2, grid):
    charA = grid[coord1[0]][coord1[1]]
    grid[coord2[0]][coord2[1]] = charA
    grid[coord1[0]][coord1[1]] = '.'
    return grid

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
        mult = 2
        newCoord = (x, y)

        while grid[x+mult*dx][y+mult*dy] == 'O':
            mult += 1

        if grid[x+mult*dx][y+mult*dy] == '.':
            newGrid = moveChar((x + dx, y + dy), (x + mult * dx, y + mult * dy), newGrid)
            newGrid = moveChar((x, y), (x + dx, y + dy), newGrid)
            newCoord = (x + dx, y + dy)

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
            if grid[x][y] == 'O':
                gps = calcCoord(x, y)
                total += gps
    return total
        

grid = inputGrid
coord = findRobot(grid)
for step in inputSteps:
    coord, grid = move(coord, step, grid)

print(calcGrid(grid))