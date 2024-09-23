from pico2d import *
open_canvas()
pico2d.hide_lattice() ##켄버스 닫는 거
pico2d.show_lattice() ##켄버스 여는 거
image = load_image('character.png')
image.draw_now(400,300)