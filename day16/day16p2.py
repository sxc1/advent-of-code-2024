import heapq

input = []
inputFile = open('day16.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == 'S':
            start = (i, j)
        elif input[i][j] == 'E':
            end = (i, j)

def safeNeighbors(grid, pos, dir):
    safe = []
    x, y = pos
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx and x + dx < len(grid) and 0 <= y + dy and y + dy < len(grid[0]):
            if grid[x+dx][y+dy] != '#' and dir != (-dx, -dy):
              safe.append(((x + dx, y + dy), (dx, dy)))
    return safe


def moves(grid, pos, dir, cost):
    mvs = []
    for newPos, newDir in safeNeighbors(grid, pos, dir):
        if dir == newDir:
            newCost = cost + 1
        else:
            newCost = cost + 1001
        mvs.append((newCost, newPos, newDir))
    return mvs
            

def updateCost(old, new):
    if old == -1 or new < old:
        return new
    return old

# (cost, pos, dir)
q = [(0, start, (0, 1))]
bestCost = -1

# key : value = (cell, dir) : {coordinates forming path to (cell, dir)}
visited = {(start, (0, 1)): set()}

# Use heapq/priority queue to optimize
heapq.heapify(q)

while q:
    cost, pos, dir = heapq.heappop(q)
    if bestCost == -1 or cost == bestCost:
        if pos == end:
            bestCost = updateCost(bestCost, cost)
        elif bestCost == -1 or cost < bestCost:
            for newCost, newPos, newDir in moves(input, pos, dir, cost):
                if (newPos, newDir) in visited:
                    visited[(newPos, newDir)] = visited[(newPos, newDir)].union(visited[(pos, dir)])
                else:
                    heapq.heappush(q, (newCost, newPos, newDir))
                    visited[(newPos, newDir)] = visited[(pos, dir)].union({(pos, dir)})
    
print(bestCost)
paths = 0
for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    if (end, dir) in visited:
        paths += len(visited[(end, dir)])
paths += 1
print(paths)