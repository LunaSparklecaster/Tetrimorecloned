# what we need to do here is start implementing functions to move blocks around in our space
# we can start with a simple "place block" function


def check_free(type, upper_left_corner, rotation, game_space):
    """
    This function is a helper for our "place block" function
    We use it to check if the area we want to move a block to is free.
    :param type: the type of block (square, l, right-zig, left-zig, straight)
    :param upper_left_corner: a tuple (x,y) of the coordinates of the upper left corner
    :param rotation: the rotation relative to the original state. can use [0, 1, 2, 3] to be [0, 90, 180, 270]
    :param game_space: the array of values that represents the game board
    :return: a boolean value (true/false)
    """
    x = upper_left_corner[0]
    y = upper_left_corner[1]
    if type == 'square':
        if game_space[x][y] == 0 and game_space[x][y+1] == 0 and game_space[x+1][y] == 0 and game_space[x+1][y+1] == 0:
            return True
        else:
            return False


def minimal_check_free(coord_list, game_space):
    is_free = True
    for x, y in coord_list:
        if game_space[x][y] != 0:
            is_free = False
    return is_free


def rotate_offsets(offsets, rotation):
    if rotation == 0:
        pass
    if rotation == 1:
        for i in offsets:
            offsets[i][0], offsets[i][1] = 0 - offsets[i][1], offsets[i][0]
    if rotation == 2:
        for i in offsets:
            offsets[i][0], offsets[i][1] = 0 - offsets[i][0], 0 - offsets[i][1]
    if rotation == 3:
        for i in offsets:
            offsets[i][0], offsets[i][1] = offsets[i][1], 0 - offsets[i][0]
    return offsets


def coords_to_check(type, center_location, rotation):
    coords = []
    if type == 'square':
        offsets = [(0, 0), (0, 1), (1, 0), (1, 1)]
    if type == 'stick':
        offsets = [(-1, 0), (0, 0), (1, 0), (2, 0)]
    if type == 'left_l':
        offsets = []  # todo
    if type == 'right_l':
        offsets = []  # todo
    if type == 'left_zig':
        offsets = []  # todo
    if type == 'right_zig':
        offsets = []  # todo
    if type == 'tee':
        offsets = []  # todo
        

    offsets = rotate_offsets(offsets, rotation)
    for i in offsets:
        coords.append((center_location[0] + offsets[i][0], center_location[1] + offsets[i][1]))
    return coords


# testing the function we just built
game_space = [[0 for a in range(10)] for b in range(22)]
game_space[1][1] = 4

boolean = check_free('square', (0, 0), 0, game_space=game_space)
print(boolean, ': should be false because one of the squares is a 4!')

boolean = check_free('square', (2, 2), 0, game_space=game_space)
print(boolean, ': should be true because all of the squares are 0!')

boolean = check_free('square', (20, 20), 0, game_space=game_space)
# should crash; do you know why? :D

print(game_space)