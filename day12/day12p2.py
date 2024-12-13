input = []
inputFile = open('day12.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

def move(x, y, regionVisited, input, plant):
    moves = []
    badMoves = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newX = x + dx
        newY = y + dy

        if (newX, newY) not in regionVisited:
            if 0 <= newX and newX < len(input) and 0 <= newY and newY < len(input[0]) and input[newX][newY] == plant:
                moves.append((newX, newY))
            else:
                badMoves.append((newX, newY))
                
    return (moves, badMoves)

def countSides(perimeter):
    connections = 0
    for (inX, inY), (outX, outY) in perimeter:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if ((inX + dx, inY + dy), (outX + dx, outY + dy)) in perimeter:
                connections += 1
    return len(perimeter) - (connections // 2)


def searchRegion(input, i, j, visited):
    plant = input[i][j]
    # BFS for all plants in region
    currPlot = {(i, j)}
    perimeter = set()
    q = []
    q.append((i, j))
    
    while q:
        x, y = q.pop(0)
        moves = move(x, y, currPlot, input, plant)

        for newX, newY in moves[0]:
            q.append((newX, newY))
            currPlot.add((newX, newY))

        for a, b in moves[1]:
            perimeter.add(((x, y), (a, b)))

    area = len(currPlot)
    sides = countSides(perimeter)
    visited = visited.union(currPlot)

    return (area * sides, visited)

total = 0
visited = set()
for i in range(len(input)):
    for j in range(len(input[0])):
        if (i, j) not in visited:
            new, newVisited = searchRegion(input, i, j, visited)
            total += new
            visited = visited.union(newVisited)

print(total)