import pgzrun

TITLE='Quiz Master'
WIDTH=700
HEIGHT=440

info=[]
totque=0
curque=0
question=''
timer=10

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
    screen.draw.filled_rect(marquee,'white')
    screen.draw.filled_rect(quebox,'red')
    screen.draw.filled_rect(timebox,'blue')
    for opt in opts:
        screen.draw.filled_rect(opt,'magenta')
    screen.draw.filled_rect(skip,'yellow')
    screen.draw.textbox(f'Welcome to the Quiz Master! This is question {curque} of {totque}.',marquee,color='black')
    screen.draw.textbox(question[0].strip(),quebox,color='black')
    screen.draw.textbox(question[1].strip(),opt1,color='black')
    screen.draw.textbox(question[2].strip(),opt2,color='black')
    screen.draw.textbox(question[3].strip(),opt3,color='black')
    screen.draw.textbox(question[4].strip(),opt4,color='black')
    screen.draw.textbox('Skip',skip,color='black')
    screen.draw.textbox(str(timer),timebox,color='black',shadow=(0.5,0.5),scolor='grey')

def readfile():
    global info,totque
    file=open('quiz questions.txt','r')
    info=file.read().split('\n')
    file.close()
    totque=len(info)

def update():
    marquee.x=marquee.x-3
    if marquee.right<=0:
        marquee.left=WIDTH

def readnextque():
    global question,curque
    question=info.pop(0).split('|')
    curque=curque+1

def on_mouse_down(pos):
    if skip.collidepoint(pos):
        readnextque()



readfile()
readnextque()
print(info)

pgzrun.go()

