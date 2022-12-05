import re

file = open('input').readlines()
stacks = []
stacks_clean = [[],[],[],[],[],[],[],[],[],]
procedure = []
x = 0
result = ""

for line in file:
    if line == '\n':
        x = 1
        continue
    if x == 0:
        stacks.append(line)
    else:
        procedure.append(line.strip())

stacks.reverse()

for i in range(0, len(stacks)):
    if i == 0: continue
    for box in range(0, len(stacks[i]), 4):
        if stacks[i][box:box + 3] == '   ':
            continue
        stacks_clean[int(box / 4)].append(stacks[i][box:box + 3])

for step in procedure:
    values = re.search(r"move (\d+) from (\d+) to (\d+)", step)
    y, a, b = values.groups()
    y, a, b = int(y), int(a), int(b)
    for i in range(y, 0, -1):
        stacks_clean[b - 1].append(stacks_clean[a - 1][len(stacks_clean[a - 1]) - i])
        del stacks_clean[a - 1][len(stacks_clean[a - 1]) - i]


for stack in stacks_clean:
    result += stack[-1][1]

print(result)

