import pgzrun
import random
WIDTH=500
HEIGHT=500

alien=Actor('alien')
alien.x=random.randint(50,WIDTH-50)
alien.y=random.randint(90,HEIGHT-50)
def draw():
    screen.fill('red')
    screen.draw.text('Shoot The Alien',center=(WIDTH/2,20),fontsize=50,color='green')
    alien.draw()

def on_mouse_down(pos):
    print(pos)
    if alien.collidepoint(pos):
        alien.x=random.randint(50,WIDTH-50)
        alien.y=random.randint(90,HEIGHT-50)
pgzrun.go()