# Time: 34:53 min

inputA = []
inputB = []
inputPrize = []

def parseline(line, prefix):
    xy = line[len(prefix):]
    x, y = xy.split(', ')
    return (int(x[2:]), int(y[2:]))

inputFile = open('day13.txt', 'r')
for line in inputFile:
    line = line.strip()
    if line.startswith('Button A: '):
        inputA.append(parseline(line, 'Button A: '))
    elif line.startswith('Button B: '):
        inputB.append(parseline(line, 'Button B: '))
    elif line.startswith('Prize: '):
        inputPrize.append(parseline(line, 'Prize: '))
inputFile.close()


def calcCost(buttonA, buttonB, prize):
    for i in range(101, 1, -1):
        remainderX = prize[0] - buttonB[0] * i
        remainderY = prize[1] - buttonB[1] * i
        if remainderX % buttonA[0] == 0 and remainderY % buttonA[1] == 0:
            if remainderX / buttonA[0] == remainderY / buttonA[1]:
                if remainderX / buttonA[0] <= 100:
                    return i + 3 * int(remainderX / buttonA[0])
    return None
            


totalCost = 0
for i in range(len(inputPrize)):
    cost = calcCost(inputA[i], inputB[i], inputPrize[i])
    if cost:
        totalCost += cost
print(totalCost)
