import pygame
from constants import SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT, SHOW_FPS, MAX_FPS, CHROMA_KEY
from level import Level
from load_level import Read_File
from misc_functions import show_fps
from confirmation import Confirmation
import sound


def Save_Level(map_data, archivo):
	for linea in map_data['mapa']:
		archivo.write(linea)
		archivo.write('\n')
	archivo.write(':Fondo ' + map_data['fondo'] + '\n')
	archivo.write(':Musica ' + map_data['musica'] + '\n')
	archivo.write(':Pared ' + map_data['pared'] + '\n')

def Test_Level(map_data, archivo, MUTE_MUSIC):
	Save_Level(map_data, archivo)
	archivo.close()
	#print map_data['mapa'][1]
	return Level('temp', MUTE_MUSIC, 's3kfileselect', 'custom/')

def Edit_Level(lvl_num, MUTE_MUSIC):
	lvl_name = 'custom' + str(lvl_num)
	base = open('levels/custom/base_lvl.txt', 'r')
	templvl = open('levels/custom/temp.txt', 'w')
	EXIT_MENU = False
	EXIT_GAME = False
	finished_level = False
	
	x_position = []
	y_position = []
	for i in range(32):
		x_position.append(i*32)
		if i < 18:
			y_position.append(i*32)
	#print x_position
	#print y_position
	
	wall_image = pygame.image.load('images/tiles/wall_base.png').convert()
	box_image = pygame.image.load('images/tiles/box.png').convert()
	player_image = pygame.image.load('images/Isaac/stand.png').convert()
	player_image.set_colorkey(CHROMA_KEY)
	jump_image = pygame.image.load('images/tiles/jumpbox.png').convert()
	
	editor_screen = pygame.Surface((1024,576))
	editor_screen.fill((175,167,124))
	
	data = {} #info del mapa
	data['mapa'], data['fondo'], data['musica'], data['pared'], data['graviswitch'], data['g_spin'], data['g_spin_spd'] = Read_File('custom/base_lvl.txt')
	base.close()
	no_place = [] #Espacios prohibidos para colocar bloques.
	
	current_y1 = 0
	for linea in data['mapa']:
		current_x1 = 0
		for cuadro in linea.strip('\n'):
			if cuadro == 'W':
				editor_screen.blit(wall_image, (current_x1*32,current_y1*32))
			elif cuadro == 'P':
				editor_screen.blit(player_image, (current_x1*32,current_y1*32))
				no_place.append((current_x1,current_y1))
			elif cuadro == 'B':
				editor_screen.blit(box_image, (current_x1*32,current_y1*32))
			elif cuadro == 'J':
				editor_screen.blit(jump_image, (current_x1*32,current_y1*32))
			elif cuadro == 'S':
				pass
			elif cuadro == 'D':
				pass
			elif cuadro == 'F':
				pass
			elif cuadro == 'C':
				pass
			elif cuadro == 'G' and len(gravi_list) == 0:
				pass
			current_x1 += 1
		current_y1 +=1

	pygame.display.set_mode((SCREEN_WIDTH +192, SCREEN_HEIGHT))
	fondo = pygame.image.load('images/backgrounds/lvl_editor.png').convert()
	
	current_x1 = 0#Reciclando variables
	current_y1 = 0
	cursor_image1 = pygame.image.load('images/gui/cursor/lvl_editor1.png').convert()
	cursor_image1.set_colorkey(CHROMA_KEY)
	cursor_rect1 = cursor_image1.get_rect()
	
	x2_pos = [1035, 1099,1037]
	y2_pos = [69,133,197, 255,413,466,519]
	states = [['W','B','F','G','B1','B2','B3'],['D','J','S','C','B1','B2','B3'],['W','B','F','G','B1','B2','B3']]
	
	current_x2 = 0
	current_y2 = 0
	cursor_image2a = pygame.image.load('images/gui/cursor/lvl_editor2.png').convert()
	cursor_image2a.set_colorkey(CHROMA_KEY)
	cursor_image2b = pygame.image.load('images/gui/cursor/lvl_editor3.png').convert()
	cursor_image2b.set_colorkey(CHROMA_KEY)
	cursor_image2 = cursor_image2a
	cursor_rect2 = cursor_image2.get_rect()
	cursor2_state = 'W'
	
	clock = pygame.time.Clock()
	
	while not EXIT_MENU:
		cursor_pos1 = [x_position[current_x1], y_position[current_y1]] #Actualiza la posicion del cursor
		cursor_pos2 = [x2_pos[current_x2], y2_pos[current_y2]]
		cursor_rect1.topleft = cursor_pos1
		cursor_rect2.topleft = cursor_pos2
		cursor2_state = states[current_x2][current_y2]
		#print cursor2_state
		SCREEN.blit(fondo,(0,0))
		SCREEN.blit(editor_screen,(0,0))
		SCREEN.blit(cursor_image1,cursor_rect1)
		SCREEN.blit(cursor_image2,cursor_rect2)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_d:
					sound.cursorleft.play()
					if current_x1 == 31:
						current_x1 = 0
					else:
						current_x1 += 1
				elif event.key == pygame.K_a:
					sound.cursorleft.play()
					if current_x1 == 0:
						current_x1 = 31
					else:
						current_x1 -= 1		
				elif event.key == pygame.K_w:
					sound.cursorleft.play()
					if current_y1 == 0:
						current_y1 = 17
					else:
						current_y1 -= 1
				elif event.key == pygame.K_s:
					sound.cursorleft.play()
					if current_y1 == 17:
						current_y1 = 0
					else:
						current_y1 += 1
				elif event.key == pygame.K_RIGHT:
					sound.cursorright.play()
					if current_x2 == 1:
						current_x2 = 0
					elif current_x2 == 2:
						pass
					else:
						current_x2 += 1
				elif event.key == pygame.K_LEFT:
					sound.cursorright.play()
					if current_x2 == 0:
						current_x2 = 1
					elif current_x2 == 2:
						pass
					else:
						current_x2 -= 1		
				elif event.key == pygame.K_UP:
					sound.cursorright.play()
					if current_y2 == 0:
						current_y2 = 6
						current_x2 = 2
						cursor_image2 = cursor_image2b
					elif current_y2 == 4:
						current_x2 = 0
						cursor_image2 = cursor_image2a
						current_y2 -=1
					else:
						current_y2 -= 1
				elif event.key == pygame.K_DOWN:
					sound.cursorright.play()
					if current_y2 == 3:
						current_x2 = 2
						current_y2 +=1
						cursor_image2 = cursor_image2b
					elif current_y2 == 6:
						current_y2 = 0
						current_x2 = 0
						cursor_image2 = cursor_image2a
					else:
						current_y2 += 1
				elif event.key == pygame.K_RETURN:
					if cursor2_state == 'B1':
						
						finished_level, EXIT_MENU, EXIT_GAME, MUTE_MUSIC, prev_song = Test_Level(data, templvl, MUTE_MUSIC)
						if EXIT_MENU:
							return EXIT_GAME, MUTE_MUSIC
						templvl = open('levels/custom/temp.txt', 'w')
						SCREEN.blit(fondo,(0,0))
						pygame.display.flip()
						music = pygame.mixer.music.load('sound/music/JumpingBat.wav')
						prev_song = 's3kfileselect'
						pygame.mixer.music.set_volume(1.0)
						pygame.mixer.music.play(-1)
						if MUTE_MUSIC:
							pygame.mixer.music.pause()
					elif cursor2_state == 'B2':
						if finished_level:
							print 'GUADDAD'
					elif cursor2_state == 'B3' and Confirmation():
						EXIT_MENU = True
					elif (current_x1, current_y1) in no_place:
						print 'NOOOOOOO'
					else:
						if cursor2_state == 'W':
							paste_image = wall_image
						elif cursor2_state == 'B':
							paste_image = box_image
						elif cursor2_state == 'J':
							paste_image = jump_image
						elif cursor2_state == 'S':
							pass
						elif cursor2_state == 'D':
							pass
						elif cursor2_state == 'F':
							pass
						elif cursor2_state == 'C':
							pass
						elif cursor2_state == 'G':
							pass
						editor_screen.blit(paste_image, (current_x1*32,current_y1*32))
						
						#data['mapa'][current_x1][current_y1] = cursor2_state
						templine = ''
						temp_x = 0
						#print current_x1
						linea = data['mapa'][current_x1]
						#print linea
						for cuadro in data['mapa'][current_y1]:
							#print cuadro
							if temp_x == current_x1:
								templine += cursor2_state
							else:
								templine += cuadro
							temp_x += 1
							#print templine
						print templine
						data['mapa'][current_y1] = templine
		#fsdfsdfsdfsdf
		FPS = clock.get_fps()
		if SHOW_FPS:
			show_fps(FPS)
		clock.tick(MAX_FPS)
		
	
	pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	return EXIT_GAME, MUTE_MUSIC
	

