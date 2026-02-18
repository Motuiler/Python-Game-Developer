import pgzrun
WIDTH=500
HEIGHT=500

def draw():
    screen.fill('black')
    rectangle=Rect(100,230,55,55)
    screen.draw.rect(rectangle,('magenta'))
    screen.draw.circle((200,257),30,('red'))
    screen.draw.line((245,285),(300,285),('green'))
    screen.draw.line((245,285),(272.5,230),('green'))  
    screen.draw.line((300,285),(272.5,230),('green'))
    screen.draw.line((325,285),(370,230),('blue'))      
    screen.draw.line((325,230),(370,285),('blue'))         
pgzrun.go()
