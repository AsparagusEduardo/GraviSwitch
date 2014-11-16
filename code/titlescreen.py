import pygame
from constants import SCREEN
def TitleScreen():
	title = pygame.image.load('images/titlescreen.png').convert()
	clock = pygame.time.Clock()
	over = False
	while not over:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					pygame.quit()
				elif event.key == pygame.K_RETURN:
					return
				
		SCREEN.blit(title, (0,0))
		pygame.display.flip()
		clock.tick(10)