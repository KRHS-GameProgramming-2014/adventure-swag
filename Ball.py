import pygame, math

class Ball(pygame.sprite.Sprite):
    def __init__(self, image, pos = [-50,100]):
            pygame.sprite.Sprite.__init__(self, self.containers)
            self.image = pygame.image.load(image)
            self.rect = self.image.get_rect()
            self.maxspeed = 5
            self.speed = [self.speedx, self.speedy]
            self.place(pos)
            self.didBounceX = False
            self.didBounceY = False
            self.radius = (int(self.rect.height/2.0 + self.rect.width/2.0)/2) - 1
            self.living = True
        
    def place(self, pos):
        self.rect.center = pos
    
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
            
    def update(*args):
        self = args[0]
        width = args[1]
        height = args[2]
        self.didBounceX = False
        self.didBounceY = False

        self.move()
        self.collideWall(width, height)
        
    def move(self):
        self.rect = self.rect.move(self.speed)
        
    def collideWall(self, width, height):
        if not self.didBounceX:
            #print "trying to hit Wall"
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                #print "hit xWall"
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                self.didBounceY = True
                #print "hit xWall"
        
    def collideBall(self, other):
            if self != other:
                if (self.radius + other.radius) > self.distance(other.rect.center):
                    if not self.didBounceX:
                        self.speedx = -self.speedx
                        self.didBouncex = True
                    if not self.didBounceY:
                        self.speedy = -self.speedy
                        self.didBounceY = True
                        #print "hit Ball"
                            
    def collidePlayer(self, other):
        if self != other:
            if (self.radius + other.radius) > self.distance(other.rect.center):
                            self.living = False
    
    def distance(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt(((x2-x1)**2) + ((y2-y1)**2))





