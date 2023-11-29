
inst = []

with open('input.txt', 'r') as file:
    line = file.readline()
    for c in line:
        inst.append(c)

x, y = 0, 0
visited = []


for i in inst:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1

    if not ((x, y) in visited):
        visited.append((x, y))

print(len(visited))
