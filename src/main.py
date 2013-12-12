import cog


#Keycodes
class KC:
    W = 119
    A = 97
    S = 115
    D = 100
    UP = 1073741906
    DOWN = 1073741905
    LEFT = 1073741904
    RIGHT = 1073741903
    ENTER = 13
    SPACE = 32


#Game state enum
class GSE:
    TITLE = 0
    LEVEL0 = 1


#Game state
class GS:
    state = GSE.TITLE


def add_fullscreen_sprite(path):
    s_id = cog.sprite_add(path)
    s = cog.sprite_get(s_id)
    s.dim.w = 1.0
    s.dim.h = 1.0
    return s_id


def game_init():
    gs = GS()
    gs.title_id = add_fullscreen_sprite("media/title.png")

    return gs


def title_loop(gs):
    if cog.input_key_pressed():
        kc = cog.input_key_code_pressed()
        #print("KEYCODE {}".format(kc))
        if kc == KC.SPACE:
            cog.sprite_remove(gs.title_id)
            gs.title_id = add_fullscreen_sprite("media/back1.png")
            gs.state = GSE.LEVEL0


def level0_loop(gs):
    pass


def game_mainloop(gs):
    if gs.state == GSE.TITLE:
        title_loop(gs)
    elif gs.state == GSE.LEVEL0:
        level0_loop(gs)


if __name__ == "__main__":
    cog.init()
    gs = game_init()
    while not cog.hasquit():
        #print("game state is : {}".format(gs.state))
        cog.loopstep()
        game_mainloop(gs)
    cog.quit()
