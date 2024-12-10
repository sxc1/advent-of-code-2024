# Time: 55:20 min

input = []
inputFile = open('day9.txt', 'r')
for line in inputFile:
    input = (line.strip())
inputFile.close()

def createBlocks(diskmap):
    blocks = []

    for i in range((len(diskmap) + 1)// 2):
        if diskmap[2*i] != '0':
            blocks.append((int(diskmap[2*i]), i))

        if (2 * i + 1) < len(diskmap) and diskmap[2*i+1] != '0':
            blocks.append((int(diskmap[2*i+1]), '.'))

    return blocks

# (count, id/'.')
blocks = createBlocks(input)

# Search backwards for file ids
i = len(blocks) - 1
while i > 0:
    if blocks[i][1] == '.':
        i -= 1
    else:
        rightSize = blocks[i][0]

        # Search forwards for spaces
        j = 0
        while j < i:
            leftSize = blocks[j][0]

            if blocks[j][1] == '.' and leftSize == rightSize:
                # Shallow copy so I don't need to think
                blocks[j] = (rightSize, blocks[i][1])
                blocks[i] = (leftSize, '.')
                i -= 1
                break
            elif blocks[j][1] == '.' and leftSize > rightSize:
                blocks = blocks[:j] + [(rightSize, blocks[i][1]), (leftSize - rightSize, '.')] + blocks[j+1:i] + [(rightSize, '.')] + blocks[i+1:]
                # Don't decrement i because added a new element at j
                break
            else:
                j += 1

        if j >= i:
            i -= 1



newBlocks = []
for block in blocks:
    newBlocks = newBlocks + [block[1]] * block[0]


def checksum(blocks):
    total = 0
    for i in range(len(blocks)):
        if blocks[i] != '.':
            total += i * blocks[i]
    return total

print(checksum(newBlocks))