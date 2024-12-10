# Time: 33:45

input = []
inputFile = open('day6.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

h, w = len(input), len(input[0])
startx, starty = 43, 52

def rotate(dir):
    if dir == (-1, 0):
        return (0, 1)
    if dir == (0, 1):
        return (1, 0)
    if dir == (1, 0):
        return (0, -1)
    if dir == (0, -1):
        return (-1, 0)

ct = 0
# Choose obstruction location
for i in range(h):
    for j in range(w):
        x, y = startx, starty
        dir = (-1, 0)
        visited = set()

        # I wasted >15 minutes because I typed "and" here instead of "or" :|
        if i != startx or j != starty:
            while 0 <= x+dir[0] and x+dir[0] < h and 0 <= y+dir[1] and y+dir[1] < w:
                # Mark current spot + orientation as visited
                visited.add((x, y, dir[0], dir[1]))

                # Move
                if input[x+dir[0]][y+dir[1]] == '#' or x+dir[0] == i and y+dir[1] == j:
                    dir = rotate(dir)
                else:
                    x, y = (x + dir[0], y + dir[1])

                # Loop found
                if (x, y, dir[0], dir[1]) in visited:
                    ct += 1
                    break

print(ct)