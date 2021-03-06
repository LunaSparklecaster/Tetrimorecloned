
####game area vals
g_area_wide = 14
g_area_height = 22
g_area_wallsize = 2

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
    #
    # T shape is shaped like a T with the middle post down, center might be on post in this version or on middle
    # I piece/stick is safe to shift depending on how we handle collisionn
    # O is square, I is stick. played some tetris and remembered the names.
    shape_lookup = {'O_shape': [[0, 0], [0, 1], [1, 0], [1, 1]],
                    'I_shape': [[-1, 0], [0, 0], [1, 0], [2, 0]],
                    'T_shape':[[-1,0],[0,0],[1,0],[0,1]],
                    'S_shape':[[0,0],[1,0],[-1,1],[0,1]],
                    'Z_shape':[[-1,0],[0,0],[0,1],[1,1]],
                    'L_shape':[[0,-1],[0,0],[0,1],[1,1]],
                    'J_shape':[[0,-1],[0,0],[0,1],[1,-1]]}
    offsets = shape_lookup[type]

    offsets = rotate_offsets(offsets, rotation)
    for i in range(len(offsets)):
        coordinate_list.append((center_location[0] + offsets[i][0], center_location[1] + offsets[i][1]))
    return coordinate_list
def wallmaker(game_space):
    #takes in game_space, changes walls to a value so they're not free
    for wallvalone in range(0, g_area_height):
        for wallvaltwo in range(0, g_area_wallsize):
            game_space[wallvalone][wallvaltwo] = 7
        for wallvaltwo in range(g_area_wide - g_area_wallsize, g_area_wide):
            game_space[wallvalone][wallvaltwo] = 7
    return game_space
def wallcheck(center,shape_type, rotation, game_space):
    pass
    #I guess it would take game space, check if shape post-rotation is intersecting wall and push it out
    # check is free several times till it finds position the piece fits in?
    #maybe not needed if a general check free is expanded?
    return #return... coords of where piece should be
# testing the function we just built
# 10 wide 20 high playing field, outer 2 walls on sides are wall checks and top 2 are death zone
# TODO pieces should spawn under dead zone. check top of screen failstate.
# I rebuilt the numbers by flipping which one was which, but I forgot if that broke something
game_space = [[0 for a in range(g_area_wide)] for b in range(g_area_height)]
coords = coords_to_check('O_shape', (4, 12), 2)
free = minimal_check_free(coord_list=coords, game_space=game_space)
#game_space[12][4]=2
## initialize walls
game_space = wallmaker(game_space)

            #hack
    #game_space[pupper][0] = 3
    #game_space[pupper][1] = 3
    #game_space[pupper][12] = 3
    #game_space[pupper][13] = 3
#assert free is True

print(game_space)
# todo: add "walls" by initializing the outer edges of the data structure to non-zero values
# this will let our code check the existing areas w/o modification, and will always prevent going through walls.
#so data set 2 wider for wall checks since the I piece is the only one to occupy 2 spaces away from center.
# todo: kill zone, line clear
# todo: generate an object at random
# todo: user input
# todo: draw to terminal
# todo: tie in graphics library
# todo: refine rotations (get rid of offset bug)
# todo: instant drop

