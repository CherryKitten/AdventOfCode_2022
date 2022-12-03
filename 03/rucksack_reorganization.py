input = open('input').readlines()
list = []
for line in input: list.append(line.strip())

def check_priority(x):
    if x.islower():
        v = ord(x) - 96
    else:
        v = ord(x) - 38
    return v

def split_compartments(rucksack):
    m = int(len(rucksack) / 2 )
    a = rucksack[0:m]
    b = rucksack[m:]
    return a, b

def split_groups(list):
    split_list = []
    group = 0
    elf = 1
    for i in list:
        if elf > 3:
            elf = 1
            group = group + 1
        if elf == 1:
            split_list.append([])
        split_list[group].append(i)
        elf = elf + 1
    return split_list



def puzzle1(list):
    total = 0
    for i in list:
        a, b = split_compartments(i)
        for x in a:
            if x in b:
                total = total + check_priority(x)
                break
    return(total)

def puzzle2(list):
    list = split_groups(list)
    total = 0
    for i in list:
        for x in i[0]:
            if x in i[1] and x in i[2]:
                total = total + check_priority(x)
                break
    return total

if __name__ == '__main__':
    print(puzzle1(list))
    print(puzzle2(list))
