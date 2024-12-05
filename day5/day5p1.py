# Time: 8:14 min

inputRules = []
inputFile = open('day5rules.txt', 'r')
for line in inputFile:
    inputRules.append(line.strip())
inputFile.close()

inputOrders = []
inputFile = open('day5orders.txt', 'r')
for line in inputFile:
    inputOrders.append(line.strip())
inputFile.close()

illegals = {}
for rule in inputRules:
    a, b = rule.split('|')[0], rule.split('|')[1]
    if b not in illegals:
        illegals[b] = []
    illegals[b].append(a)

total = 0
for order in inputOrders:
    orderList = order.split(',')
    good = True
    for i in range(len(orderList)):
        for illegal in illegals[orderList[i]]:
            if illegal in orderList[i+1:]:
                good = False
    if good:
        total += int(orderList[len(orderList)//2])
        
print(total)