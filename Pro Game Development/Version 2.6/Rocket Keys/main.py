import pygame
from time import *
import os
from pygame.locals import *

keys = [False, False, False, False]

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

screen = pygame.display.set_mode((600, 600))
player = pygame.image.load("./images/rocket.png")
background = pygame.image.load("./images/space.png")
p_x = 200
p_y = 200

while True:
    screen.blit(background, (0,0))
    screen.blit(player, (p_x, p_y))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_w:
                keys[0] = True
            if event.key == K_a:
                keys [1] = True
            if event.key == K_s:
                keys [2] = True
            if event.key == K_d:
                keys [3] = True

        if event.type == pygame.KEYUP:
            if event.key == K_w:
                keys[0] = False
            if event.key == K_a:
                keys [1] = False
            if event.key == K_s:
                keys [2] = False
            if event.key == K_d:
                keys [3] = False
        #w up
        if keys[0]:
            if p_y > 0:
                p_y -= 7
        #a left
        if keys[1]:
            if p_x > 0:
                p_x -= 7
        #s down
        if keys[2]:
            if p_y < 380:
                p_y += 7
        #d right
        if keys[3]:
            if p_x < 450:
                p_x += 7
        
    
    pygame.display.update()