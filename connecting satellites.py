import pgzrun
import random

WIDTH=800
HEIGHT=600
TITLE='Connecting Satellites'

satellites=[]
num=8
for i in range(num):
    sat=Actor('satellite')
    sat.x=random.randint(50,WIDTH-50)
    sat.y=random.randint(90,HEIGHT-50)
    satellites.append(sat)
print(satellites)

def draw():
    screen.blit('stars',(0,0))
    for i in range(0,len(satellites)):
        satellites[i].draw()
        screen.draw.text(str(i),(satellites[i].x-7,satellites[i].y+10),fontsize=30,color='red')
pgzrun.go()