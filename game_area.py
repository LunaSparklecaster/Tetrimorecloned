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


# testing the function we just built
game_space = [[0 for a in range(20)] for b in range(20)]

game_space[1][1] = 4

boolean = check_free('square', (0,0), 0, game_space=game_space)

print(boolean) # should be false because one of the squares is a 4!

print(game_space)