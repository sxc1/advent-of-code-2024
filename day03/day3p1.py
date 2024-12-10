# Time: 10:30 min

input = []
inputFile = open('day3.txt', 'r')
for line in inputFile:
    input.append(line.strip())
inputFile.close()

total = 0

for line in input:
    muls = line.split('mul')
    for mul in muls:
        if len(mul) > 0 and mul[0] == '(':
            endIdx = mul.find(')')
            if endIdx != -1:
                nums = mul[1:endIdx].split(',')
                if len(nums) == 2 and nums[0].isnumeric() and nums[1].isnumeric():
                    total += int(nums[0]) * int(nums[1])
print(total)