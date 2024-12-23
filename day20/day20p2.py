FILENAME = 'day20.txt'
CHEAT_LIMIT = 20

if FILENAME == 'day20.txt':
    SAVE_THRESHOLD = 100
else:
    SAVE_THRESHOLD = 70

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append(list(line.strip()))
inputFile.close()

# Store coord of start and end
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


# (x, y, length)
q = [(start[0], start[1], 0)]
visited = {start}
nonWalls = []

# Queue BFS to fill non wall cells with their maze distance from start
while q:
    x, y, length = q.pop(0)
    input[x][y] = length
    nonWalls.append((x, y))
    
    visited.add((x, y))
    for (x2, y2, isWall) in moves(input, (x, y)):
        if (x2, y2) not in visited and not isWall:
          q.append((x2, y2, length + 1))

ct = 0
# Brute force possible (cheat start, cheat end) combos
for i in range(len(nonWalls)):
    for j in range(i + 1, len(nonWalls)):
        x1, y1 = nonWalls[i]
        x2, y2 = nonWalls[j]

        cheatJump = input[x2][y2] - input[x1][y1]
        cheatDistance = abs(x1 - x2) + abs(y1 - y2)

        # If cheat length and steps saved are valid
        if cheatDistance <= CHEAT_LIMIT and cheatDistance + SAVE_THRESHOLD <= cheatJump:
            ct += 1

print(ct)