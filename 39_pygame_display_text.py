#coding:utf-8

""" pygame display text
-----------------------------
"""

import pygame
import time

# var
width = 640
height = 480
res = (width, height)
blue_color = (0, 0, 255)

# params : type, size, optional : bold, italic
arial_font = pygame.font.SysFont("arial", 20, True)

# params : string, antialiasing, color, optional : background 
hello_text_surface = arial_font.render("Hello World !", False, blue_color)

# conf
pygame.init()
pygame.display.set_caption("My pygame game ^^ !")
window_surface = pygame.display.set_mode(res)



# update display
pygame.display.flip()

launched = True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False


