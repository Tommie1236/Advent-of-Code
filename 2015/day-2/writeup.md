# 2015 Day-2

## Part 1
### The question is:
```
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

    A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
    A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.

All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
```

This is a more difficult problem than the last one. You need to calculate how much paper each package needs and sum that up for your answer.

I started by writing a little piece of code to read the `input.txt` file and create a list of all packages and their sizes.

Once i had that list it was time to do some more math. The formula for the amount of paper needed per package `(2*l*w + 2*w*h + 2*h*l + smallest-square)` is luckely given and I started to implement said formula.  
This translated to python to something like this.
The first part is relatively simple, get the sizes from the list ( `l,w,h = box` ) ans put them trough the formula.
`paper = (2*l*w) + (2*w*h) + (2*h*l)`.

And for the second part, the part where you also need to add the smalles side, i just used the `min()` function build into python.
`paper += min((l*w), (w*h), (h*l))`.

And then at last I added te paper for this box to the total amount of paper.
`total_paper += paper`.

## Part 2

### Question:
```
The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.

The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.

For example:

    A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
    A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.

How many total feet of ribbon should they order?
```

This one is also just some basic math, but this time you aren't given a simple formula. so the first thing is to get a formula from the question.

The elves say that is is the shortest distange around the present. So that gives us that we need to get the 2 shortest sides, multiply them by 2 (becausse it has a front and a back) and add them together.

I did this by sorting the list and getting the 2 first items from that list (`smallest = sorted(box)[:2]`). Then i just multiply both values by 2 and add them together. `ribbon_box = 2*smallest[0] + 2*smallest[1]`

But then we also need to add the amount of ribbon needed for the bow. That is equal to the cubic feet of the present. so we just multiply all the sides with eachother and add that answer to the total ribbon needed. `cfeet = l * w * h
    ribbon_box += cfeet`

And in the end just add the amount of ribbon needed for this box to the total `total_ribbon += ribbon_box` and print the total amount needed.