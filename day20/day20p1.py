# Warning: the stack size increase seems to work fine on my Mac but not on my Windows.
# I recommend looking at my part 2 solution day20p2.py and applying that instead.

import sys
sys.setrecursionlimit(10000)

FILENAME = 'day20.txt'

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            start = (i, j)
        elif input[i][j] == 'E':
            end = (i, j)

def safeCoord(grid, x, y):
    return 0 <= x and x < len(grid) and 0 <= y and y < len(grid[0])

def moves(grid, coord):
    x, y = coord
    moves = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if safeCoord(grid, x + dx, y + dy):
            if grid[x+dx][y+dy] == '#':
                moves.append((x + dx, y + dy, True))
            else:
                moves.append((x + dx, y + dy, False))
    return moves

noCheat = 0
# (x, y, length)
q = [(start[0], start[1], 0)]
visited = {start}
while q:
    x, y, length = q.pop(0)
    if (x, y) == end:
        noCheat = length
        break
    
    visited.add((x, y))
    for (x2, y2, isWall) in moves(input, (x, y)):
        if (x2, y2) not in visited and not isWall:
          q.append((x2, y2, length + 1))

print(f'Shortest solution with no cheats: {noCheat}')

ct = 0
SAVE_THRESHOLD = 100
visited = [[0 for _ in range(len(input[0]))] for _ in range(len(input))]
threshold = noCheat - SAVE_THRESHOLD

def dfs(x, y, cheated, length):
    global end
    global input
    global visited
    global threshold

    # Cheated too much :(
    if length > threshold:
        return 0
    
    if (x, y) == end:
        print(f'End reached with length {length}')
        return 1
    
    visited[x][y] = 1

    paths = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if safeCoord(input, x + dx, y + dy) and visited[x+dx][y+dy] == 0:
            if input[x + dx][y + dy] == '#':
                if not cheated:
                    paths += dfs(x + dx, y + dy, True, length + 1)
            else:
                paths += dfs(x + dx, y + dy, cheated, length + 1)
    
    # Backtrack
    visited[x][y] = 0
    return paths

print(dfs(start[0], start[1], False, 0))
