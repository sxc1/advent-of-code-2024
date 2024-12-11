# Time: 1:24:30 hr
# I tried a way different, mathematical solution first which failed

input = []
inputFile = open('day11.txt', 'r')
for line in inputFile:
    input = line.strip().split(' ')
inputFile.close()

def updateStone(stone):
    if stone == '0':
        return ['1']
    elif len(stone) % 2 == 0:
        return [str(int(stone[:len(stone)//2])), str(int(stone[len(stone)//2:]))]
    else:
        return [str(int(stone) * 2024)]
    
stones = { stone : 1 for stone in input}
for i in range(75):
    newStones = {}
    for stone in stones.keys():
        additionals = updateStone(stone)
        for additional in additionals:
            if additional in newStones:
                newStones[additional] += stones[stone]
            else:
                newStones[additional] = stones[stone]
    stones = newStones

print(sum(stones.values()))