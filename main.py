import pygame, os, sys, code.constants as C
from code.level import Level
from code.titlescreen import TitleScreen
from code.menu import Menu

def main():
	pygame.init()
	pygame.display.set_caption(C.GAME_NAME)
	Menu()
	'''
	done = False
	while not done:
		TitleScreen()
		done = Level('levelTest1')
		
	done = False
	while not done:
		TitleScreen()
		done = Level('level0')
	'''
	
	#Level('level0')
	#Level('Level2')
main()


#-------TO DO------
'''
- PROBAR FRAMESKIP EN EL RASPBERRY!!

- Crear un switch y un sistema de "corriente"
- Crear un bloque que player pueda atravesar, pero no las cajas

- Menus
- CREAR NIVELES
'''
