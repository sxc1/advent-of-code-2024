# Time: 4:11 min

leftInput = []
rightInput = []
inputFile = open('day1.txt', 'r')
for line in inputFile:
    lineList = line.strip().split('   ')
    leftInput.append(int(lineList[0]))
    rightInput.append(int(lineList[1]))
inputFile.close()

leftInput.sort()
rightInput.sort()

total = 0
for i in range(len(leftInput)):
    total += abs(leftInput[i] - rightInput[i])

print(total)