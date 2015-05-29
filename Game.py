import pygame, sys, random, time
from Ball import Ball
from Player import *
from Bullet import *
from Zombie import *
#from Title import Title
from Score import *
from Background import Background

pygame.init()

clock = pygame.time.Clock()

width = 800
height = 600
size = width, height

screen = pygame.display.set_mode(size)

enemies = pygame.sprite.Group()
playerx = pygame.sprite.Group()
playery = pygame.sprite.Group()
hudItems = pygame.sprite.Group()
backgrounds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Player.containers = (all, playerx)
Player2.containers = (all, playery)
Background.containers = (all, backgrounds)
Zombie.containers = (all, enemies)
Bullet.containers = (all, bullets)
Score.containers = (all, hudItems)

Background()

score = Score([width-300, height-25], "Score: ", 80)

spawnRate = .3 #seconds

player1 = Player((width/2, height/2))

player2 = Player2((width/2, height/2))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1.go("up")
            if event.key == pygame.K_UP:
                player2.go("up")
            if event.key == pygame.K_d:
                player1.go("right")
            if event.key == pygame.K_RIGHT:
                player2.go("right")
            if event.key == pygame.K_s:
                player1.go("down")
            if event.key == pygame.K_DOWN:
                player2.go("down")
            if event.key == pygame.K_a:
                player1.go("left")
            if event.key == pygame.K_LEFT:
                player2.go("left")
            if event.key == pygame.K_SPACE:
                player1.shoot()
            if event.key == pygame.K_RETURN:
                player2.shoot()
            if event.key == pygame.K_1:
                player1.gun = player1.pistol
                player1.shoot("stop")
            if event.key == pygame.K_KP1:
                player2.gun = player2.pistol
                player2.shoot("stop")
            if event.key == pygame.K_2:
                player1.gun = player1.shotGun
                player1.shoot("stop")
            if event.key == pygame.K_KP2:
                player2.gun = player2.shotGun
                player2.shoot("stop")
            if event.key == pygame.K_3:
                player1.gun = player1.uzi
                player1.shoot("stop")
            if event.key == pygame.K_KP3:
                player2.gun = player2.uzi
                player2.shoot("stop")
            if event.key == pygame.K_4:
                player1.gun = player1.joker
                player1.shoot("stop")
            if event.key == pygame.K_KP4:
                player2.gun = player2.joker
                player2.shoot("stop")
            if event.key == pygame.K_5:
                player1.gun = player1.exploder
                player1.shoot("stop")
            if event.key == pygame.K_KP5:
                player2.gun = player2.exploder
                player2.shoot("stop")
            if event.key == pygame.K_6:
                player1.gun = player1.laser
                player1.shoot("stop")
            if event.key == pygame.K_KP6:
                player2.gun = player2.laser
                player2.shoot("stop")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player1.go("stop up")
            if event.key == pygame.K_UP:
                player2.go("stop up")
            if event.key == pygame.K_d:
                player1.go("stop right")
            if event.key == pygame.K_RIGHT:
                player2.go("stop right")
            if event.key == pygame.K_s:
                player1.go("stop down")
            if event.key == pygame.K_DOWN:
                player2.go("stop down")
            if event.key == pygame.K_a:
                player1.go("stop left")
            if event.key == pygame.K_LEFT:
                player2.go("stop left")
            if event.key == pygame.K_SPACE:
                player1.shoot("stop")
            if event.key == pygame.K_RETURN:
                player2.shoot("stop")
            
            
    if len(enemies) < 240:
        if random.randint(0, int(spawnRate*60)) == 0:
            side = random.randint(1,4)
            kind = random.randint(1,123)
            if side == 1: #top
                if kind <30:
                    Zombie([random.randint(0,width),-50])
                elif kind <50:
                    RedZombie([random.randint(0,width),-50])
                elif kind <71:
                    Maoira([random.randint(0,width),-50])
                elif kind <77:
                    Phantom([random.randint(0,width),-50])
                elif kind <86:
                    Druflyll([random.randint(0,width),-50])
                elif kind <101:
                    Chatterbox([random.randint(0,width),-50])
                elif kind <102:
                    Illuminatus([random.randint(0,width),-50])
                elif kind <111:
                    Raksasha([random.randint(0,width),-50])
                elif kind <122:
                    Ghast([random.randint(0,width),-50])
                
                    
            elif side == 2: #right
                if kind <30:
                    Zombie([width+50, random.randint(0,height)])
                elif kind <50:
                    RedZombie([width+50, random.randint(0,height)])
                elif kind <71:
                    Maoira([width+50, random.randint(0,height)])
                elif kind <77:
                    Phantom([width+50, random.randint(0,height)])
                elif kind <86:
                    Druflyll([width+50, random.randint(0,height)])
                elif kind <101:
                    Chatterbox([width+50, random.randint(0,height)])
                elif kind <102:
                    Illuminatus([width+50, random.randint(0,height)])
                elif kind <111:
                    Raksasha([width+50, random.randint(0,height)])
                elif kind <122:
                    Ghast([width+50, random.randint(0,height)])
                
                    
            elif side == 3: #bottom
                if kind <30:
                    Zombie([random.randint(0,width),height+50])
                elif kind <50:
                    RedZombie([random.randint(0,width),height+50])
                elif kind <71:
                    Maoira([random.randint(0,width),height+50])
                elif kind <77:
                    Phantom([random.randint(0,width),height+50])
                elif kind <86:
                    Druflyll([random.randint(0,width),height+50])
                elif kind <101:
                    Chatterbox([random.randint(0,width),height+50])
                elif kind <102:
                    Illuminatus([random.randint(0,width),height+50])
                elif kind <111:
                    Raksasha([random.randint(0,width),height+50])
                elif kind <122:
                    Ghast([random.randint(0,width),height+50])
               
                    
            elif side == 4: #left
                if kind <30:
                    Zombie([-50, random.randint(0,height)])
                if kind <50:
                    RedZombie([-50, random.randint(0,height)])
                elif kind <71:
                    Maoira([-50, random.randint(0,height)])
                elif kind <77:
                    Phantom([-50, random.randint(0,height)])
                elif kind <86:
                    Druflyll([-50, random.randint(0,height)])
                elif kind <101:
                    Chatterbox([-50, random.randint(0,height)])
                elif kind <102:
                    Illuminatus([-50, random.randint(0,height)])
                elif kind <111:
                    Raksasha([-50, random.randint(0,height)])
                elif kind <121:
                    Ghast([-50, random.randint(0,height)])
                elif kind <122:
                    BadJuju([-50, random.randint(0,height)])

    for player1 in playerx.sprites():
        if player1.shooting:
            player1.shoot()
    for player2 in playery.sprites():
        if player2.shooting:
            player2.shoot()
            
    bulletsHitEnemies = pygame.sprite.groupcollide(bullets, enemies, True, True)
    
    for bullet in bulletsHitEnemies:
            for enemy in bulletsHitEnemies[bullet]:
                enemy.collideBullet(bullet)
                score.increaseScore(enemy.value)
        
    
    all.update(width, height, player1.rect.center, player2.rect.center)
        
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)
