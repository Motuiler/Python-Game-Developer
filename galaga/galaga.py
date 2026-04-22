import pgzrun

WIDTH=1500
HEIGHT=1000
TITLE='Galaga'

ship=Actor('ship')
ship.center=WIDTH/2,HEIGHT-100

def draw():
    screen.fill('red')
    ship.draw()

def update():
    pass
    
pgzrun.go()