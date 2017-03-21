# Kaleid Release Version 1.0
# Gordon Swan (DelbyPicnic)
# https://delbypicnic.com
# https://github.com/DelbyPicnic/Kaleid
# 20-03-17

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((1366, 768))
pygame.display.toggle_fullscreen()

fOut = open('bookmarks.txt','w')

width = screen.get_width
height = screen.get_height

posX = 100
posY = 200

rot = 0
scaleX = 500
scaleY = 250 

screen_left = pygame.Surface((678, 758))
screen_right = pygame.Surface((678, 758))
screen_feedback = pygame.Surface((1366, 768))

def InvertSurface(surf):
	pixels = pygame.surfarray.pixels2d(surf)
	pixels ^= 2 ** 32 - 1
	del pixels
	return surf


clock = pygame.time.Clock()

while 1:
    clock.tick(100)

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN and \
                event.key == pygame.K_ESCAPE:
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        posX -= 5
    if key[pygame.K_RIGHT]:
        posX += 5
    if key[pygame.K_UP]:
        posY -= 5
    if key[pygame.K_DOWN]:
        posY += 5
    if key[pygame.K_o]:
    	rot += 1
    if key[pygame.K_p]:
    	rot -= 1
    if key[pygame.K_k]:
    	scaleX += 16
    	scaleY += 9
    if key[pygame.K_l]:
    	scaleX -= 16
    	scaleY -= 9
    if key[pygame.K_SPACE]:
        fOut.write("Pos X: " + str(posX) + " Pos Y: " + str(posY) + " Scale X: " + str(scaleX) + " Scale Y: " + str(scaleY) + " Rotation: " + str(rot) + "\n")


    screen.fill((255,255,255))
    screen_left.fill((255,255,255))
    screen_right.fill((255,255,255))


    screen_left.blit(screen_feedback, (posX, posY))
    screen_right.blit(screen_left, (0,0))
    screen_right = pygame.transform.flip(screen_right, True, False)
    screen.blit(screen_left, (5,5))
    screen.blit(screen_right, (678,5))
    screen_feedback = InvertSurface(screen)
    screen_feedback = pygame.transform.flip(screen_feedback, False, True)
    screen_feedback = pygame.transform.scale(screen_feedback, (scaleX, scaleY))
    screen_feedback = pygame.transform.rotate(screen_feedback, rot)


    pygame.display.flip()
