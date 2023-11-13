''' Find The Golden Star '''
import random


def print_map(p_map):
    print('\n'.join([''.join(['{:2}'.format(item) for item in row]) for row in p_map]))


map1 = [["◻️", "◻️", "◻️"], ["◻️", "◻️", "◻️"], ["◻️", "◻️", "◻️"]]
print("This is our initial map...")
print_map(map1)
gold_horizontal = random.randint(0, 2)
gold_vertical = random.randint(0, 2)
map1[gold_horizontal][gold_vertical] = "⭐"
gold_position = str(gold_horizontal + 1) + str(gold_vertical + 1)

position = input("what do you think: where is the Golden Star in the map?")
if gold_position == position:
    print("Congratulations You Have Found The Golden Star")
else:
    horizontal = int(position[0])
    vertical = int(position[1])
    map1[horizontal - 1][vertical - 1] = "❌"
    print("Unfortunately you could not find it😶 ")
print(print_map(map1))
