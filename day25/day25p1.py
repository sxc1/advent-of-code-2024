# Time: 13:59 min

def readLock(block):
    vals = []
    for col in range(5):
        for row in range(6):
            if block[row+1][col] == '.':
                vals.append(row)
                break
    return tuple(vals)

def readKey(block):
    vals = []
    for col in range(5):
        for row in range(6):
            if block[5-row][col] == '.':
                vals.append(row)
                break
    return tuple(vals)

inputLocks = []
inputKeys = []

inputFile = open('day25.txt', 'r')
block = []
for _ in range(7):
    block.append(inputFile.readline().strip())

while block and len(block[0]) > 0:
    if block[0][0] == '#':
        inputLocks.append(readLock(block))
    elif block[0][0] == '.':
        inputKeys.append(readKey(block))
    else:
        print('Input Error:', block)

    inputFile.readline().strip()
    block = []
    for _ in range(7):
        block.append(inputFile.readline().strip())

inputFile.close()
# print(inputLocks)
# print(inputKeys)

pairs = 0
for lock in inputLocks:
    for key in inputKeys:
        match = True
        for col in range(5):
            if lock[col] + key[col] > 5:
                match = False
        if match:
            pairs += 1

print(pairs)