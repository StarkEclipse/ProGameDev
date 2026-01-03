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
jump_power = -13
ms = 6

# hitbox size (width, height)
HITBOX_WIDTH = 120
HITBOX_HEIGHT = 25

# Screen
WIDTH, HEIGHT = int(736 / 1.2), int(1200 / 1.2)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Jumper")

# Load images
bg = pygame.image.load("./Sky Jumper/images/sky.png")
char = pygame.image.load("./Sky Jumper/images/char.PNG")
cloud = pygame.image.load("./Sky Jumper/images/cloud.PNG")

# Scale images
cloudimg = pygame.transform.scale(cloud, (int(cloud.get_width()*0.2), int(cloud.get_height()*0.2)))
charimg = pygame.transform.scale(char, (int(char.get_width()*0.1), int(char.get_height()*0.1)))
bgimg = pygame.transform.scale(bg, (WIDTH, HEIGHT))

clouds = []
hitboxes = []

for i in range(10):

    # visual cloud position
    cloud_rect = cloudimg.get_rect(
        topleft=(random.randint(0, WIDTH - cloudimg.get_width()), HEIGHT - i * 150)
    )
    clouds.append(cloud_rect)

    # REAL platform hitbox (independent box)
    hb_rect = pygame.Rect(
        cloud_rect.centerx - HITBOX_WIDTH//2,
        cloud_rect.centery,
        HITBOX_WIDTH,
        HITBOX_HEIGHT
    )
    hitboxes.append(hb_rect)

# character
char_rect = charimg.get_rect()
char_hitbox = (char_rect.inflate(-25, -30))
char_hitbox.center = char_rect.center
char_rect.midbottom = (clouds[1].centerx, hitboxes[1].top)

run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # gravity + movement
    velocity += gravity
    char_rect.y += velocity

    char_hitbox.center = char_rect.center

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        char_rect.x -= ms
    if keys[pygame.K_d]:
        char_rect.x += ms

    # -------------- COLLISION ONLY WITH HITBOX --------------
    for hb in hitboxes:
        if char_hitbox.colliderect(hb) and velocity > 0:
            char_rect.bottom = hb.top
            velocity = jump_power

    # draw background
    screen.blit(bgimg, (0, 0))

    # draw clouds (visual only)
    for c in clouds:
        screen.blit(cloudimg, c)

    # draw REAL hitboxes
    for hb in hitboxes:
        pygame.draw.rect(screen, ("#FFFFFF"), hb, 2)

    
    # draw character
    screen.blit(charimg, char_rect)
    pygame.draw.rect(screen, ("#00CCFF"), char_rect, 1)
    pygame.draw.rect(screen, ("#00FF0D"), char_hitbox, 2)

    pygame.display.update()

pygame.quit()