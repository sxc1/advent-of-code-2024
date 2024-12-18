input = []
inputFile = open('day17.txt', 'r')

# Get registers
registerA = int(inputFile.readline().strip().split('A: ')[1])
registerB = int(inputFile.readline().strip().split('B: ')[1])
registerC = int(inputFile.readline().strip().split('C: ')[1])
# Line break
inputFile.readline()
# Program
inputString = inputFile.readline().strip()[len('Program: '):]
input = [int(n) for n in inputString.split(',')]
inputFile.close()
print(registerA, registerB, registerC)
print(inputString)

def getCombo(operand, registers):
    a, b, c = registers
    if 0 <= operand <= 3:
        return operand
    elif operand == 4:
        return a
    elif operand == 5:
        return b
    elif operand == 6:
        return c
    else:
        print(f'Error in getCombo(): operand = {operand}')
        return

# Updated these to all use bit operations instead of integer math for faster calc
def adv(operand, registers):
    a, b, c = registers
    return (a >> getCombo(operand, registers), b, c)
    
def bxl(operand, registers):
    a, b, c = registers
    return (a, b ^ operand, c)

def bst(operand, registers):
    a, b, c = registers
    return (a, getCombo(operand, registers) & 7, c)

def jnz(operand, registers, i):
    a, b, c = registers
    if a == 0:
        return i + 2
    else:
        return operand

def bxc(operand, registers):
    a, b, c = registers
    return (a, b ^ c, c)

def out(operand, registers):
    return str(getCombo(operand, registers) & 7)

def bdv(operand, registers):
    a, b, c = registers
    return (a, a >> getCombo(operand, registers), c)

def cdv(operand, registers):
    a, b, c = registers
    return (a, b, a >> getCombo(operand, registers))

# Optimized brute force
start = 1
for outputIdx in range(1, len(input) + 1):
    # Build partial output to brute force with part 1 code
    partialOutput = ','.join([str(n) for n in input][-outputIdx:])

    for a in range(start, start * 8):
        i = 0
        output = ''
        registers = (a, registerB, registerC)
        while i + 1 < len(input):
            instruction = input[i]
            operand = input[i+1]

            if instruction == 0:
                registers = adv(operand, registers)
            elif instruction == 1:
                registers = bxl(operand, registers)
            elif instruction == 2:
                registers = bst(operand, registers)
            elif instruction == 3:
                i = jnz(operand, registers, i)
                # Offset i += 2 later
                i -= 2
            elif instruction == 4:
                registers = bxc(operand, registers)
            elif instruction == 5:
                output += out(operand, registers) + ','
            elif instruction == 6:
                registers = bdv(operand, registers)
            elif instruction == 7:
                registers = cdv(operand, registers)
            else: 
                print(f'Error in instruction = {instruction}')

            i += 2
        
        output = output[:-1]
        if output == partialOutput:
            print(a, partialOutput)
            # This is the sauce - left shift 3 bits to start search range for next output splice
            # I don't have a complete proof for this but I noticed empirically while manually
            # calculating, that the next splice answer was simply the previous splice shifted 3
            # bits plus 0 < extra < 7. There are one or two exceptions, but this shortcuts the
            # runtime like crazy to O(8 x input len) amortized as opposed to O(8^(input len))
            start = a * 8
            break