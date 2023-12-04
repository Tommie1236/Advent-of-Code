games_in = []

with open('input.txt', 'r') as file:
    for line in file:
        games_in.append(line.strip())

total = 0

for game in games_in:
    game = game.split(':')
    Id = int(game[0].split(' ')[1])
    bags = game[1].split(';')
    bags = [bags[i].strip().split(', ') for i in range(len(bags))]
    
    cubes = {'red': 0, 'green': 0, 'blue': 0}

    for bag in bags:
        bag_list = [bag[i].strip() for i in range(len(bag))]
        bag_dict = {item.split(' ')[1]: int(item.split(' ')[0]) for item in bag_list}
        for key in ['red', 'green', 'blue']:
            if bag_dict.get(key) == None:
                bag_dict[key] = 0

        cubes['red'] = max(cubes['red'], bag_dict['red'])
        cubes['green'] = max(cubes['green'], bag_dict['green'])
        cubes['blue'] = max(cubes['blue'], bag_dict['blue'])

        if cubes['red'] > 12 or cubes['green'] > 13 or cubes['blue'] > 14:
            total += Id
            break


        

print(total)


