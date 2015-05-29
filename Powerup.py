import pygame

class Powerup(Ball):
	def __init__(self, pos):
		Powerup.__init__(self, "images/Powerup/powerup1.png", [0,0], pos)
		self.upImages = [pygame.image.load("images/Powerup/powerup2.png"),
						 pygame.image.load("images/Powerup/powerup3.png"),
						 pygame.image.load("images/Powerup/powerup4.png")]                                                                                                            


def main():
	
	return 0

if __name__ == '__main__':
	main()

