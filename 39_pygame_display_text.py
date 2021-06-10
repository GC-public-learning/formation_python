#coding:utf-8

""" pygame display text
-----------------------------
"""

import pygame

# var
width = 640
height = 480
res = (width, height)
blue_color = (0, 0, 255)


# conf
pygame.init()
pygame.display.set_caption("My pygame game ^^ !")
window_surface = pygame.display.set_mode(res)

# params : type, size, optional : bold, italic
arial_font = pygame.font.SysFont("arial", 100, bold=True, italic=False)
# params : string, antialiasing, color, optional : background 
hello_text_surface = arial_font.render("Hello World !", True, blue_color)

# use a personalised font from a file
perso_font = pygame.font.Font("fonts/Jungle DF.ttf", 100)
jungle_text_surface = perso_font.render("Jungle !", True, blue_color)

# integrate the text surfaces on the main surface
window_surface.blit(hello_text_surface, (10, 10))
window_surface.blit(jungle_text_surface, (10, 150))


# update display
pygame.display.flip()

launched = True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False


