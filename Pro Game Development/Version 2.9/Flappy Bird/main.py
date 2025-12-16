import pygame
import os
from random import randint

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.init()
clock = pygame.time.Clock()
fps = 60
WIDTH, HEIGHT = 864, 936
pygap = 150
pipefreq = 1500
lastpy = pygame.time.get_ticks() - pipefreq


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont("Flappy Bird/LEMONMILK-Bold.otf", 50)
# Background
bg = pygame.image.load("./Flappy Bird/images/bg.png")

# Bird
f1 = pygame.image.load("./Flappy Bird/images/f1.png")
f2 = pygame.image.load("./Flappy Bird/images/f2.png")
f3 = pygame.image.load("./Flappy Bird/images/f3.png")

restart = pygame.image.load("./Flappy Bird/images/restart.png")
surface = pygame.image.load("./Flappy Bird/images/surface.png")


class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("./Flappy Bird/images/pipe.png")
        self.rect = self.image.get_rect()
        if position == 1:
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = [x, y - int(pygap / 2)]
        if position == -1:
            self.rect.topleft = [x, y + int(pygap / 2)]
 
    def update(self):
        self.rect.x -= 4
pipegroup = pygame.sprite.Group()

run = True
while run:
    clock.tick(fps)
    pipegroup.draw(screen)
    screen.blit(bg, (0,0))
    screen.blit(surface, (0,768))
    pipeheight = randint(-100, 100)
    toppipe = Pipe(WIDTH, int(HEIGHT / 2) + pipeheight, + 1)
    bottompipe = Pipe(WIDTH, int(HEIGHT / 2 ) + pipeheight, -1)
    pipegroup.add(bottompipe)
    pipegroup.add(toppipe)
    pipegroup.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    pygame.display.update()



