# Time: ~12 min

inputValues = []
inputNums = []
inputLength = 0
inputFile = open('day7.txt', 'r')
for line in inputFile:
    inputValues.append(int(line.strip().split(':')[0]))
    inputNums.append(line.strip().split(':')[1].strip().split(' '))
    inputLength += 1
inputFile.close()

# operators is string
def generateOperators (operators, i, length):
    if i == length - 1:
        return [operators]

    return generateOperators(operators + '+', i+1, length) + generateOperators(operators + '*', i+1, length) + generateOperators(operators + '|', i+1, length)

def checkValue(value, nums, operator):
    total = int(nums[0])
    for i in range(len(operator)):
        if operator[i] == '+':
            total += int(nums[i+1])
        elif operator[i] == '*':
            total = total * int(nums[i+1])
        else:
            total = int(str(total) + nums[i+1])
    return value == total

total = 0
for i in range(inputLength):
    operators = generateOperators('', 0, len(inputNums[i]))
    for op in operators:
        if checkValue(inputValues[i], inputNums[i], op):
            total += inputValues[i]
            break

print(total)