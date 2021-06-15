#coding:utf-8

""" pygame play sound
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

"""
<Sound>.play(loop = 0, time = 0, fadein = 0)
		.stop()
		.fadout()
		.set_volume(0.0 -> 1.0)
		.get_volume()
		.get_length()

<mixer>.stop()
		.pause()

<music>.stop()
		.pause()
		.rewind()
		.fadout()
		.fadein()
		...
"""
# load entire file
forest_sound = pygame.mixer.Sound("sounds/AMBForst_Forest (ID 0100)_BSB.ogg")
cymbal_sound = pygame.mixer.Sound("sounds/MUSCPerc_Nepalese cymbal 1 (ID 2366)_BSB.ogg")
forest_sound.play()

# streaming with a play list (load() overwite the old sound file !)
pygame.mixer.music.load("sounds/AMBForst_Forest (ID 0100)_BSB.ogg")
pygame.mixer.music.play();

pygame.display.flip()

launched = True
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				cymbal_sound.stop()
				cymbal_sound.play()



	
