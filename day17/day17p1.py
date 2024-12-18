input = []
inputFile = open('day17.txt', 'r')

# Get registers
registerA = int(inputFile.readline().strip().split('A: ')[1])
registerB = int(inputFile.readline().strip().split('B: ')[1])
registerC = int(inputFile.readline().strip().split('C: ')[1])
# Line break
inputFile.readline()
# Program
input = [int(n) for n in inputFile.readline().strip()[len('Program: '):].split(',')]
inputFile.close()
print(registerA, registerB, registerC)
print(input)

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


def adv(operand, registers):
    a, b, c = registers
    return (a // (2 ** getCombo(operand, registers)), b, c)
    
def bxl(operand, registers):
    a, b, c = registers
    return (a, b ^ operand, c)

def bst(operand, registers):
    a, b, c = registers
    return (a, getCombo(operand, registers) % 8, c)

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
    return str(getCombo(operand, registers) % 8)

def bdv(operand, registers):
    a, b, c = registers
    return (a, a // (2 ** getCombo(operand, registers)), c)

def cdv(operand, registers):
    a, b, c = registers
    return (a, b, a // (2 ** getCombo(operand, registers)))



i = 0
output = ''
registers = (registerA, registerB, registerC)
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

# Trim trailing comma
print(output[:-1])