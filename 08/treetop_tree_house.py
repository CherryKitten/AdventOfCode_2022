file = open('input').readlines()
grid = []
scores = []


def get_distance(h, trees):
    score = 0
    for x in trees:
        score = score + 1
        if x >= h:
            return score
    return score


for i in range(0, len(file)):
    line = file[i].strip()
    grid.append([x for x in [*line]])

for i in range(1, len(grid) - 1):
    for y in range(1, len(grid[i]) - 1):
        h = int(grid[i][y])
        left = [int(grid[i][x]) for x in range(0, y)]
        right = [int(grid[i][x]) for x in range(y + 1, len(grid[i]))]
        up = [int(x[y]) for x in grid[:i]]
        down = [int(x[y]) for x in grid[i + 1:]]
        scores.append(get_distance(h, reversed(left)) * get_distance(h, right) *
                      get_distance(h, reversed(up)) * get_distance(h, down))
print(max(scores))
