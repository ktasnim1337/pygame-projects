#J.K.Game Company
#Cart Rider
#car,road...
#We want other objects to come towards the car and the player has to dodge it.
#Problems and Chalenges:background stopped moving 
from gamelib import *

game = Game(800, 600,"Game")



bk = Animation("gameimages\\roadsprite.png",100,game,8000/10,8000/10,1)
game.setBackground(bk)
car = Image("images\\car.png",game)
car.resizeBy(5)
car.moveTo(300,700)

car.setSpeed(1,180)
game.drawBackground()
car.draw()
game.drawText("Cart Rider",game.width/4 ,game.height/4,Font(green,90,yellow))
game.drawText("Press [SPACE] to Start",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update(1)
game.wait(K_SPACE)

heart = Image("gameimages\\heart.png",game)
heart =[]
for times in range(3):
    heart.append(Image("gameimages\\heart.png",game))
for h in heart:
    h.resizeBy(-80)
    h.setSpeed(5,180)
    h.moveTo(randint(30,600),randint(-75,-50))
banana = Image("gameimages\\banana.png",game)
banana =[]
zoom = Sound("car.wav",1)
splat = Sound("banana.wav",2)
for times in range(10):
    banana.append(Image("gameimages\\banana.png",game))
for b in banana:
    b.resizeBy(-70)
    b.setSpeed(1,180)
    b.moveTo(randint(10,750),randint(-800,-50))

    
while not game.over:
    game.processInput()
    game.drawBackground()
    game.displayScore()
     
    for b in banana:
        b.move()
    for h in heart:
        h.move()
        
    car.move()
    if keys.Pressed[K_UP]:
        zoom.play()
        car.y-=8
        car.resizeBy(-1)
    if keys.Pressed[K_DOWN]:
        zoom.play()
        car.y+=3
        car.resizeBy(1)

    if keys.Pressed[K_LEFT]:
        zoom.play()
        car.x-=3
        

    if keys.Pressed[K_RIGHT]:
        zoom.play()
        car.x+=3
        
    for b in banana:
        b.move()
        b.y+=2
        b.resizeBy(-1)
        if b.isOffScreen("bottom"):
            b.moveTo(randint(10,750),randint(-800,-50))
            b.resizeTo(863,558)
            b.move()
            b.y+=2

        if car.collidedWith(b,"rectangle"):
            splat.play()
            b.visible = False
            b.moveTo(randint(10,750),randint(-800,-50))
            b.resizeTo(863,558)
            b.visible = True
        
    for h in heart:
        h.move()
        h.y+=3
        h.resizeBy(-3)
        if h.isOffScreen("bottom"):
            h.moveTo(randint(10,750),randint(-800,-50))
            h.resizeTo(863,558)
            h.move()
            h.y+=2

        if car.collidedWith(h,"squuare"):
            h.moveTo(randint(10,750),randint(-800,-50))
            h.resizeTo(863,558)
            
        if car.collidedWith(h):
            game.score+=5

        if car.collidedWith(b):
            car.damage+=10
            count+=1

    if car.health <= 100:
        game.over = True


            
    if car.width<=10 and car.height<=10:

        car.resizeTo(800,600)
        car.moveTo(300,700)

    if car.collidedWith(b):
        game.health-=2
    
    game.drawText("Car Health: " + str(car.health),100,5)
  
                
        

    

    game.update(60)
game.drawText("Game Over",game.width/4,game.height/3,Font(green,90,yellow))
game.drawText("Press [ESC] to Exit",game.width/2 + 80,game.height - 50,Font(yellow,40,green))
game.update()
game.wait(K_ESCAPE)
game.quit()

