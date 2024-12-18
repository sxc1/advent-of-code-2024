# Time: 28:52 min

FILENAME = 'day18.txt'
if FILENAME == 'day18sample.txt':
    size = 7
    cutoff = 12
else:
    size = 71
    cutoff = 1024

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append([int(n) for n in line.strip().split(',')])
inputFile.close()

gridDict = {}
for i in range(len(input)):
    gridDict[i] = [[0 for _ in range(size)] for _ in range(size)]

    for j in range(i + 1):
        y, x = input[j]
        gridDict[i][x][y] = 1

def safeNeighbors(grid, x, y):
    safe = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx and x + dx < len(grid) and 0 <= y + dy and y + dy < len(grid[0]):
            if grid[x+dx][y+dy] == 0:
              safe.append((x + dx, y + dy))
    return safe

# Try linear search first and then switch to binary search if necessary
for i in range(len(input)):
    print(f'Checking input {i}')
    safePath = False

    # (x, y, steps)
    q = [(0, 0, 0)]
    visited = {(0, 0)}

    # Queue BFS
    while q:
        x, y, steps = q.pop(0)
        if (x, y) == (size - 1, size - 1):
            safePath = True
            break

        for newX, newY in safeNeighbors(gridDict[i], x, y):
            if (newX, newY) not in visited:
                q.append((newX, newY, steps + 1))
                visited.add((newX, newY))

    if safePath != True:
        print('First unsafe path: ', i, input[i])
        break

# Binary search was not necessary xD