# Time: 17:55 min

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

grid = [[0 for _ in range(size)] for _ in range(size)]
for i in range(min(cutoff, len(input))):
    y, x = input[i]
    grid[x][y] = 1

def safeNeighbors(grid, x, y):
    safe = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx and x + dx < len(grid) and 0 <= y + dy and y + dy < len(grid[0]):
            if grid[x+dx][y+dy] == 0:
              safe.append((x + dx, y + dy))
    return safe

# (x, y, steps)
q = [(0, 0, 0)]
visited = {(0, 0)}

# Queue BFS
while q:
    x, y, steps = q.pop(0)
    if (x, y) == (size - 1, size - 1):
        print(steps)
        break

    for newX, newY in safeNeighbors(grid, x, y):
        if (newX, newY) not in visited:
            q.append((newX, newY, steps + 1))
            visited.add((newX, newY))