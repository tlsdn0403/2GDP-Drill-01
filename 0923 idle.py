from pico2d import *
open_canvas()
pico2d.hide_lattice() ##켄버스 닫는 거
pico2d.show_lattice() ##켄버스 여는 거
image = load_image('character.png')
for x in range(0,9):
    for y in range(0,7):
        image.draw_now(x*100,y*100)
