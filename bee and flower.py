import pgzrun
import random
WIDTH=500
HEIGHT=500

bee=Actor('bee')
flower=Actor('flower')
flower.x=random.randint(50,WIDTH-50)
flower.y=random.randint(90,HEIGHT-50)
gameover=False
score=0

def draw():
    if not gameover:
        screen.blit('background',(0,0))
        bee.draw()
        flower.draw()
        screen.draw.text(f"Score:{score}",center=(WIDTH/10,20),fontsize=35,color='red')
    else:
        screen.blit('game over',(0,0))
        screen.draw.text(f"Your final score is {score}",center=(WIDTH/2,20),fontsize=35,color='red')

def timeup():
    global gameover
    gameover=True

# def on_key_down(key):
#     if key==keys.D
#     bee.x=bee.x+10
#This Function only works when the key is pressed one time not when you hold it

def update():
    global score
    if keyboard.D and bee.right<WIDTH:
        bee.x=bee.x+10
    elif keyboard.A and bee.left>0:
        bee.x=bee.x-10
    if keyboard.W and bee.top>0:
        bee.y=bee.y-10
    elif keyboard.S and bee.bottom<HEIGHT:
        bee.y=bee.y+10
    if bee.colliderect(flower):
        score=score+1
        flower.x=random.randint(50,WIDTH-50)
        flower.y=random.randint(90,HEIGHT-50)
clock.schedule(timeup,10)
pgzrun.go()
