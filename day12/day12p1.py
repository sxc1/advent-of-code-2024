# Time: 42:11 min

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

def searchRegion(input, i, j, visited):
    plant = input[i][j]
    # BFS for all plants in region
    currPlot = {(i, j)}
    perimeter = []
    q = []
    q.append((i, j))
    
    while q:
        x, y = q.pop(0)
        moves = move(x, y, currPlot, input, plant)

        for newX, newY in moves[0]:
            q.append((newX, newY))
            currPlot.add((newX, newY))

        for a, b in moves[1]:
            perimeter.append((a, b))
            
        
    # Area = count
    # Perimeter = 2 * (width + height)
    visited = visited.union(currPlot)
    print(i, j, input[i][j], len(currPlot), len(perimeter), len(currPlot) * len(perimeter))
    return (len(currPlot) * len(perimeter), visited)

    # add new visited to visited
    # return A * P

total = 0
visited = set()
for i in range(len(input)):
    for j in range(len(input[0])):
        if (i, j) not in visited:
            new, newVisited = searchRegion(input, i, j, visited)
            total += new
            visited = visited.union(newVisited)

print(total)