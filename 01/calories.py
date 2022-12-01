input = open('input').read()
input = input.split('\n\n')
list = []
totals = []
how_many = 3
top_x_total = 0

for elf in input:
    list.append(elf.split('\n'))

for elf in range(0, len(list)):
    totals.append(0)
    for entry in list[elf]:
        if entry.isnumeric():
            totals[elf] = totals[elf] + int(entry)

totals.sort(reverse=True)

for i in range(0, how_many):
    top_x_total = top_x_total + totals[i]

print(top_x_total)