# Time: 8:33 min

input = []
inputFile = open('day6.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

h, w = len(input), len(input[0])
visited = set()

# speed
x, y = 43, 52
print(input[x][y])
dir = (-1, 0)

def rotate(dir):
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (1, 0)
    if dir == (1, 0):
        return (0, -1)
    if dir == (0, -1):
        return (-1, 0)

while 0 <= x and x < h and 0 <= y and y < w:
    visited.add((x, y))
    if input[x+dir[0]][y+dir[1]] == '#':
        dir = rotate(dir)
    else:
        x, y = (x + dir[0], y + dir[1])

print(len(visited))