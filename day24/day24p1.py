# Time: 23:05 min

inputs = {}
inputFile = open('day24.txt', 'r')
line = inputFile.readline().strip()
while len(line) > 0:
    wire, bit = line.split(': ')
    inputs[wire] = int(bit)
    line = inputFile.readline().strip()

# key : value = wire output : (input 1, logic gate, input 2)
gates = {}
wireValues = inputs
zbits = []
line = inputFile.readline().strip()
while line:
    left, right = line.split(' -> ')
    wireValues[right] = None
    gates[right] = tuple(left.split(' '))

    if right[0] == 'z':
        zbits.append(right)
    line = inputFile.readline().strip()
zbits.sort(reverse = True)
inputFile.close()

# print(gates)
# print('')
# print(wireValues)
# print('')
# print(zbits)
# print('')

def runGate(input1, input2, operator):
    a = wireValues[input1]
    b = wireValues[input2]
    if operator == 'AND':
        return (a & b)
    if operator == 'OR':
        return (a | b)
    if operator == 'XOR':
        return (a ^ b)
    
changed = True
while changed:
    changed = False
    for wire in wireValues:
        if wireValues[wire] == None:
            left, operator, right = gates[wire]
            if wireValues[left] != None and wireValues[right] != None:
                changed = True
                wireValues[wire] = runGate(left, right, operator)

# print(wireValues)
output = ''
for z in zbits:
    output = output + str(wireValues[z])
print(int(output, 2))