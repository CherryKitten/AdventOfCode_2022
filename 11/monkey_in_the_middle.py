import re

import math


class Monkey:
    def __init__(self, monkeystr):
        self.id = re.search('Monkey (\\d):', monkeystr)[1]
        self.items = re.search('Starting items: (.*)\\n', monkeystr)[1].split(",")
        for y in range(0, len(self.items)):
            self.items[y] = int(self.items[y].strip())
        op = re.search('Operation: new = old ([*+]) (\\d+|old)', monkeystr)
        self.operation = [op[1], op[2]]
        self.test = int(re.search('divisible by (\\d+)', monkeystr)[1])
        self.iftrue = int(re.search('If true: throw to monkey (\\d)', monkeystr)[1])
        self.iffalse = int(re.search('If false: throw to monkey (\\d)', monkeystr)[1])
        self.inspects = 0

    def turn(self):
        for y in range(0, len(self.items)):
            self.inspect()

    def inspect(self):
        # print(' ' * 4 + 'Monkey inspects an item with a worry level of ' + str(self.items[0]) + '.')
        self.inspects += 1
        self.runop()
        self.items[0] = math.floor(self.items[0] % supermodulo)
        print(' ' * 8 + 'Monkey gets bored with item. Worry level is managed to ' + str(self.items[0]) + '.')
        self.throw()

    def runop(self):
        operator = self.operation[0]
        if self.operation[1] == 'old':
            x = self.items[0]
        else:
            x = int(self.operation[1])
        if operator == '*':
            self.items[0] = self.items[0] * x
            # print(' ' * 8 + 'Worry level is multiplied by ' + str(x) + ' to ' + str(self.items[0]) + '.')
        else:
            self.items[0] = self.items[0] + x
            # print(' ' * 8 + 'Worry level increases by ' + str(x) + ' to ' + str(self.items[0]) + '.')

    def throw(self):
        if self.items[0] % self.test == 0:
            monkeys[self.iftrue].receive(self.items[0])
            # print(' ' * 8 + 'Current worry level is divisible by ' + str(self.test) + '.')
            # print(' ' * 8 + 'Item with worry level ' + str(self.items[0]) + ' is thrown to monkey ' + str(
            #    self.iftrue) + '.')
        else:
            monkeys[self.iffalse].receive(self.items[0])
            # print(' ' * 8 + 'Current worry level is not divisible by ' + str(self.test) + '.')
            # print(' ' * 8 + 'Item with worry level ' + str(self.items[0]) + ' is thrown to monkey ' + str(
            #    self.iffalse) + '.')
        del self.items[0]

    def receive(self, item):
        self.items.append(item)


file = open('input').read()
monkeys = {}
monkeystrings = file.split('\n\n')
supermodulo = 1
for i in range(0, len(monkeystrings)):
    monkeys[i] = Monkey(monkeystrings[i])
    supermodulo = supermodulo * monkeys[i].test

for i in range(0, 10000):
    for monkeyid, monkey in monkeys.items():
        print('Monkey ' + str(monkeyid) + ':')
        monkey.turn()

    print('After round ' + str(i) + ', the monkeys are holding items with these worry levels:')

    # for id, monkey in monkeys.items():
    # print('Monkey ' + str(id) + ':', monkey.items)

inspects = []

for monkeyid, monkey in monkeys.items():
    print('Monkey ' + str(monkeyid) + ' inspected items ' + str(monkey.inspects) + ' times.')
    inspects.append(monkey.inspects)

inspects.sort(reverse=True)
print(inspects[0] * inspects[1])
