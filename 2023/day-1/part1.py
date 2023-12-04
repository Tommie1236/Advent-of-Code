
calibrations = []

with open('input.txt', 'r') as file:
    for line in file:
        calibrations.append(line.strip())

total = 0

for cal in calibrations:
    ints = []
    for i in range(len(cal)):
        try:
            ints.append(int(cal[i]))
        except:
            continue
    print(ints)
    total += int(str(ints[0]) + str(ints[-1]))

print(total)