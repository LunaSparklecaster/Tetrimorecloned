def minimal_check_free(coord_list, game_space):
    is_free = True
    for x, y in coord_list:
        if game_space[x][y] != 0:
            is_free = False
    return is_free


def rotate_offsets(offsets, rotation):
    if rotation == 1:
        for i in range(len(offsets)):
            offsets[i][0], offsets[i][1] = 0 - offsets[i][1], offsets[i][0]
    if rotation == 2:
        for i in range(len(offsets)):
            offsets[i][0], offsets[i][1] = 0 - offsets[i][0], 0 - offsets[i][1]
    if rotation == 3:
        for i in range(len(offsets)):
            offsets[i][0], offsets[i][1] = offsets[i][1], 0 - offsets[i][0]
    return offsets


def coords_to_check(type, center_location, rotation):
    coordinate_list = []
    # todo: dictionary-ify
    shape_lookup = {'square': [[0, 0], [0, 1], [1, 0], [1, 1]],
                    'stick': [[-1, 0], [0, 0], [1, 0], [2, 0]]}
    offsets = shape_lookup[type]

    offsets = rotate_offsets(offsets, rotation)
    for i in range(len(offsets)):
        coordinate_list.append((center_location[0] + offsets[i][0], center_location[1] + offsets[i][1]))
    return coordinate_list


# testing the function we just built
game_space = [[0 for a in range(22)] for b in range(10)]
coords = coords_to_check('square', (4, 12), 2)
free = minimal_check_free(coord_list=coords, game_space=game_space)
assert free is True


# todo: add "walls" by initializing the outer edges of the data structure to non-zero values
# this will let our code check the existing areas w/o modification, and will always prevent going through walls.
# todo: kill zone, line clear
# todo: generate an object at random
# todo: user input
# todo: draw to terminal
# todo: tie in graphics library
# todo: refine rotations (get rid of offset bug)
# todo: instant drop

