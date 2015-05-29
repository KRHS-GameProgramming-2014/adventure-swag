
import pygame
from Ball import Ball

class Bullet(Ball):
    def __init__(self, pos, bspeed, heading, heading2 = None, life = 500):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.image = pygame.image.load("RSC/Bullet/Illuminati1.png")
            if heading == "up" or heading2 == "up":
                self.speedy = -bspeed
            if heading == "down" or heading2 == "down":
                self.speedy = bspeed
            if heading == "right" or heading2 == "right":
                self.speedx = bspeed
            if heading == "left" or heading2 == "left":
                self.speedx = -bspeed
            self.life = life

    def collideZombie(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
        return []
    
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        Ball.update(self, width, height,)
        if self.life > 0:
            self.life -= 1
        else:
            self.living = False
            
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.living = False
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.living = False

class Exploder(Bullet):
    def __init__(self, pos, bspeed, heading, heading2 = None, life = 40):
        Bullet.__init__(self, pos, bspeed, heading, heading2 = None)
        self.image = pygame.image.load("RSC/Bullet/Fireball.png")
        self.bSpeed = bspeed
        self.life = life
        
    def collideZombie(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
                    return [Exploder(self.rect.center, self.bSpeed, "right", self.life/3),
                            Exploder(self.rect.center, self.bSpeed, "up", self.life/3),
                            Exploder(self.rect.center, self.bSpeed, "left", self.life/3),
                            Exploder(self.rect.center, self.bSpeed, "down", self.life/3)]
        return []

class Laser(Bullet):
    def __init__(self, pos, bspeed, heading, heading2 = None, life = 100):
        Bullet.__init__(self, pos, bspeed, heading, heading2 = None)
        self.image = pygame.image.load("RSC/Bullet/Lasershot.png")
    def collideZombie(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    self.living = False
        return []
        
