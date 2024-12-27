from collections import defaultdict

inputs = {}
xbits = []
ybits = []
inputFile = open('day24.txt', 'r')
line = inputFile.readline().strip()
while len(line) > 0:
    wire, bit = line.split(': ')
    inputs[wire] = int(bit)
    line = inputFile.readline().strip()

    if wire[0] == 'x':
        xbits.append(wire)
    elif wire[0] == 'y':
        ybits.append(wire)

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

print(gates)
print('')
print(wireValues)
print('')
print(zbits)
print('')

# PART 2 PURE EXPLORATION
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

xbits.sort(reverse = True)
xbin = ''
for x in xbits:
    xbin = xbin + str(wireValues[x])
print(f'x input: {xbin}')
xval = int(xbin, 2)

ybits.sort(reverse = True)
ybin = ''
for y in ybits:
    ybin = ybin + str(wireValues[y])
print(f'y input: {ybin}')
yval = int(ybin, 2)

zbin = ''
for z in zbits:
    zbin = zbin + str(wireValues[z])
zval = int(zbin, 2)
print(f'z output: {zbin}')

diffbin = format(xval + yval - zval, 'b')
print(f'x + y - z: {diffbin}')

# Difference = 1000010000010000000
print('(manual) bad z bits = z07, z13, z18\n')

# PART 2 CODING BEGINS
def isInput(wire):
    return wire[0] in 'xy'

# key : value = input wire : [ list of gates it's used in ]
usageMap = defaultdict(list)
for outputWire in gates:
    left, op, right = gates[outputWire]
    usageMap[left].append((left, op, right, outputWire))
    usageMap[right].append((left, op, right, outputWire))

swaps = set()
for outputWire in gates:
    left, op, right = gates[outputWire]
    # Edge case - first input and last output are safe
    if left == 'x00' or outputWire == 'z45':
        continue

    # I did not come up with these cases. They are determined by sanity checks for a
    # ripple-carry adder: https://en.wikipedia.org/wiki/Adder_(electronics)#Ripple-carry_adder

    # Case 1: XOR gates must:
    # Case 1a: either combine two input (x/y) wires
    # Case 1b: or output to an output (z) wire (z00 is exception)
    # Case 1c: but not both
    # Case 1d: feed into exactly 1 AND + 1 XOR gate
    if op == 'XOR':
        if isInput(left):
            if not isInput(right):
                # Case 1a
                swaps.add(outputWire)
                print(left, op, right, '->', outputWire, 'only 1 is an input')
            if outputWire[0] == 'z' and outputWire != 'z00':
                # Case 1c
                swaps.add(outputWire)
                print(left, op, right, '->', outputWire, 'output is a z when using an input')
            # Case 1d
            usage = usageMap[outputWire]
            usageOps = [o[1] for o in usage]
            if outputWire != 'z00' and sorted(usageOps) != ['AND', 'XOR']:
                swaps.add(outputWire)
                print(left, op, right, '->', outputWire, 'wrong subsequent gates', usage)
        else:
            if outputWire[0] != 'z':
                # Case 1b
                swaps.add(outputWire)
                print(left, op, right, '->', outputWire, 'output was not a z')
    # Case 2: AND gates must both:
    # Case 2a: combine two or zero input (x/y) wires
    # Case 2b: feed into an OR gate
    elif op == 'AND':
        if isInput(left):
            if not isInput(right):
                # Case 2a
                swaps.add(outputWire)
                print(left, op, right, '->', outputWire, 'only 1 is an input')
        # Case 2b
        usage = usageMap[outputWire]
        if [o[1] for o in usage] != ['OR']:
            swaps.add(outputWire)
            print(left, op, right, '->', outputWire, 'wrong subsequent gates', usage)
    # Case 3: OR gates must:
    # Case 3a: not utilize input (x/y) wires
    # Case 3b: feed into exactly 1 AND + 1 XOR gate
    elif op == 'OR':
        if isInput(left) or isInput(right):
            # Case 3a
            swaps.add(outputWire)
            print(left, op, right, '->', outputWire, 'used an input')
        usage = usageMap[outputWire]
        usageOps = [o[1] for o in usage]
        if sorted(usageOps) != ['AND', 'XOR']:
            # Case 3b
            swaps.add(outputWire)
            print(left, op, right, '->', outputWire, 'wrong subsequent gates', usage)

print(','.join(sorted(swaps)))