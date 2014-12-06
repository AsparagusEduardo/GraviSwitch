import pygame
from constants import SCREEN, SCREEN_HEIGHT, SCREEN_WIDTH, MAX_FPS, CHROMA_KEY, SHOW_FPS
from confirmation import Confirmation
import sound
from misc_functions import show_fps
from Adventure import Adventure

def save_read(save_num):
	archivo = open('saves/save' + str(save_num) + '.txt')
	lastlevel = 0
	
	for linea in archivo:
		linea = linea.split('=')
		if linea[0] == 'lastlevel':
			lastlevel = int(linea[1])
			if lastlevel == 12:
				lastlevel = 'COMPLETADO'
	
	return lastlevel
	

	
	
def save_menu(MUTE_MUSIC):
	save1 = save_read(1)
	save2 = save_read(2)
	save3 = save_read(3)
	
	background = pygame.image.load('images/backgrounds/fondo_marble2.png').convert()
	
	music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
	prev_song = 's3kfileselect'
	pygame.mixer.music.play(-1)
	if MUTE_MUSIC:
		pygame.mixer.music.pause()
	
	menu_image = pygame.image.load('images/gui/file_menu.png').convert()
	menu_rect = menu_image.get_rect()
	menu_pos = (SCREEN_WIDTH/2 - menu_rect.w/2 , SCREEN_HEIGHT/2 - menu_rect.h/2)
	menu_list = [(220,136), (424,136), (626,136), (388,383)]
	
	cursor_image1 = pygame.image.load('images/gui/cursor/file_cursor1.png').convert()
	cursor_image1.set_colorkey(CHROMA_KEY)
	cursor_rect1 = cursor_image1.get_rect()
	
	cursor_image2 = pygame.image.load('images/gui/cursor/file_cursor2.png').convert()
	cursor_image2.set_colorkey(CHROMA_KEY)
	cursor_rect2 = cursor_image2.get_rect()
	
	cursor_image = cursor_image1
	
	cursor_state = 0

	clock = pygame.time.Clock()
	
	EXIT_GAME = False
	
	while not EXIT_GAME:
		FPS = clock.get_fps()
		if SHOW_FPS:
			
			show_fps(FPS)
		SCREEN.blit(background, (0,0))
		SCREEN.blit(menu_image, menu_pos)
		SCREEN.blit(cursor_image, menu_list[cursor_state])
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False, True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return 'Back'
				elif event.key == pygame.K_RETURN:
					if cursor_state == 0: #Valores relleno
						EXIT_GAME, MUTE_MUSIC, prev_song = Adventure(1, MUTE_MUSIC, prev_song, save1)
						save1 = save_read(1)
					elif cursor_state == 1:
						EXIT_GAME, MUTE_MUSIC, prev_song = Adventure(2, MUTE_MUSIC, prev_song, save2)
						save2 = save_read(2)
					elif cursor_state == 2:
						EXIT_GAME, MUTE_MUSIC, prev_song = Adventure(3, MUTE_MUSIC, prev_song, save3)
						save3 = save_read(3)
					elif cursor_state == 3:
						EXIT_GAME = True
					if prev_song != 's3kfileselect':
						music = pygame.mixer.music.load('sound/music/s3kfileselect.mp3')
						pygame.mixer.music.set_volume(1.0)
						pygame.mixer.music.play(-1)
						prev_song = 's3kfileselect'
						if MUTE_MUSIC:
							pygame.mixer.music.pause()
				elif event.key == pygame.K_RIGHT:
					sound.cursor.play()
					if cursor_state == 0:
						cursor_state = 1
					elif cursor_state == 1:
						cursor_state = 2
					elif cursor_state == 2:
						cursor_state = 0
				elif event.key == pygame.K_LEFT:
					sound.cursor.play()
					if cursor_state == 0:
						cursor_state = 2
					elif cursor_state == 1:
						cursor_state = 0
					elif cursor_state == 2:
						cursor_state = 1
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					sound.cursor.play()
					if cursor_state == 3:
						cursor_state = 1
						cursor_image = cursor_image1
					else:
						cursor_state = 3
						cursor_image = cursor_image2
						
				elif event.key == pygame.K_m:
					if not MUTE_MUSIC:
						print 'MUSIC - OFF'
						MUTE_MUSIC = True
						pygame.mixer.music.pause()
					else:
						print 'MUSIC - ON'
						MUTE_MUSIC = False
						pygame.mixer.music.unpause()
				
		
		clock.tick(MAX_FPS)
	return True