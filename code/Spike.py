import pygame
class Spike(pygame.sprite.Sprite):
	spd_x = 0
	spd_y = 0
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('images/tiles/spike_col.png').convert_alpha()
		self.rect = self.image.get_rect()	
		
		self.image = pygame.image.load('images/tiles/spike.png').convert_alpha()		
		self.rect.y = y + 1
		self.rect.x = x + 1
