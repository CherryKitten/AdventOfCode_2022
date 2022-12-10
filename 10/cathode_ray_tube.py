import math


class Crt:
    def __init__(self):
        self.c = 0
        self.x = 1
        self.log = []
        self.screen = [['.' for i in range(40)] for j in range(6)]

    def runcycle(self):
        row = math.floor(self.c / 40)
        col = self.c % 40
        self.c += 1
        self.log.append({'c': self.c, 'x': self.x})
        if col == self.x or col == self.x + 1 or col == self.x - 1:
            self.screen[row][col] = '#'

    def addx(self, arg):
        self.runcycle()
        self.runcycle()
        self.x += arg

    def noop(self):
        self.runcycle()


file = open('input').readlines()
crt = Crt()
total = 0

for line in file:
    line = line.split()
    cmd = line[0]
    if cmd == 'addx':
        arg = int(line[1])
        crt.addx(arg)
    elif cmd == 'noop':
        crt.noop()

for line in crt.screen:
    print(line)
