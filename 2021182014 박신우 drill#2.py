from pico2d import *
import math
open_canvas()



grass= load_image('grass.png')
character = load_image('character.png')

def moveright_1():
    x=0
    while(x<400):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x,90)
         x=x+2
         delay(0.01)
def moveright_2():
    x=400
    while(x<750):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x,90)
         x=x+2
         delay(0.01)
def moveup():
    y=90
    while(y<500):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(750,y)
         y=y+2
         delay(0.01)
def moveleft():
    x=750
    while(x>0):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(x,500)
         x=x-2
         delay(0.01)
def movedown():
    y=500
    while(y>90):
         clear_canvas_now()
         grass.draw_now(400, 30)
         character.draw_now(0,y)
         y=y-2
         delay(0.01)

def makecircle():
    x=400
    y=90
    a=0
    while(a<360):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x+math.sin(a/360*2*math.pi),y+math.sin(a/360*2*math.pi))
        a=a+2
        delay(0.01)

while True:
    moveright_2()
    moveup()
    moveleft()
    movedown()
    moveright_1()
    makecircle()






