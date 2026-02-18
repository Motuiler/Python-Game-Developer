import pgzrun
import random
WIDTH=500
HEIGHT=500

bee=Actor('bee')
flower=Actor('flower')
flower.x=random.randint(50,WIDTH-50)
flower.y=random.randint(90,HEIGHT-50)

def draw():
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()

# def on_key_down(key):
#     if key==keys.D
#     bee.x=bee.x+10
#This Function only works when the key is pressed one time not when you hold it

def update():
    if keyboard.D:
        bee.x=bee.x+10
pgzrun.go()
