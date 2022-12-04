file = open('input').readlines()
assignment = []
for line in file: assignment.append(line.strip())

total = 0
for i in assignment:
    pair = i.split(",")
    elf1 = pair[0].split("-")
    elf2 = pair[1].split("-")
    min1 = int(elf1[0])
    min2 = int(elf2[0])
    max1 = int(elf1[1])
    max2 = int(elf2[1])
    if max1 >= min2 and max2 >= min1:
        total = total + 1

print(total)