import pgzrun
WIDTH=500
HEIGHT=500

def draw():
    screen.fill('black')
    for i in range(1):
        rectangle=Rect(100,230,55,55)
        screen.draw.rect(rectangle,('magenta'))
        screen.draw.circle((200,257),30,('red'))
        screen.draw.line((300,230),(350,230),('green'))
        screen.draw.line((300,230),(325,250),('green'))
pgzrun.go()
