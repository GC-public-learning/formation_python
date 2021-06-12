#coding:utf-8

""" pygame events
-----------------------------
"""

import pygame

# var
width = 640
height = 480
res = (width, height)
blue_color = (0, 0, 255)
white_color = (255, 255, 255)
x = 10
y = 10


# conf
pygame.init()
pygame.display.set_caption("My pygame game ^^ !")
window_surface = pygame.display.set_mode(res, pygame.RESIZABLE)
window_surface.fill(white_color)

# use a personalised font from a file
perso_font = pygame.font.Font("fonts/Jungle DF.ttf", 50)
size_text_surface = perso_font.render(f"res : {res}", True, blue_color)
window_surface.blit(size_text_surface, (x, y))

# if a key steal down repeat the action
# params 1 : time in ms left before the repetitions begin
# params 2 : interval in ms for repetitions
pygame.key.set_repeat(1,2)

# update display
pygame.display.flip()

launched = True
while launched:
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			launched = False

		# event VIDEORESIZE -> display the res in real time
		elif event.type == pygame.VIDEORESIZE:
			window_surface.fill(white_color)
			size_text_surface = perso_font.render(
				f"res : ({event.w}, {event.h})", True, blue_color)
			window_surface.blit(size_text_surface, (x, y))
			pygame.display.flip()

		# event KEYDOWN -> move the size_text_surface on the screen
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				window_surface.fill(white_color)
				y-=1
				if y < 0: y = 0
			if event.key == pygame.K_DOWN:
				window_surface.fill(white_color)
				y+=1
				if y > window_surface.get_height() - size_text_surface.get_height(): 
					y = window_surface.get_height() - size_text_surface.get_height()
			if event.key == pygame.K_LEFT:
				window_surface.fill(white_color)
				x-=1
				if x < 0: x = 0
			if event.key == pygame.K_RIGHT:
				window_surface.fill(white_color)
				x+=1
				if x > window_surface.get_width() - size_text_surface.get_width(): 
					x = window_surface.get_width() - size_text_surface.get_width() 
			window_surface.blit(size_text_surface, (x, y))
			pygame.display.flip()





