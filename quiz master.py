import pgzrun

TITLE='Quiz Master'
WIDTH=700
HEIGHT=440

info=[]

marquee=Rect(0,0,WIDTH,50)
quebox=Rect(10,60,500,150)
timebox=Rect(520,60,170,150)
opt1=Rect(10,220,245,100)
opt2=Rect(265,220,245,100)
opt3=Rect(10,330,245,100)
opt4=Rect(265,330,245,100)
opts=[opt1,opt2,opt3,opt4]
skip=Rect(520,220,170,210)

def draw():
    screen.fill('white')
    screen.draw.filled_rect(marquee,'green')
    screen.draw.filled_rect(quebox,'red')
    screen.draw.filled_rect(timebox,'blue')
    for opt in opts:
        screen.draw.filled_rect(opt,'magenta')
    screen.draw.filled_rect(skip,'yellow')

def readfile():
    global info
    file=open('quiz questions.txt','r')
    info=file.read().split('\n')
    file.close()


readfile()
print(info)

pgzrun.go()

