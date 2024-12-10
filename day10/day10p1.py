# Time: 11:53 min

input = []
inputFile = open('day10.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

def validNeighbors(x, y, currVal, input):
    valids = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= x + dx and x + dx < len(input) and 0 <= y + dy and y + dy < len(input[0]):
            if int(input[x+dx][y+dy]) == currVal + 1:
                valids.append((x+dx, y+dy, currVal + 1))
    return valids


def scoreTrailhead(i, j, input):
    trailEnds = set()
    q = [(i, j, 0)]
    while q:
        x, y, currVal = q.pop(0)
        if currVal == 9:
            trailEnds.add((x, y))
        else:
            q = q + validNeighbors(x, y, currVal, input)
    return len(trailEnds)



total = 0
for i in range(len(input)):
    for j in range(len(input[0])):
        if input[i][j] == '0':
            total += scoreTrailhead(i, j, input)

print(total)