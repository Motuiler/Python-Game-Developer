import pgzrun

WIDTH=1500
HEIGHT=1000
TITLE='Galaga'

ship=Actor('ship')
ship.center=WIDTH/2,HEIGHT-100
bullets=[] 
enemies=[]
score=0
direction=1
gameover=False
gameovermessage=''
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
    if gameover==False:
        ship.draw()
        for bullet in bullets:
            bullet.draw()
        for row in enemies:
            for enemy in row:
                enemy.draw()
        screen.draw.text(f"Score:{score}",center=(WIDTH-50,10),fontsize=35,color='white')
    else:
        screen.draw.text(gameovermessage,center=(WIDTH/2,HEIGHT/2),fontsize=50,color='white')
        screen.draw.text(f"Your final score is:{score}",center=(WIDTH/2,HEIGHT/2+30),fontsize=35,color='white')

def update():
    global direction,score,gameover,gameovermessage
    movedown=False
    if keyboard.D and ship.right<WIDTH:
        ship.x=ship.x+10
    elif keyboard.A and ship.left>0:
        ship.x=ship.x-10
    for bullet in bullets:
        bullet.y=bullet.y-10
        
    if any(enemies):
        if enemies[0][-1].x>=WIDTH or enemies[0][0].x<=0:
            direction=direction*-1
            movedown=True
    else:
        gameover=True
        gameovermessage='Well Played!'
    

    for row in enemies:
        for enemy in row:
            enemy.x=enemy.x+10*direction
            if movedown:
                enemy.y=enemy.y+40
    
    for i in range(len(enemies)):
        for enemy in enemies[i]:
            for bullet in bullets:
                if enemy.colliderect(bullet):
                    bullets.remove(bullet)
                    enemies[i].remove(enemy)
                    score=score+1
    


def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor('bullet')
        bullet.x=ship.x
        bullet.y=ship.top
        bullets.append(bullet)

     
    
pgzrun.go()