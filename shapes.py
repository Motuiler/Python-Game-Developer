import pgzrun
import random
WIDTH=500
HEIGHT=500

def draw():
    screen.fill('black')
    size=490
    for i in range(49):
        r=random.randint(0,255)
        g=random.randint(0,255)
        b=random.randint(0,255)
        rectangle=Rect(0,0,size,size)
        rectangle.center=WIDTH/2,HEIGHT/2
        screen.draw.rect(rectangle,(r,g,b))
        size=size-10
pgzrun.go()
