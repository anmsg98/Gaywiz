import gfw
from pico2d import *
from player import Player
from bullet import LaserBullet
from score import Score
from background import HorzScrollBackground
import gobj
import enemy_gen

canvas_width = 1000
canvas_height = 600

def enter():
    gfw.world.init(['bg', 'enemy', 'bullet', 'player', 'ui', 'cg'])
    center = get_canvas_width() // 2, get_canvas_height() // 2
    bg = HorzScrollBackground('bg.png')
    bg.speed = 300
    gfw.world.add(gfw.layer.bg, bg)
    

    global player
    player = Player()
    player.bg = bg
    gfw.world.add(gfw.layer.player, player)

    global score
    score = Score(canvas_width - 20, canvas_height - 50)
    gfw.world.add(gfw.layer.ui, score)

    global font
    font = gfw.font.load(gobj.RES_DIR + '/segoeprb.ttf', 40)

def check_enemy(e):
    if gobj.collides_box(player, e):
        print('Player Collision', e)
        e.remove()
        return

    for b in gfw.gfw.world.objects_at(gfw.layer.bullet):
        if gobj.collides_box(b, e):
            # print('Collision', e, b)
            dead = e.decrease_life(b.power)
            if dead:
                score.score += e.level * 10
                e.remove()
            b.remove()
            return

def update():
    gfw.world.update()
    enemy_gen.update()

    for e in gfw.world.objects_at(gfw.layer.enemy):
        check_enemy(e)

def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()

def handle_event(e):
    global player
    # prev_dx = boy.dx
    if e.type == SDL_QUIT:
        gfw.quit()
    elif e.type == SDL_KEYDOWN:
        if e.key == SDLK_ESCAPE:
            gfw.pop()

    player.handle_event(e)

def exit():
    pass

if __name__ == '__main__':
    gfw.run_main()
