import pgzrun
import random
import time

WIDTH=800
HEIGHT=600
TITLE='Connecting Satellites'

satellites=[]
lines=[]
cursat=0
num=8
for i in range(num):
    sat=Actor('satellite')
    sat.x=random.randint(50,WIDTH-50)
    sat.y=random.randint(90,HEIGHT-50)
    satellites.append(sat)
print(satellites)
starttime=time.time()
timepassed=0

def draw():
    screen.blit('stars',(0,0))
    for i in range(0,len(satellites)):
        satellites[i].draw()
        screen.draw.text(str(i+1),(satellites[i].x-7,satellites[i].y+10),fontsize=30,color='red')
    for line in lines:
        screen.draw.line(line[0],line[1],'white')
    screen.draw.text(f'Timer:{timepassed}',(10,10),fontsize=50,color='white')

def on_mouse_down(pos):
    global cursat,lines
    if cursat<num:
        if satellites[cursat].collidepoint(pos):
            if cursat!=0:
                curpos=satellites[cursat].pos
                prevpos=satellites[cursat-1].pos
                lines.append([curpos,prevpos])
            cursat=cursat+1 
        else:
            lines=[]
            cursat=0       
    print(lines)

def update():
    global timepassed
    if cursat!=num:
        timepassed=round(time.time()-starttime,1)
pgzrun.go()