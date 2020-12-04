import random
from pico2d import *
import gfw
from gobj import *

class Player:
    RUNNING, FALLING, JUMPING, DOUBLE_JUMP = range(4)
    KEY_MAP = {
        (SDL_KEYDOWN, SDLK_SPACE): 1,
        (SDL_KEYUP, SDLK_SPACE): -1,
    }
    KEYDOWN_SPACE = (SDL_KEYDOWN, SDLK_SPACE)
    LASER_INTERVAL = 0.15
    SPARK_INTERVAL = 0.03
    IMAGE_RUN = [
        (54, 7, 86, 93),
        (158, 7, 86, 93),
        (263, 7, 82, 93),
        (363, 7, 88, 93),
        (467, 7, 87, 93),
        (571, 7, 86, 93),
    ]
    IMAGE_JUMP = [
        (52, 0, 55, 160),
        (121, 0, 76, 160),
        (221, 0, 75, 160),
        (324, 0, 76, 160),
        (416, 0, 56, 160),
        (498, 0, 83, 160),
        (595, 0, 72, 160),
        (675, 0, 86, 160),
        (746, 0, 84, 160),
    ]
    MAX_ROLL = 0.4
    SPARK_OFFSET = 28
    GRAVITY = 1.5
    JUMP = 18

    def magnify(self):
        self.mag_speed = 1.0
    def reduce(self):
        self.mag_speed = -1.0
    def __init__(self):
        # self.pos = get_canvas_width() // 2, get_canvas_height() // 2
        self.x, self.y = 100, 150
        self.dx, self.dy = 0, 0
        self.mag = 1
        self.mag_speed = 0
        self.delta = 0, 0
        self.time = 0
        self.state = Player.RUNNING
        self.speed = 320
        self.coincount = 0
        self.image = gfw.image.load(RES_DIR + '/runner_run.png')
        self.src_rect = Player.IMAGE_RUN[0]
        self.roll = 0
        self.count = 0

    def draw(self):
        self.image.clip_draw(*self.src_rect, self.x,self.y)
    def jump(self):
        if self.state in [Player.FALLING, Player.DOUBLE_JUMP]:
            return
        if self.state == Player.RUNNING:
            self.state = Player.JUMPING
        elif self.state == Player.JUMPING:
            self.state = Player.DOUBLE_JUMP
        self.jump_speed = Player.JUMP

    def update(self):
        self.update_roll()
        if self.state == Player.JUMPING:
            self.y += self.jump_speed
            self.jump_speed -= Player.GRAVITY
            if self.y < 150:
                self.y = 150
                self.state = Player.RUNNING
        elif self.state == Player.RUNNING:
            self.image = gfw.image.load(RES_DIR + '/runner_run.png')
        elif self.state == Player.DOUBLE_JUMP:
            self.image = gfw.image.load(RES_DIR + '/runner_jump.png')
            self.y += self.jump_speed
            self.jump_speed -= Player.GRAVITY/1.4
            if self.y < 150:
                self.y = 150
                self.roll = 3;
                self.state = Player.RUNNING

    def update_roll(self):
        self.count = (self.count+1)%5
        if self.state in [Player.RUNNING, Player.JUMP]:
            self.src_rect = Player.IMAGE_RUN[self.roll]
            if self.count == 0:
                self.roll = (self.roll+1) % 6
        elif self.state == Player.DOUBLE_JUMP:
            self.src_rect = Player.IMAGE_JUMP[self.roll]
            if self.count == 0:
                self.roll = (self.roll + 1) % 9

    def handle_event(self, e):
        if e.type == SDL_KEYDOWN:
            if e.key == SDLK_SPACE or e.key == SDLK_UP:
                self.count = self.roll = 0
                self.jump()

    def get_bb(self):
        hw = self.src_rect[2] / 2
        hh = self.src_rect[3] / 2
        return self.x - hw, self.y - hh, self.x + hw, self.y + hh

if __name__ == "__main__":
    for (l,t,r,b) in Player.IMAGE_RUN:
        l *= 2
        t *= 2
        r *= 2
        b *= 2
        l -= 1
        r += 2
        print('(%3d, %d, %d, %d),' % (l,t,r,b))
