# Time: 11:09 min

input = []
inputFile = open('day4.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

def checkDir(x, y, dx, dy, input):
    if input[x+dx][y+dy] == 'M' and input[x+2*dx][y+2*dy] == 'A' and input[x+3*dx][y+3*dy] == 'S':
        return 1
    else:
        return 0

def checkXmas (x, y, input):
    ct = 0
    
    if 3 <= x:
        ct += checkDir(x, y, -1, 0, input)
        if 3 <= y:
            ct += checkDir(x, y, -1, -1, input)
        if y <= len(input[0]) - 4:
            ct += checkDir(x, y, -1, 1, input)

    if x <= len(input) - 4:
        ct += checkDir(x, y, 1, 0, input)
        if 3 <= y:
            ct += checkDir(x, y, 1, -1, input)
        if y <= len(input[0]) - 4:
            ct += checkDir(x, y, 1, 1, input)

    if 3 <= y:
        ct += checkDir(x, y, 0, -1, input)

    if y <= len(input[0]) - 4:
        ct += checkDir(x, y, 0, 1, input)

    return ct
    


total = 0

for x in range(len(input)):
    for y in range(len(input[0])):
        if input[x][y] == 'X':
            total += checkXmas(x, y, input)

print(total)