# Time: 23:40 min

input = []
inputFile = open('day9.txt', 'r')
for line in inputFile:
    input = (line.strip())
inputFile.close()

def createBlocks(diskmap):
    blocks = []
    for i in range((len(diskmap) + 1)// 2):
        blocks = blocks + [i] * int(diskmap[2*i])
        if (2 * i + 1) < len(diskmap):
            blocks = blocks + ['.'] * int(diskmap[2*i+1])
    return blocks

blocks = createBlocks(input)

# 2 pointer
# left searches for next '.'
# right searches for next int
left = 0
right = len(blocks) - 1

while left < right:
    while left < right and blocks[left] != '.':
        left += 1
    while right > left and blocks[right] == '.':
        right -= 1
    if left < right:
        blocks[left] = blocks[right]
        blocks[right] = '.'
        left += 1
        right -= 1

def checksum(blocks):
    total = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            total += i * int(blocks[i])
        else:
            break
    return total

print(checksum(blocks))