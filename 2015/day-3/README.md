# Writeup AoC 2015 Day-3

## Part 1
### The question is:
```
Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

  - > delivers presents to 2 houses: one at the starting location, and one to the east.
  - ^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
  - ^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.
```

This a pretty simple one again. You just need to keep track of the position of santa and the coordinates of all the visited houses.

Lets start again by writing some code that reads the `input.txt` file and puts it in a list called `inst` (instructions).
```py
inst = []

with open('input.txt', 'r') as file:
    line = file.readline()
    for i in line:
        inst.append(i)
```

Then I looped over all the instructions and updated the coordinate of santa accordingly.
```py
for i in inst:
    if i == '^':
        y += 1
    elif i == 'v':
        y -= 1
    elif i == '>':
        x += 1
    elif i == '<':
        x -= 1
```

At last i checked if the current coordinate of santa is already visited, if it already exists in the `visited` list and append it to the list if it doesn't. then just continue to the next instruction.

You should have a list of coordinates of visited houses at the end. To get the answer just get the lenght of the `visited` list and print it `print(len(visited))`.

## Part 2

### Question:
```
The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

  - ^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
  - ^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
  - ^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
```

This looks a lot like the [last](README.md#part-1) challenge. But now we have to keep track what santa is currently moving and the coordinates of both santa's.

I did this by changing the `x, y` coordinates of santa to `xs, ys` for santa and `xr, yr` for robo-santa. And added a variable called `real_santa` that equals `True` for santa and `False` for robo-santa.

Then I again looped over the instructions, moved the correct santa accordingly and checked if the current coordinates are in the `visited` list and otherwise add them.

At the end of the loop I switched santas by doing. 
`real_santa = not real_santa`

And like the end of [part-1](README.md#part-1) print the lenght of the list of visited houses again `print(len(visited))`.