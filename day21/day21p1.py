FILENAME = 'day21.txt'

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

def buttons(keymap, curr, destination):
    start = keymap[curr]
    end = keymap[destination]
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    buttons = ''

    # Edge cases - need to avoid keypad gap
    if (curr in {'0', 'A'} and destination in {'1', '4', '7'} or
        destination in {'0', 'A'} and curr in {'1', '4', '7'} or
        curr in {'^', 'A'} and destination in {'<'} or
        destination in {'^', 'A'} and curr in {'<'}
       ):
        if dx > 0:
            buttons = buttons + '>' * dx
        if dy > 0:
            buttons = buttons + '^' * dy
        if dy < 0:
            buttons = buttons + 'v' * (-1 * dy)
        if dx < 0:
            buttons = buttons + '<' * (-1 * dx)
    # Standard priority
    else:
        if dx < 0:
            buttons = buttons + '<' * (-1 * dx)
        if dy > 0:
            buttons = buttons + '^' * dy
        if dy < 0:
            buttons = buttons + 'v' * (-1 * dy)
        if dx > 0:
            buttons = buttons + '>' * dx

    return buttons + 'A'

def control(keymap, inputSeq):
    outputSeq = ''
    for i in range(len(inputSeq)):
        if i == 0:
            outputSeq += buttons(keymap, 'A', inputSeq[i])
        else:
            outputSeq += buttons(keymap, inputSeq[i-1], inputSeq[i])
    print('in:', inputSeq, 'out:', outputSeq)
    return outputSeq


def controlRobot(inputSeq):
    keypadMap = {
        '<': (0, 0),
        'v': (1, 0),
        '>': (2, 0),
        '^': (1, 1),
        'A': (2, 1)
    }

    return control(keypadMap, inputSeq)

def controlNumpad(inputSeq):
    numpadMap = {
        '0': (1, 0),
        'A': (2, 0),
        '1': (0, 1),
        '2': (1, 1),
        '3': (2, 1),
        '4': (0, 2),
        '5': (1, 2),
        '6': (2, 2),
        '7': (0, 3),
        '8': (1, 3),
        '9': (2, 3),
    }

    return control(numpadMap, inputSeq)

def fullSequence(code):
    return controlRobot(controlRobot(controlNumpad(code)))

def calcComplexity(code, buttons):
    print('sequence length:', len(buttons), 'code:', code)
    print('')
    return len(buttons) * int(code[:-1])

total = 0
for code in input:
    total += calcComplexity(code, fullSequence(code))
print('total complexity:', total)
