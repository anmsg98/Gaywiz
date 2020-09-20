from pico2d import*
import helper
def handle_events():
    global running, x, y, dx, dy, tx, ty
    events = get_events()
    for event in events:
          if event.type == SDL_QUIT:
              running = False
          elif event.type == SDL_KEYDOWN:
              if event.key == SDLK_ESCAPE:
                  running = False
          elif event.type == SDL_MOUSEBUTTONDOWN:
              tx, ty = event.x, get_canvas_height() - event.y - 1
              helper.set_target(boy, (tx, ty))
              boy.speed += 2
class Boy:
    def __init__(self):
        self.image = load_image('../res/run_animation.png')
        self.frame = 0
        self.speed = 0
        self.delta = (0, 0)
        self.target = (0, 0)
        self.pos = (x, y)
    def update(self):
        self.frame = (self.frame + 1) % 8
        helper.move_toward_obj(boy)
        if boy.target == None:
            boy.speed = 0
    def draw (self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.pos[0], self.pos[1])
open_canvas()

done = False

grass = load_image('../res/grass.png')
x,y = get_canvas_width() // 2, 85
boy = Boy()
                             
running = True


while(running):
    handle_events()

    boy.update()
    
    clear_canvas()
    grass.draw(400, 30)
    boy.draw()
    update_canvas()
    
    delay(0.05)
    
close_canvas()
