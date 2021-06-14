#coding:utf-8

""" pygame measure time
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

# display time since start pygame in ms
print(pygame.time.get_ticks())

# wait in ms
# pygame.time.wait(3000)

# wait in ms thank to the processor
# pygame.time.delay(3000)

# get the time since start in a object with other functions
clock = pygame.time.Clock()

# triger a user event every secondes
pygame.time.set_timer(pygame.USEREVENT, 1000)



launched = True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False

		elif event.type == pygame.USEREVENT:
			
			# display frame rate (round -> n digits after comma)
			window_surface.fill(white_color)
			size_text_surface = perso_font.render(
				f"fps : {round(clock.get_fps(), 2)}", True, blue_color)
			window_surface.blit(size_text_surface, (x, y))

			# update display
			pygame.display.flip()


	# refresh rate (fps)
	clock.tick(60)

	

	
