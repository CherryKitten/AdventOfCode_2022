file = open('input').read()

for i in range(14, len(file)):
    x = [*file[i - 14:i]]
    y = []
    for z in x:
        if z in y: break
        y.append(z)
    if len(y) == 14:
        print(i)
        break
        
