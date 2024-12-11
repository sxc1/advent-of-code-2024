# Time: 6:25 min

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
    
stones = input
for i in range(25):
    newStones = []
    for stone in stones:
        newStones += updateStone(stone)
    stones = newStones
    
print(len(stones))