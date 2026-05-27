import pgzrun
import random
import time

WIDTH=510
HEIGHT=510
TITLE='Ocean Map Treasure Hunt'

oceans=[]
attempts=25
message=''
gameover=False
y=10
for i in range(5):
    row=[]
    x=10
    for u in range(5):
        ocean=Actor('ocean')
        ocean.topleft=x,y
        row.append(ocean)
        x=x+100
    oceans.append(row)
    y=y+100
treasurerow=random.randint(0,4)
treasurecolumn=random.randint(0,4)

def draw():
    screen.fill('white')
    if not gameover:
        for row in oceans:
            for ocean in row:
                ocean.draw()
        screen.draw.text(f'Attempts:{attempts}',(15,5),fontsize=30,color='black')
    else:
        screen.draw.text(message,center=(WIDTH/2,HEIGHT/2),fontsize=35,color='black')
    
def on_mouse_down(pos):
    global gameover,attempts,message
    if not gameover:
        for i in range(5):
            for j in range(5):
                if oceans[i][j].collidepoint(pos):
                    attempts=attempts-1
                    if i==treasurerow and j==treasurecolumn:
                        oceans[i][j].image='treasure'
                        time.sleep(8)
                        message='You win!'
                        gameover=True
                    if attempts==0:
                        message='You lost!'
                        gameover=True
                

pgzrun.go()