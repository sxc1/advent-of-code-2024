# Time: 1:04:37 hr :(

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

# Rules are symmetric
forward = {}
backward = {}
for rule in inputRules:
    a, b = rule.split('|')[0], rule.split('|')[1]
    if a not in forward:
        forward[a] = set()
    forward[a].add(b)
    if b not in backward:
        backward[b] = set()
    backward[b].add(a)


# Assume there's only one correct ordering strictly defined by the rules + path dict
total = 0
for order in inputOrders:
    # Copied from part 1
    orderList = order.split(',')
    good = True
    for i in range(len(orderList)):
        for illegal in backward[orderList[i]]:
            if illegal in orderList[i+1:]:
                good = False

    if not good:
      unvisited = order.split(',')
      path = [unvisited[-1]]
      unvisited.pop()

      while len(unvisited) > 0:
        curr = unvisited.pop()
        for i in range(len(path)):
            n = path[i]
            if n in forward and curr in forward[n]:
                while i < len(path) and path[i] in forward and curr in forward[path[i]]:
                    i += 1
                path.insert(i, curr)
                break
            elif n in backward and curr in backward[n]:
                path.insert(i, curr)
                break

      total += int(path[len(path)//2])

print(total)