import pygame,math,random
from Ball import Ball


class Zombie(Ball):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/BlueZombieu.png"), pygame.image.load("RSC/Zombie/BlueZombieu1.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/BlueZombied.png"), pygame.image.load("RSC/Zombie/BlueZombied1.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/BlueZombiel.png"), pygame.image.load("RSC/Zombie/BlueZombiel.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/BlueZombier.png"), pygame.image.load("RSC/Zombie/BlueZombier.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.maxSpeed = random.randint(1,3)
        self.speedx = 0
        self.speedy = 0
        self.kind = "zombie"
        self.value = 100
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height,)
        self.move()
        self.animate()
        self.changed = False
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False

class RedZombie(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/RedZombieu.png"), pygame.image.load("RSC/Zombie/RedZombieu1.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/RedZombied.png"), pygame.image.load("RSC/Zombie/RedZombied1.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/RedZombier.png"), pygame.image.load("RSC/Zombie/RedZombier.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/RedZombiel.png"), pygame.image.load("RSC/Zombie/RedZombiel.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.maxSpeed = random.randint(1,3)
        self.kind = "zombie"
        self.value = 500
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False

class  Maoira(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Maoira3.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Maoira3.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Maoira3.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Maoira3.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 5
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.kind = "maoira"
        self.value = 1000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False

class Phantom(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/GlitchPhantom.png"), pygame.image.load("RSC/Zombie/GlitchPhantom2.png"), pygame.image.load("RSC/Zombie/GlitchPhantom3.png"), pygame.image.load("RSC/Zombie/GlitchPhantom4.png"),pygame.image.load("RSC/Zombie/GlitchPhantom5.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/GlitchPhantom.png"), pygame.image.load("RSC/Zombie/GlitchPhantom2.png"), pygame.image.load("RSC/Zombie/GlitchPhantom3.png"), pygame.image.load("RSC/Zombie/GlitchPhantom4.png"),pygame.image.load("RSC/Zombie/GlitchPhantom5.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/GlitchPhantom.png"), pygame.image.load("RSC/Zombie/GlitchPhantom2.png"), pygame.image.load("RSC/Zombie/GlitchPhantom3.png"), pygame.image.load("RSC/Zombie/GlitchPhantom4.png"),pygame.image.load("RSC/Zombie/GlitchPhantom5.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/GlitchPhantom.png"), pygame.image.load("RSC/Zombie/GlitchPhantom2.png"), pygame.image.load("RSC/Zombie/GlitchPhantom3.png"), pygame.image.load("RSC/Zombie/GlitchPhantom4.png"),pygame.image.load("RSC/Zombie/GlitchPhantom5.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 25
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.kind = "phantom"
        self.value = 2000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
    
class Druflyll(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Druflyll.png"),pygame.image.load("RSC/Zombie/Druflyll2.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll10.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll2.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Druflyll.png"),pygame.image.load("RSC/Zombie/Druflyll2.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll10.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll2.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Druflyll.png"),pygame.image.load("RSC/Zombie/Druflyll2.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll10.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll2.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Druflyll.png"),pygame.image.load("RSC/Zombie/Druflyll2.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll10.png"),pygame.image.load("RSC/Zombie/Druflyll9.png"),pygame.image.load("RSC/Zombie/Druflyll8.png"),pygame.image.load("RSC/Zombie/Druflyll7.png"),pygame.image.load("RSC/Zombie/Druflyll6.png"),pygame.image.load("RSC/Zombie/Druflyll5.png"),pygame.image.load("RSC/Zombie/Druflyll4.png"),pygame.image.load("RSC/Zombie/Druflyll3.png"),pygame.image.load("RSC/Zombie/Druflyll2.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 2.0
        self.kind = "druflyll"
        self.value = 3500
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False
        
class Chatterbox(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Chatterbox.png"), pygame.image.load("RSC/Zombie/DarkChatterbox.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Chatterbox.png"), pygame.image.load("RSC/Zombie/DarkChatterbox.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Chatterbox.png"), pygame.image.load("RSC/Zombie/DarkChatterbox.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Chatterbox.png"), pygame.image.load("RSC/Zombie/DarkChatterbox.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 1.0
        self.kind = "chatterbox"
        self.value = 3000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False      

class Illuminatus(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Illuminatus.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Illuminatus.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Illuminatus.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Illuminatus.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 1
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 20.0
        self.kind = "illuminatus"
        self.value = 50000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False                

class Raksasha(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Raksasha.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Raksasha.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Raksasha.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Raksasha.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 3
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 4.0
        self.kind = "raksasha"
        self.value = 10000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False 

class Ghast(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Ghast.png"), pygame.image.load("RSC/Zombie/Ghast1.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast5.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast1.png"),pygame.image.load("RSC/Zombie/Ghast1.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Ghast.png"), pygame.image.load("RSC/Zombie/Ghast1.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast5.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast1.png"),pygame.image.load("RSC/Zombie/Ghast1.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Ghast.png"), pygame.image.load("RSC/Zombie/Ghast1.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast5.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast1.png"),pygame.image.load("RSC/Zombie/Ghast1.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Ghast.png"), pygame.image.load("RSC/Zombie/Ghast1.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast5.png"), pygame.image.load("RSC/Zombie/Ghast4.png"), pygame.image.load("RSC/Zombie/Ghast3.png"), pygame.image.load("RSC/Zombie/Ghast2.png"), pygame.image.load("RSC/Zombie/Ghast1.png"),pygame.image.load("RSC/Zombie/Ghast1.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 3
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 4.0
        self.kind = "ghast"
        self.value = 10000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False     
    
class BadJuju(Zombie):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.upImages = [pygame.image.load("RSC/Zombie/Badjuju.png")]
        self.downImages = [pygame.image.load("RSC/Zombie/Badjuju.png")]
        self.leftImages = [pygame.image.load("RSC/Zombie/Badjuju.png")]
        self.rightImages = [pygame.image.load("RSC/Zombie/Badjuju.png")]
        self.facing = "up"
        self.changed = False
        self.images = self.upImages
        self.frame = 0
        self.maxFrame = len(self.images) - 1
        self.maxSpeed = 10
        self.waitCount = 0
        self.maxWait = 60*.25
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
        self.life = 10.0
        self.kind = "badjuju"
        self.value = 1000000
        
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        playerPos = args[3]
        self.facePlayer(playerPos)
        Ball.update(self, width, height)
        self.animate()
        self.changed = False
    
    def facePlayer(self, pt):
        xdiff = pt[0] - self.rect.center[0]
        ydiff = pt[1] - self.rect.center[1]
        
        if xdiff > 0: #go right
            self.speedx = self.maxSpeed
        elif xdiff < 0: #go left
            self.speedx = -self.maxSpeed
        else:
            self.speedx = 0
            
        if ydiff > 0: #go down
            self.speedy = self.maxSpeed
        elif ydiff < 0: #go up
            self.speedy = -self.maxSpeed
        else:
            self.speedy = 0
                
        
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
            if self.speedy == -self.maxSpeed:
                self.facing == "up"
                self.images = self.upImages
            elif self.speedy == self.maxSpeed:
                self.facing == "down"
                self.images = self.downImages
            elif self.speedx == self.maxSpeed:
                self.facing == "right"
                self.images = self.rightImages
            elif self.speedx == -self.maxSpeed:
                self.facing == "left"
                self.images = self.leftImages
            
            self.image = self.images[self.frame]
    
    def collideBullet(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
                if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                    if (self.radius + other.radius) > self.distance(other.rect.center):
                        if self.life > 0.0:
                            self.life = self.life - 1.1
                        elif  self.life < 0:
                            self.living = False     

#class Skeleton (Zombie):
    #def __init__(self, pos):
        #pygame.sprite.Sprite.__init__(self, self.containers)
        #self.upImages = [pygame.image.load("RSC/Zombie/zombieu1.png")]
        #self.downImages = [pygame.image.load("RSC/Zombie/zombied1.png")]
        #self.leftImages = [pygame.image.load("RSC/Zombie/zombiel1.png")]
        #self.rightImages = [pygame.image.load("RSC/Zombie/zombier1.png")]
