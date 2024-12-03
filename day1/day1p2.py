# Time: 7:12 min

leftInput = []
rightInput = []
inputFile = open('day1.txt', 'r')
for line in inputFile:
    lineList = line.strip().split('   ')
    leftInput.append(int(lineList[0]))
    rightInput.append(int(lineList[1]))
inputFile.close()

left = set(leftInput)
rightFreqs = { n : rightInput.count(n) for n in rightInput }

total = 0
for n in left:
    if n in rightFreqs:
        total += n * rightFreqs[n]

print(total)