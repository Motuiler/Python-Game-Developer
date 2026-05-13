import pgzrun
import random

WIDTH=500
HEIGHT=500

oceans=[]
y=40

for i in range(5):
    row=[]
    x=40
    for u in range(5):
        ocean=Actor('ocean')
        ocean.x=x
        ocean.y=y
        row.append(ocean)
        x=x+70
    oceans.append(row)
    y=y+70
treasurerow=random.randint(0,4)
treasurecolumn=random.randint(0,4)

def draw():
    for row in oceans:
        for ocean in row:
            ocean.draw()

def on_mouse_down(pos):
    global treasurerow,treasurecolumn
    if mouse.colidepoint(pos):
        treasurerow
        treasurecolumn

pgzrun.go()