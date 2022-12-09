file = open('input').readlines()
coords = []
tailpositions = [{'x': 0, 'y': 0}]
unique = []
knotcount = 10

for knot in range(0, knotcount):
    coords.append({'x': 0, 'y': 0})

for line in file:
    direction, repeats = line.split()
    for i in range(0, int(repeats)):
        match direction:
            case 'R':
                coords[0]['x'] += 1
            case 'L':
                coords[0]['x'] -= 1
            case 'U':
                coords[0]['y'] += 1
            case 'D':
                coords[0]['y'] -= 1

        for y in range(1, len(coords)):
            xdist = coords[y - 1]['x'] - coords[y]['x']
            ydist = coords[y - 1]['y'] - coords[y]['y']
            if abs(xdist) <= 1 and abs(ydist) <= 1:
                continue

            if abs(xdist) > 1 and abs(ydist) > 1:
                coords[y]['x'] += 1 if xdist > 0 else -1
                coords[y]['y'] += 1 if ydist > 0 else -1

            else:

                if abs(xdist) > 1:
                    coords[y]['x'] += 1 if xdist > 0 else -1
                    if abs(ydist) == 1:
                        coords[y]['y'] += ydist

                if abs(ydist) > 1:
                    coords[y]['y'] += 1 if ydist > 0 else -1
                    if abs(xdist):
                        coords[y]['x'] += xdist

        tailpositions.append({'x': coords[-1]['x'], 'y': coords[-1]['y']})

for pos in tailpositions:
    if pos not in unique:
        unique.append(pos)

print(len(tailpositions))
print(len(unique))
