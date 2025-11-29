import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill("white")
pygame.display.update()

class Circle:
    def __init__(self, width, position, color, radius):

        self.color = color
        self.width = width
        self.position = position
        self.radius = radius
        self.surface = screen

    def draw(self):
        self.draw_circle = pygame.draw.circle(self.surface, self.color, self.position, self.radius, self.width)

    def grow(self, r):
        self.radius = self.radius + r
        self.draw_circle = pygame.draw.circle(self.surface, self.color, self.position, self.radius, self.width)
        

circle = Circle(0, (300, 300), "black", 20)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("white")
            circle.draw()
            pygame.display.update()
            
        if event.type == pygame.MOUSEBUTTONUP:
            screen.fill("white")
            circle.grow(30)
            pygame.display.update()

        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            white_circle = Circle(0, (pos), "blue", 20)
            white_circle.draw()
            pygame.display.update()
