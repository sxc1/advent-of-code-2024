# Time: ~18 min

input = []
inputFile = open('day8.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

h, w = (len(input), len(input[0]))

def checkSafeCoord(coord, h, w):
    return 0 <= coord[0] and coord[0] < h and 0 <= coord[1] and coord[1] < w

# returns set of locations
def findAntinodes(char, input, h, w):
    locations = []
    for i in range(h):
        for j in range(w):
            if input[i][j] == char:
                locations.append((i, j))
    

    antinodes = set()
    if len(locations) == 0:
        return antinodes
    
    for x1, y1 in locations:
        antinodes.add((x1, y1))

        for x2, y2 in locations:
            if x1 != x2 and y1 != y2:
                dx = x1 - x2
                dy = y1 - y2

                antinode = (x1+dx, y1+dy)
                while checkSafeCoord(antinode, h, w):
                    antinodes.add(antinode)
                    antinode = (antinode[0]+dx, antinode[1]+dy)
                
                antinode = (x2-dx, y2-dy)
                while checkSafeCoord(antinode, h, w):
                    antinodes.add(antinode)
                    antinode = (antinode[0]-dx, antinode[1]-dy)

    return antinodes
                


antinodes = set()
for char in '0123456789' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower():
    newAntinodes = findAntinodes(char, input, h, w)
    if len(newAntinodes) > 0:
      antinodes = antinodes.union(newAntinodes)

print(len(antinodes))