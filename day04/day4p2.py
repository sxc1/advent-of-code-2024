# Time: 16:32 min
input = []
inputFile = open('day4.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()


def checkXmas (x, y, input):
    xchars = [input[x+coord[0]][y+coord[1]] for coord in [(-1, -1), (-1, 1), (1, -1), (1, 1)]]
    if sorted(xchars) == ['M', 'M', 'S', 'S'] and input[x-1][y-1] != input[x+1][y+1]:
        return True
    return False

total = 0

for x in range(1, len(input) - 1):
    for y in range(1, len(input[0]) - 1):
        if input[x][y] == 'A' and checkXmas(x, y, input):
            total += 1

print(total)