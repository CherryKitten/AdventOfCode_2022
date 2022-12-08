file = open('input').readlines()
path = []
sizes = {}
filtered = []
total = 0

for line in file:
    line = line.strip()
    if line.startswith('$ cd'):
        if not line[5:] == '..':
            path.append(line[5:])   
            curdir = "/".join(path)
            sizes[curdir] = sizes.get(curdir, 0)
        else:
            del path[-1]
    elif line[0].isdigit():
        curdir = "/".join(path)
        sizes[curdir] = sizes.get(curdir, 0) + int(line.split(" ")[0])
        
                
for k, v in sizes.items():
    for k2, v2 in sizes.items():
        if k != k2 and k2.startswith(k):
            sizes[k] = sizes[k] + v2


for k, v in sizes.items():
    if v <= 100000:
        filtered.append(v)
        
space_available = 70000000 - sizes['/']
space_needed = 30000000 - space_available

current = None

for v in sizes.values():
    if v >= space_needed:
        if current == None:
            current = v
        elif v < current:
            current = v
    

print(current)
