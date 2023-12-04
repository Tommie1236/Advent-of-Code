import re

pattern = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
patterndict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
               'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

def find_numbers_in_sting(string):
    out = []
    for number in pattern:
        out += [(m.start(), patterndict[m.group()]) for m in re.finditer(number, string)]
        # coudn't get re.compile to work
    return out




calibrations = []

with open('input.txt', 'r') as file:
    for line in file:
        calibrations.append(line.strip())

total = 0

for cal in calibrations:
    ints = []
    strings = find_numbers_in_sting(cal)
    for i in range(len(cal)):
        try:
            ints.append(int(cal[i]))
            continue
        except:
            pass
        if i in [int(x[0]) for x in strings]:
            ints.append(strings[[x[0] for x in strings].index(i)][1])
    print(ints)


    total += int(str(ints[0]) + str(ints[-1]))


print(total)