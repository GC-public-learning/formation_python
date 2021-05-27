#coding:utf-8

""" pygame draw a surface
-----------------------------
"""

import pygame

# params
width = 640
height = 480
res = (width, height)
blue_color = (0, 0, 255)
white_color = (255, 255, 255)

pygame.init()
pygame.display.set_caption("My pygame game ^^ !")

window_surface = pygame.display.set_mode(res)

# fill color
window_surface.fill(blue_color)

# draw a diagonal line 
start_position = (50, 50)
end_position = (100, 100)
pygame.draw.line(window_surface, white_color, start_position, end_position)

# draw a rectangle
start_position_x = 200
start_position_y = 50
width = 100
height = 50
line_thickness = 5
rect_shape = pygame.Rect(start_position_x, start_position_y, width, height)

# if the thigness is passed in arg the shape isn't filled by the color
pygame.draw.rect(window_surface, white_color, rect_shape, line_thickness)

# draw a circle
start_position = (450, 75)
radius = 25

# draw polygon
coords = [(50, 300), (300, 400),  (500, 350), (150, 200)]
pygame.draw.polygon(window_surface, white_color, coords)

# update display
pygame.display.flip()


launched = True

while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

