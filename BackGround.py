import pygame, sys, math, time

class Background(pygame.sprite.Sprite):
    def __init__(self, speed = [0,-1]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("RSC/Background/Illuminati.png")
        self.rect = self.image.get_rect()
        self.maxSpeedx = speed[1]
        self.maxSpeedy = speed[0]
        self.speedy = self.maxSpeedy
        self.speedx = self.maxSpeedx
    #telling the background to move
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
    #telling the background to update   
    def update(*args):
        self = args[0]
        self.move()
        print self.rect.x
        if self.rect.x <= -800:
            self.reset()
    #telling the background where it needs to reset    
    def reset(self):
        self.rect.x = 0
