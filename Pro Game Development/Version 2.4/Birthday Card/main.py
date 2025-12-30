import os
import pygame
import time
os.environ['SDL_VIDEO_CENTERED'] = '1'

pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill("#000000")
pygame.display.update()
pygame.display.set_caption("Birthday Card")

ing = pygame.image.load("./Birthday Card/images/cake.jpg")
image = pygame.transform.scale(ing, (600, 600))
print(image)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    font = pygame.font.SysFont("LEMONMILK-Bold.oft", 50)
    text = font.render("Happy Birthday", True, "#482727")
    textp = text.get_rect(center=(600/2, 600/2))
    screen.fill("white")
    screen.blit(image, (0, 0))
    screen.blit(text, textp)
    pygame.display.update()
    time.sleep(2)
    
    image2 = pygame.image.load("./Birthday Card/images/card.jpg")
    font = pygame.font.SysFont("LEMONMILK-Bold.oft", 50)
    text = font.render("Wish you a great birthday", True, "#482727")
    textp = text.get_rect(center=(600/2, 600/2))
    screen.fill("#000000")
    screen.blit(image2, (0, 0))
    screen.blit(text, textp)
    pygame.display.update()
    time.sleep(2)