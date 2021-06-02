#coding:utf-8

""" pygame draw a surface
-----------------------------
"""

import pygame

# var
width = 800
height = 600
res = (width, height)
white_color = (255, 255, 255)
png_python = pygame.image.load("img/python.png") # return a surface
jpg_snake = pygame.image.load("img/snake.jpg")

# config
pygame.init()
pygame.display.set_caption("My pygame game ^^ !")
window_surface = pygame.display.set_mode(res)
jpg_snake.convert()
png_python.convert_alpha() # alpha to handle transparency 



launched = True

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

	window_surface.fill(white_color)			
	window_surface.blit(jpg_snake, (10, 10))
	window_surface.blit(png_python, (100, 100))

	# update display
	pygame.display.flip()




