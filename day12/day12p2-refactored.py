input = []
inputFile = open('day12.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

# Returns boolean indicating if (x, y) is within the bounds of input
def checkSafeCoord(x, y, input):
    return 0 <= x and x < len(input) and 0 <= y and y < len(input[0])

# Returns a tuple of ([cells to move to], [perimeter cells])
def move(x, y, regionVisited, input):
    goodMoves = []
    badMoves = []
    plant = input[x][y]

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        newX = x + dx
        newY = y + dy
        if (newX, newY) not in regionVisited:
            if checkSafeCoord(newX, newY, input) and input[newX][newY] == plant:
                goodMoves.append((newX, newY))
            else:
                badMoves.append((newX, newY))

    return (goodMoves, badMoves)

# Returns the number of sides defined by a perimeter set
def countSides(perimeter):
    # Count how many perimeter pieces are joinable neighbors
    connections = 0
    for (inX, inY), (outX, outY) in perimeter:
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if ((inX + dx, inY + dy), (outX + dx, outY + dy)) in perimeter:
                connections += 1

    # Divide connections by 2 since they're double counted
    return len(perimeter) - (connections // 2)

# Searches input grid to define region occupied by plant at input[i][j]
# Returns 
def searchRegion(input, i, j):
    # Queue BFS for all plants in region
    q = [(i, j)]
    currPlot = {(i, j)}
    perimeter = set()
    
    while q:
        x, y = q.pop(0)
        goodMoves, badMoves = move(x, y, currPlot, input)

        for goodCord in goodMoves:
            q.append(goodCord)
            currPlot.add(goodCord)

        for badCoord in badMoves:
            # Each item in perimeter is nested tuple ((x1, y1), (x2, y2))
            # This defines a line segment between cells (x1, y1) and (x2, y2)
            perimeter.add((badCoord, (x, y)))
            
    return (len(currPlot) * countSides(perimeter), currPlot)

# Main
total = 0
visited = set()
# Iterate through every possible cell as a starting point
for i in range(len(input)):
    for j in range(len(input[0])):
        if (i, j) not in visited:
            # Begin BFS on unvisited cell
            new, newVisited = searchRegion(input, i, j)

            # Update cost and visited set
            total += new
            visited = visited.union(newVisited)

print(total)