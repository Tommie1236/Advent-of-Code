
inst = []

with open('input.txt', 'r') as file:
    line = file.readline()
    for i in line:
        inst.append(i)

xs, ys, xr, yr = 0, 0, 0, 0
visited = []

real_santa = True
for i in inst:
    if real_santa:
        if i == '^':
            ys += 1
        elif i == 'v':
            ys -= 1
        elif i == '>':
            xs += 1
        elif i == '<':
            xs -= 1
        if not ((xs, ys) in visited):
            visited.append((xs, ys))
    else:
        if i == '^':
            yr += 1
        elif i == 'v':
            yr -= 1
        elif i == '>':
            xr += 1
        elif i == '<':
            xr -= 1
        if not ((xr, yr) in visited):
            visited.append((xr, yr))
    real_santa = not real_santa


print(len(visited))
