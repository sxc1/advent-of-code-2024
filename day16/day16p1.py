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
visited = set()
# Use heapq/priority queue to optimize
heapq.heapify(q)

# Queue BFS
while q:
    cost, pos, dir = heapq.heappop(q)
    if (pos, dir) not in visited:
        visited.add((pos, dir))
        if pos == end:
            print(cost)
            break
        else:
            for mv in moves(input, pos, dir, cost):
                heapq.heappush(q, mv)