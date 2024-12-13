# Time: 1:19:17 hr

import numpy as np

inputA = []
inputB = []
inputPrize = []

def parseline(line, prefix):
    xy = line[len(prefix):]
    x, y = xy.split(', ')
    if prefix == 'Prize: ':
        return (10000000000000 + int(x[2:]), 10000000000000 + int(y[2:]))
    else:
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
    # Edge case
    if buttonA[0] / buttonA[1] == buttonB[0] / buttonB[1]:
        if prize[0] % buttonB[0] == 0 and prize[1] % buttonB[1] == 0:
            return prize[0] // buttonB[0]
        else:
            return None

    # Solve system of 2 linear eqs using matrices
    coeffs = np.array([[buttonA[0], buttonB[0]], [buttonA[1], buttonB[1]]])
    consts = np.array([prize[0], prize[1]])
    presses = np.linalg.solve(coeffs, consts)

    # Round and double check to resolve floats
    pressesA = round(presses[0])
    pressesB = round(presses[1])
    if pressesA * buttonA[0] + pressesB * buttonB[0] == prize[0] and pressesA * buttonA[1] + pressesB * buttonB[1] == prize[1]:
        return 3 * pressesA + pressesB
    
    # No solution
    return None
            
totalCost = 0
for i in range(len(inputPrize)):
    cost = calcCost(inputA[i], inputB[i], inputPrize[i])
    if cost:
        totalCost += cost
print(totalCost)
