
floor = 0
i = 0

with open("input.txt", "r") as file:
    line = file.readline()
    for c in line:

        if floor < 0:
            break

        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

        i += 1

print(i)