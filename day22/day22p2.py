# Time: 53:25 min

FILENAME = 'day22.txt'

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append(int(line.strip()))
inputFile.close()

def prune(n):
    # return n % 16777216
    # Bit speedhack
    return n & 16777215

def step1(n):
    return prune((n << 6) ^ n)

def step2(n):
    return prune((n >> 5) ^ n)

def step3(n): 
    return prune((n << 11 ^ n))

def calcNext(n):
    return step3(step2(step1(n)))

# {key : value} = {(a, b, c, d) : {input index : bananas}}
bananaDict = {}
for i, n in enumerate(input):
    secret = n
    digit = n % 10
    seq = []

    for _ in range(2000):
        secret = calcNext(secret)

        # Build up possible sequences in memory for fast access later
        diff = (secret % 10) - digit
        digit = secret % 10

        # Update current sequence of last 4 changes
        seq.append((diff))
        if len(seq) > 4:
            seq.pop(0)
        if len(seq) == 4:
            tup = tuple(seq)
            if tup not in bananaDict:
                bananaDict[tup] = {}
            if i not in bananaDict[tup]:
                # Add sale from sequence + buyer combo
                bananaDict[tup][i] = digit
        
maxB = 0
for tup in bananaDict:
    bananas = sum(bananaDict[tup].values())
    if bananas > maxB:
        maxB = bananas
print(maxB)