import pygame
import os

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.font.init()
pygame.mixer.init()
pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

p1health = 10
p2health = 10

p1 = pygame.image.load(("./Space Shooter/images/ship.png"))
p1img = pygame.transform.rotate(pygame.transform.scale(p1, (55, 40)), 90)
p2 = pygame.image.load(("./Space Shooter/images/ship2.png"))
p2img = pygame.transform.rotate(pygame.transform.scale(p2, (55, 40)), 270)
background = pygame.image.load(("./Space Shooter/images/space.png"))
BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

HEALTHFONT = pygame.font.SysFont("comicsans", 40)
WINNERFONT = pygame.font.SysFont("comicsans", 50)

def draw():
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, "#000000", BORDER)
    screen.blit(p1img, (20, 250))
    screen.blit(p2img, (800, 250))
    p1_hp = HEALTHFONT.render(f"HEALTH: {p1health}", 1, "#FFFFFF")
    p2_hp = HEALTHFONT.render(f"HEALTH: {p2health}", 1,  "#FFFFFF")
    screen.blit(p1_hp, (20, HEIGHT - 490))
    screen.blit(p2_hp, (650, HEIGHT - 490))
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    draw()
    pygame.display.update()


