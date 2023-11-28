
floor = 0

with open("input.txt", "r") as file:
    line = file.readline()
    for c in line:
        if c == "(":
            floor += 1
        elif c == ")":
            floor -= 1

print(floor)