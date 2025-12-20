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
flying = False

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
font = pygame.font.SysFont("Flappy Bird/LEMONMILK-Bold.otf", 50)

# Background
bg = pygame.image.load("./Flappy Bird/images/bg.png")

restart = pygame.image.load("./Flappy Bird/images/restart.png")
surface = pygame.image.load("./Flappy Bird/images/surface.png")

class Bird(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1, 4):
            img = pygame.image.load(f"./Flappy Bird/images/f{i}.png")
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.velocity = 0
        self.click = False
        

    def update(self):
        if flying == True:
            self.velocity += 0.5
            if self.velocity > 8:
                self.velocity = 8
            if self.rect.bottom < 768:
                self.rect.y += int(self.velocity)
            keys = pygame.key.get_pressed()
            if keys [K_SPACE]:
                self.velocity = -10
                self.clicked = True
                
        
            self.counter += 1
            flapcd = 5
            if self.counter > flapcd:
                self.counter = 1
                self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]
            

        

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
        if self.rect.right < 0:
            self.kill()

pipegroup = pygame.sprite.Group()
birdgroup = pygame.sprite.Group()
flappy = Bird(100, HEIGHT / 2)
birdgroup.add(flappy)

run = True
while run:
    clock.tick(fps)
    screen.blit(bg, (0, 0))
    pipegroup.draw(screen)
    birdgroup.draw(screen)
    screen.blit(surface, (0, 768))
    timenow = pygame.time.get_ticks()
    if timenow - lastpy > pipefreq:
        pipeheight = randint(-100, 100)
        toppipe = Pipe(WIDTH, int(HEIGHT / 2) + pipeheight, + 1)
        bottompipe = Pipe(WIDTH, int(HEIGHT / 2 ) + pipeheight, -1)
        pipegroup.add(bottompipe)
        pipegroup.add(toppipe)
        lastpy = timenow

    pipegroup.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    pygame.display.update()



