import pygame
import os
from pygame.locals import *

# ------------------ Setup ------------------
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

background = pygame.image.load("./Space Shooter/images/space.png")

p1 = pygame.image.load("./Space Shooter/images/ship.png")
p1img = pygame.transform.rotate(pygame.transform.scale(p1, (55, 40)), 90)

p2 = pygame.image.load("./Space Shooter/images/ship2.png")
p2img = pygame.transform.rotate(pygame.transform.scale(p2, (55, 40)), 270)

bullet = pygame.image.load("./Space Shooter/images/beam.png")
bulletimg = pygame.transform.rotate(pygame.transform.scale(bullet, (15 * 3, 8 * 3)), 90)

E = 7
MAXB = 5
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)


# ------------------ Player Movement Functions ------------------

def handle_player1(keys1, p1_x, p1_y):
    # W
    if keys1[0] and p1_y > 0:
        p1_y -= E
    # A
    if keys1[1] and p1_x > 0:
        p1_x -= E
    # S
    if keys1[2] and p1_y < HEIGHT - 60:
        p1_y += E
    # D
    if keys1[3] and p1_x + 55 < BORDER.x:
        p1_x += E

    return p1_x, p1_y


def handle_player2(keys2, p2_x, p2_y):
    # Up
    if keys2[0] and p2_y > 0:
        p2_y -= E
    # Left
    if keys2[1] and p2_x > BORDER.x + BORDER.width:
        p2_x -= E
    # Down
    if keys2[2] and p2_y < HEIGHT - 60:
        p2_y += E
    # Right
    if keys2[3] and p2_x < WIDTH - 55:
        p2_x += E

    return p2_x, p2_y


# ------------------ Main Game Loop ------------------

def main():
    p1_x, p1_y = 20, 250
    p2_x, p2_y = 800, 250

    keys1 = [False, False, False, False]  # W A S D
    keys2 = [False, False, False, False]  # Up Left Down Right

    bullets1 = []
    bullets2 = []

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        screen.blit(background, (0, 0))
        pygame.draw.rect(screen, "#000000", BORDER)

        screen.blit(p1img, (p1_x, p1_y))
        screen.blit(p2img, (p2_x, p2_y))

        for b in bullets1:
            b.x += 10
            if b.x > WIDTH:
                bullets1.remove(b)
            else:
                screen.blit(bulletimg, (b.x, b.y))
        
        for l in bullets2:
            l.x -= 10
            if l.x > WIDTH:
                bullets2.remove(l)
            else:
                screen.blit(pygame.transform.rotate(bulletimg, 180), (l.x, l.y))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                # Player 1
                if event.key == K_w: keys1[0] = True
                if event.key == K_a: keys1[1] = True
                if event.key == K_s: keys1[2] = True
                if event.key == K_d: keys1[3] = True

                # Player 2
                if event.key == K_UP: keys2[0] = True
                if event.key == K_LEFT: keys2[1] = True
                if event.key == K_DOWN: keys2[2] = True
                if event.key == K_RIGHT: keys2[3] = True

                if event.key == K_LCTRL and len(bullets1) < MAXB:
                    bullet_rect = pygame.Rect(p1_x + 50, p1_y, 15, 8)
                    bullets1.append(bullet_rect)

                if event.key == K_RCTRL and len(bullets2) < MAXB:
                    bullet2_rect = pygame.Rect(p2_x - 50, p2_y, 15, 8)
                    bullets2.append(bullet2_rect)

            if event.type == KEYUP:
                # Player 1
                if event.key == K_w: keys1[0] = False
                if event.key == K_a: keys1[1] = False
                if event.key == K_s: keys1[2] = False
                if event.key == K_d: keys1[3] = False

                # Player 2
                if event.key == K_UP: keys2[0] = False
                if event.key == K_LEFT: keys2[1] = False
                if event.key == K_DOWN: keys2[2] = False
                if event.key == K_RIGHT: keys2[3] = False

        # Update players using functions
        p1_x, p1_y = handle_player1(keys1, p1_x, p1_y)
        p2_x, p2_y = handle_player2(keys2, p2_x, p2_y)

        pygame.display.update()


# Run the game
main()
