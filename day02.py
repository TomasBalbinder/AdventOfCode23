
#part one

with open("day02.txt", "r") as day02:
    content = day02.read().strip()
    games = content.split()


games_list = []
nested_list = []
for game in games:
    if game.startswith('Game'):
        if nested_list:
            games_list.append(nested_list)
            nested_list = [game]
    else:
        nested_list.append(game.rstrip(';'))
if nested_list:
    games_list.append(nested_list)


game_counter = 0
result = 0
for individual_game in games_list:

    game_counter = game_counter + 1
    blue_counter = 0
    red_counter = 0
    green_counter = 0

    for j in range(len(individual_game)):
        
        if 'blue' in individual_game[j]:
            number_blue = int(individual_game[j - 1])
            if blue_counter < int(number_blue):
                blue_counter = number_blue

        elif 'red' in individual_game[j]:
            number_red = int(individual_game[j - 1])
            if red_counter < int(number_red):
                red_counter = number_red

        elif 'green' in individual_game[j]:
            number_green = int(individual_game[j - 1])
            if green_counter < int(number_green):
                green_counter = number_green

    if blue_counter < 15 and red_counter < 13 and green_counter < 14:
        result = result + game_counter
           
print(result)













