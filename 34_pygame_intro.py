#coding:utf-8

""" pygame intro
----------------------

Pygame is a set of Python modules designed for writing video games. Pygame 
adds functionality on top of the excellent SDL library. This allows you to 
create fully featured games and multimedia programs in the python language. 
Pygame is highly portable and runs on nearly every platform and operating system.
"""

import pygame

# minimal configuration to run a window with its loop
pygame.init()
screen = pygame.display.set_mode((640, 480))

launched = True

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False