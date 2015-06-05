import pygame
from Ball import Ball
from Bullet import *
from Gun import Gun

class Player(Ball):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Player/Shadow2.png")]
        self.downImages = [pygame.image.load("RSC/Player/Shadow2.png")]
        self.leftImages = [pygame.image.load("RSC/Player/Shadow2.png")]
        self.rightImages = [pygame.image.load("RSC/Player/Shadow2.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.maxspeed = 5
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.pistol = Gun("pistol")
        self.uzi = Gun("uzi")
        self.shotGun = Gun("shot gun")
        self.joker = Gun("joker")
        self.exploder = Gun("exploder")
        self.laser = Gun("laser")
        self.gun = self.pistol
        self.shooting = False
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 100
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        Ball.update(self, width, height)
        self.move()
        self.animate()
        self.changed = False
        #print self.gun.coolDown
        if self.gun.coolDown > 0:
            if self.gun.coolDown < self.gun.coolDownMax:
                self.gun.coolDown += 1
            else:
                self.gun.coolDown = 0
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = 0
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = 0
                self.didBounceY = True
                #print "hit xWall"
    
    def animate(self):
        if self.waitCount < self.maxWait:
            self.waitCount += 1
        else:
            self.waitCount = 0
            self.changed = True
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        
        if self.changed:    
            if self.facing == "up":
                self.images = self.upImages
            elif self.facing == "down":
                self.images = self.downImages
            elif self.facing == "right":
                self.images = self.rightImages
            elif self.facing == "left":
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def go(self, direction):
        if direction == "up":
            self.facing = "up"
            self.changed = True
            self.speedy = -self.maxspeed
        elif direction == "stop up":
            self.speedy = 0
        elif direction == "down":
            self.facing = "down"
            self.changed = True
            self.speedy = self.maxspeed
        elif direction == "stop down":
            self.speedy = 0
            
        if direction == "right":
            self.facing = "right"
            self.changed = True
            self.speedx = self.maxspeed
        elif direction == "stop right":
            self.speedx = 0
        elif direction == "left":
            self.facing = "left"
            self.changed = True
            self.speedx = -self.maxspeed
        elif direction == "stop left":
            self.speedx = 0
            
    def shoot(self, command = ""):
        if command == "stop":
            self.shooting = False
        if self.gun.coolDown == 0:
            self.gun.coolDown += 1
            if self.gun.kind == "pistol":
                return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing)]
            elif self.gun.kind == "shot gun":
                if self.facing == "up" or self.facing == "down":
                    return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, "right"),
                            Bullet(self.rect.center, self.gun.gunSpeed, self.facing),
                            Bullet(self.rect.center, self.gun.gunSpeed, self.facing, "left")]
                if self.facing == "left" or self.facing == "right":
                    return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing, "up"),
                            Bullet(self.rect.center, self.gun.gunSpeed, self.facing),
                            Bullet(self.rect.center, self.gun.gunSpeed, self.facing, "down")]
            elif self.gun.kind == "uzi":
                self.shooting = True
                return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing)]
            elif self.gun.kind == "joker":
                return [Bullet(self.rect.center, self.gun.gunSpeed, self.facing)]
            elif self.gun.kind == "exploder":
                return [Exploder(self.rect.center, self.gun.gunSpeed, self.facing)]
            elif self.gun.kind == "laser":
                self.shooting = True
                return [Laser(self.rect.center, self.gun.gunSpeed, self.facing)]
        else:
            return []
            
    def collideZombie(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    if self.life > 0:
                        self.life = self.life - 11
                    elif self.life < 0: 
                        self.living = False        

class Player2(Player):
    def __init__(self, pos):
    	Player.__init__(self, pos,)
        self.upImages = [pygame.image.load("RSC/Player/LightShadow2.png")]
        self.downImages = [pygame.image.load("RSC/Player/LightShadow2.png")]
        self.leftImages = [pygame.image.load("RSC/Player/LightShadow2.png")]
        self.rightImages = [pygame.image.load("RSC/Player/LightShadow2.png")]
        