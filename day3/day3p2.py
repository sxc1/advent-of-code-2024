# Time: 30:44 min

input = []
inputFile = open('day3.txt', 'r')
for line in inputFile:
    input.append(line.strip())
input = ''.join(input)
inputFile.close()

def startsWith(string, prefix):
    if len(string) >= len(prefix):
        return string[:len(prefix)] == prefix

total = 0
do = True
i = 0

while i < len(input):
    curr = input[i:]
    if startsWith(curr, 'do()'):
        do = True
        i += 4
    elif startsWith(curr, "don't()"):
        do = False
        i += 7
    elif startsWith(curr, "mul("):
        if do:
            firstNum = []
            secondNum = []
            i += 4

            while input[i].isnumeric():
                firstNum.append(input[i])
                i += 1

            if input[i] == ',':
                i += 1
            else:
                continue

            while input[i].isnumeric():
                secondNum.append(input[i])
                i += 1

            if input[i] == ')' and len(firstNum) > 0 and len(secondNum) > 0:
                total += int(''.join(firstNum)) * int(''.join(secondNum))
            else:
                i += 1
        else:
            i += 4
    else:
        i += 1

print(total)