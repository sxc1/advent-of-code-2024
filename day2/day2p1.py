# Time: 6 min

input = []
inputFile = open('day2.txt', 'r')
for line in inputFile:
    lineList = line.strip().split(' ')
    input.append([int(n) for n in lineList])
inputFile.close()

ct = 0

def safeDiff(a, b, isIncreasing):
    if isIncreasing:
        return (1 <= b - a) and (b - a <= 3)
    else:
        return (1 <= a - b) and (a - b <= 3)

for report in input:
    if report[0] < report[1]:
        isIncreasing = True
    elif report[0] > report[1]:
        isIncreasing = False
    else:
        continue

    bad = False
    for i in range(len(report) - 1):
        if not safeDiff(report[i], report[i+1], isIncreasing):
            bad = True
            
    if bad == False:
        ct += 1

print(ct)