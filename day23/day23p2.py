# Time: 17:17 min

import networkx as nx

input = []
inputFile = open('day23.txt', 'r')
for line in inputFile:
    input.append(line.strip().split('-'))
inputFile.close()

# Build graph
network = {}
for com1, com2 in input:
    if com1 not in network:
        network[com1] = []
    if com2 not in network:
        network[com2] = []
    network[com1].append(com2)
    network[com2].append(com1)

# Crutch :P
graph = nx.Graph(network)
print(','.join(sorted(max(nx.algorithms.clique.find_cliques(graph), key = len))))