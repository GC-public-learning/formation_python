#coding:utf-8

""" pygame rect object
-----------------------------
"""

import pygame
import time

# var
width = 640
height = 480
res = (width, height)
red = (255, 0, 0)
black = (0, 0, 0)


"""

some rect features
----------------------
rect.copy()
rect.move() rect.move_ip()
rect.inflate() -> reduce or enlarge the rect
rect.cooliderect() -> detect collisions

"""

# conf
pygame.init()
pygame.display.set_caption("My pygame game ^^ !")
window_surface = pygame.display.set_mode(res)


# draw a rectangle and a copy of it
start_position_x = 200
start_position_y = 50
width = 100
height = 50
rect_shape = pygame.Rect(start_position_x, start_position_y, width, height)
rect_shape2 = rect_shape.copy()
rect_shape2.x = start_position_x + 200
pygame.draw.rect(window_surface, red, rect_shape)
pygame.draw.rect(window_surface, red, rect_shape2)


# update display
pygame.display.flip()

launched = True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

	# stop loop when the 2 rect shapes collide
	while not rect_shape.colliderect(rect_shape2):
		time.sleep(0.01)
		window_surface.fill(black)

		# change rect 1 position to move it to the right
		rect_shape.x +=1
		pygame.draw.rect(window_surface, red, rect_shape)
		pygame.draw.rect(window_surface, red, rect_shape2)
		pygame.display.flip()

