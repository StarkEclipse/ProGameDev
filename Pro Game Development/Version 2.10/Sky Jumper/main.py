import pygame
import os
import random

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
fps = 60

# Physics
gravity = 0.4
velocity = 0
jump_power = -11
ms = 6
hb = (30, 0)



# Screen
WIDTH, HEIGHT = int(736 / 1.2), int(1200 / 1.2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Jumper")

# Loading
bg = pygame.image.load("./Sky Jumper/images/sky.png")
char = pygame.image.load("./Sky Jumper/images/char.PNG")
cloud = pygame.image.load("./Sky Jumper/images/cloud.PNG")

# Sclaing
cloudimg = pygame.transform.scale(cloud, (int(cloud.get_width() * 0.2), int(cloud.get_height() * 0.2)))
charimg = pygame.transform.scale(char, (int(char.get_width() * 0.1), int(char.get_height() * 0.1)))
bgimg = pygame.transform.scale(bg, (float(736 / 1.2), (1200 / 1.2)))

# Cloud config
clouds = []
hitboxes = []
for i in range(10):
    rect = cloudimg.get_rect(
    topleft=(random.randint(0, WIDTH - cloudimg.get_width()), HEIGHT - i * 150))

    clouds.append(rect)
    hitboxes.append(rect.inflate(*hb))

char_rect = charimg.get_rect()
first_cloud = clouds[1]
char_rect.midbottom = (
    first_cloud.centerx, first_cloud.top
)

run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    velocity += gravity
    char_rect.y += velocity

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        char_rect.x -= ms
    if keys[pygame.K_d]:
        char_rect.x += ms

    for hb_rect in hitboxes:
        if char_rect.colliderect(hb_rect) and velocity > 0:
            char_rect.bottom = hb_rect.top
            velocity = jump_power

    # Draw bg
    screen.blit(bgimg, (0, 0))

    # Draw Clouds
    for cloud_rect, hb_rect in zip(clouds, hitboxes):
        screen.blit(cloudimg, cloud_rect)

        pygame.draw.rect(screen, ("#FF0000"), hb_rect, 1)

    # Draw character
    screen.blit(charimg, char_rect)
    
    pygame.display.update()

pygame.quit()