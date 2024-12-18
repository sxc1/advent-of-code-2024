# WIDTH = 11
# HEIGHT = 7
WIDTH = 101
HEIGHT = 103
MOVES = 100

def parseCoord(coord):
    x, y = coord.split(',')
    return (int(x), int(y))

def readLine(line):
    p, v = line[2:].split(' v=')
    return (parseCoord(p), parseCoord(v))

input = []
inputFile = open('day14.txt', 'r')
for line in inputFile:
    input.append(readLine(line.strip()))
inputFile.close()

def calcFinalPos(pos, vel, w, h, moves):
    xFinal = (pos[0] + vel[0] * moves) % w
    yFinal = (pos[1] + vel[1] * moves) % h

    if xFinal < 0:
        xFinal += w
    if yFinal < 0:
        yFinal += h

    return (xFinal, yFinal)

def findQuadrant(pos, w, h):
    x, y = pos
    if 0 <= x and x < w // 2:
        if 0 <= y and y < h // 2:
            return 1
        
        if h // 2 < y and y < h:
            return 3
        
    if w // 2 < x and x < w:
        if 0 <= y and y < h // 2:
            return 2
        
        if h // 2 < y and y < h:
            return 4
    
    return 0
    

def calcSafetyFactor(positions, w, h):
    # [discards, q1, q2, q3, q4]
    quadrantCt = [0, 0, 0, 0, 0]
    for pos in positions:
        quadrantCt[findQuadrant(pos, w, h)] += 1
    print(quadrantCt)
    return quadrantCt[1] * quadrantCt[2] * quadrantCt[3] * quadrantCt[4]


finalPositions = []
for pos, vel in input:
    finalPositions.append(calcFinalPos(pos, vel, WIDTH, HEIGHT, MOVES))

print(calcSafetyFactor(finalPositions, WIDTH, HEIGHT))
