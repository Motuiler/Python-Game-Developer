import pgzrun

WIDTH=1500
HEIGHT=1000
TITLE='Galaga'

ship=Actor('ship')
ship.center=WIDTH/2,HEIGHT-100
bullets=[] 
enemies=[]
score=0
y=40
for i in range(4):
    row=[]
    x=40
    for u in range(5):
        enemy=Actor('enemy')
        enemy.x=x
        enemy.y=y
        row.append(enemy)
        x=x+70
    enemies.append(row)
    y=y+70
print(enemies)


def draw():
    screen.fill('red')
    ship.draw()
    for bullet in bullets:
        bullet.draw()
    for row in enemies:
        for enemy in row:
            enemy.draw()
    screen.draw.text(f"Score:{score}",center=(WIDTH-50,10),fontsize=35,color='white')

def update():
        if keyboard.D and ship.right<WIDTH:
            ship.x=ship.x+10
        elif keyboard.A and ship.left>0:
            ship.x=ship.x-10
        for bullet in bullets:
             bullet.y=bullet.y-5

def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullet.x=ship.x
        bullet.y=ship.top
        bullets.append(bullet)

     
    
pgzrun.go()
