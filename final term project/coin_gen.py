import random
import gfw
from pico2d import *
from coin import Coin

GEN_X = [ 50, 150, 250, 350, 450 ]
GEN_Y = [ 50, 150, 250, 350, 450 ]
next_wave = 0
wave_index = 0

def update():
    global next_wave
    next_wave -= gfw.delta_time
    if next_wave < 0:
        generate_wave()

def generate_wave():
    global wave_index, next_wave
    for x in range(5):
        GEN_Y[x] = random.randint(200, get_canvas_height())
        level = coin_level()
        speed = -(100 + 5 * (wave_index))
        e = Coin(GEN_X[x], GEN_Y[x], speed, level)
        gfw.world.add(gfw.layer.coin, e)
    wave_index += 1
    next_wave = random.uniform(5, 6)

LEVEL_ADJUST_PERCENTS = [ 10, 15, 15, 40, 15, 5 ] # -3 ~ 2
def coin_level():
    level = (wave_index - 5) // 10 - 3;
    percent = random.randrange(100)
    pl = level
    pp = percent
    for p in LEVEL_ADJUST_PERCENTS:
        if percent < p: break
        percent -= p
        level += 1
    # print(pl, '->', level, ', ', pp, '->', percent)
    if level < 1: level = 1
    if level > 20: level = 20
    return level

