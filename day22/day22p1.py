# Time: 23:36 min

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

total = 0
for n in input:
    secret = n
    for i in range(2000):
        secret = calcNext(secret)
    print(secret)
    total += secret

print(f'Sum: {total}')