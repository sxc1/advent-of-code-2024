from functools import cache

FILENAME = 'day21.txt'

input = []
inputFile = open(FILENAME, 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

KEYPAD_MAP = {
    '<': (0, 0),
    'v': (1, 0),
    '>': (2, 0),
    '^': (1, 1),
    'A': (2, 1)
}

NUMPAD_MAP = {
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

@cache
def buttons(curr, destination):
    if curr in NUMPAD_MAP and destination in NUMPAD_MAP:
        keymap = NUMPAD_MAP
    else:
        keymap = KEYPAD_MAP

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

@cache
def sequenceLength(code, keypads):
    if keypads < 0:
        return len(code)
    
    length = 0
    for i in range(len(code)):
        length += sequenceLength(buttons(code[i-1], code[i]), keypads - 1)

    return length

def calcComplexity(code, length):
    print('sequence length:', length, 'code:', code)
    print('')
    return length * int(code[:-1])

total = 0
for code in input:
    total += calcComplexity(code, sequenceLength(code, 25))
print('total complexity:', total)
