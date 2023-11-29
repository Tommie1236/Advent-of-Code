from pprint import PrettyPrinter
pp = PrettyPrinter()

total_paper = 0

# store input data into a list
boxes = []
with open('input.txt', 'r') as file:
    for box in file:
        boxes.append([int(s) for s in box.strip('\n').split('x')])


total_ribbon = 0

for box in boxes:    
    l,w,h = box

    smallest = sorted(box)[:2]

    ribbon_box = 2*smallest[0] + 2*smallest[1]

    cfeet = l * w * h
    ribbon_box += cfeet

    total_ribbon += ribbon_box

print(total_ribbon)