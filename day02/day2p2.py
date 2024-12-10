# Time: 26 min

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
    
def badReport(report):
    if len(report) < 2:
        return -1
    
    if report[0] < report[1]:
        isIncreasing = True
    elif report[0] > report[1]:
        isIncreasing = False
    else:
        return 0
    
    for i in range(len(report) - 1):
        if not safeDiff(report[i], report[i+1], isIncreasing):
            return i + 1
        
    return -1

for report in input:
    badIndex = badReport(report)
    if badIndex == -1:
        ct += 1
    else:
        goodReport = False
        for i in range(len(report)):
            if badReport(report[:i] + report[i+1:]) == -1:
                goodReport = True
                break

        if goodReport:
            ct += 1
        else:
            print(report)
            
print(ct)