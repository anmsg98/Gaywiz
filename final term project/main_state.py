import gfw
from pico2d import *
from player import Player
from score import Score
from background import HorzScrollBackground
import gobj
import coin_gen
STATE_IN_GAME, STATE_GAME_OVER = range(2)
canvas_width = 800
canvas_height = 600
coin_count = 0
def enter():
    gfw.world.init(['bg', 'coin', 'bullet', 'player', 'ui'])
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

    global state
    state = STATE_IN_GAME

    global game_over_image
    game_over_image = gfw.image.load('res/game_over.png')

def check_coin(e):
    if gobj.collides_box(player, e):
        print('Player Collision', e)
        score.score += e.level * 10
        coin_gen.coin_count += 1
        e.remove()
        return

def update():
    if state != STATE_IN_GAME:
        return
    gfw.world.update()
    coin_gen.update()
    if coin_gen.life_count <= 0:
        end_game()
    for e in gfw.world.objects_at(gfw.layer.coin):
        check_coin(e)
def end_game():
    global state
    print('Dead')
    state = STATE_GAME_OVER
    draw()
    # music_bg.stop()
def draw():
    gfw.world.draw()
    # gobj.draw_collision_box()
    if state == STATE_IN_GAME:
        font.draw(20, canvas_height - 35, 'Wave: %d' % coin_gen.wave_index)
        font.draw(20, canvas_height - 80, 'coin : %d' % coin_gen.coin_count)
        font.draw(20, canvas_height - 125, 'life : %d' % coin_gen.life_count)
    if state == STATE_GAME_OVER:
        center = get_canvas_width() // 2, get_canvas_height() * 2 // 3 + 30
        game_over_image.draw(*center)
        font.draw(300, get_canvas_height() * 2 // 3 - 150, 'Score : %d' % score.score)

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
