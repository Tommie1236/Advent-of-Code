from pprint import PrettyPrinter
pp = PrettyPrinter()

total_paper = 0

# store input data into a list
boxes = []
with open('input.txt', 'r') as file:
    for box in file:
        boxes.append([int(s) for s in box.strip('\n').split('x')])



for box in boxes:
    l,w,h = box
    paper = (2*l*w) + (2*w*h) + (2*h*l)
    paper += min((l*w), (w*h), (h*l))
    total_paper += paper

print(total_paper)