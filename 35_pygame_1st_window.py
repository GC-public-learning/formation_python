#coding:utf-8

""" pygame 1st windoww
---------------------------
"""

import pygame

"""
possible modes
-------------------
pygame.FULLSCREEN
pygame.RESIZABLE
pygame.NOFRAME

pygame.OPENGL
pygame.HWSURFACE
pygame.DOUBLEBUF
"""



# params
res = (640, 480)

pygame.init()
pygame.display.set_caption("My pygame game ^^ !")

# RESIZABLE is optional
window_surface = pygame.display.set_mode(res, pygame.RESIZABLE)

# display some infos
print(pygame.display.Info())
print(pygame.get_sdl_version())

launched = True

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

