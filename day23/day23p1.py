# Time: 8:33 min

input = []
inputFile = open('day23.txt', 'r')
for line in inputFile:
    input.append(line.strip().split('-'))
inputFile.close()

# { key : value } = { computer : set(connected computers) }
network = {}
# 3 computer sets, represented as sorted tuples
sets = set()

for com1, com2 in input:

    if com1 in network and com2 in network:
        # Existing mutual -> "new" 3 computer set
        mutuals = network[com1].intersection(network[com2])
        for mutual in mutuals:
            sets.add(tuple(sorted([mutual, com1, com2])))

    # Add to graph
    if com1 not in network:
        network[com1] = set()
    if com2 not in network:
        network[com2] = set()
    network[com1].add(com2)
    network[com2].add(com1)

print(f'Total sets: {len(sets)}')

total = 0
for a, b, c in sets:
    if a[0] == 't' or b[0] == 't' or c[0] == 't':
        total += 1
print(f'Sets starting with "t": {total}')