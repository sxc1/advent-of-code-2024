# Time: 28:06 min

from functools import lru_cache

input = []
inputFile = open('day19.txt', 'r')

inputPatterns = inputFile.readline().strip().split(', ')
inputFile.readline()

for line in inputFile:
    input.append(line.strip())
inputFile.close()

# Convert list to trie
patterns = {}
for pattern in inputPatterns:
    curr = patterns
    for char in pattern:
        curr = curr.setdefault(char, {})
    # Mark end of word
    curr['.'] = '.'

def checkTrie(trie, s):
    curr = trie
    for char in s:
        if char not in curr:
            return False
        curr = curr[char]
    return '.' in curr

# TIL @lru_cache is op af for recursion
@lru_cache(maxsize=10000000)
def checkSubstring(substring):
    global patterns
    if substring == '':
        return True
    
    for i in range(len(substring)):
        if checkTrie(patterns, substring[:i+1]):
            if checkSubstring(substring[i+1:]):
                return True

    return False
    
ct = 0
for design in input:
    if checkSubstring(design):
        ct += 1
print(ct)