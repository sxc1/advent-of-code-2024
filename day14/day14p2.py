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

# This problem is not great - the idea is cute but the actual determination of
# "do the robots form a Christmas tree" is really "are there no overlapping robots"
# which is not a logical conclusion.
def checkBounds(positions):
    return len(positions) == len(set(positions))

for i in range(1, 10000):
  finalPositions = []
  for pos, vel in input:
      finalPositions.append(calcFinalPos(pos, vel, WIDTH, HEIGHT, i))

  if checkBounds(finalPositions):
    print(i) 
    output = [[0 for _ in range(HEIGHT)] for _ in range(WIDTH)]
    for x, y in finalPositions:
        output[x][y] += 1

    outputFile = open(f'outputs/{i}moves.txt', 'w')
    for row in output:
        outputFile.write((' ').join([str(n) if n > 0 else ' ' for n in row]) + '\n')
    outputFile.close()