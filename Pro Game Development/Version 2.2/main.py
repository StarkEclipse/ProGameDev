import pgzrun
from random import randint


TITLE = "Flappy Ball"
HEIGHT = 500
WIDTH = 800

gravity = 2000

# Values
R = randint (0, 255)
G = randint (0, 255)
B = randint (0, 255)

CLR = R, G, B

class Ball:

    def __init__(self, innitial_x, innitial_y):
        
        self.x = innitial_x
        self.y = innitial_y
        self.vx = 200
        self.vy = 0
        self.radius = 40

    def draw(self):
        pos = (self.x, self.y)
        screen.draw.filled_circle(pos, self.radius, CLR)

ball = Ball(50, 100)

def update(dt):
        ui = ball.vy
        ball.vy += gravity * dt
        ball.y += (ui + ball.vy) * 0.5 * dt
        if ball.y > HEIGHT - ball.radius:
             ball.y = HEIGHT - ball.radius
             ball.vy = - ball.vy * 0.9
        ball.x += ball.vx * dt
        if ball.x > WIDTH - ball.radius or ball.x < ball.radius:
             ball.vx = - ball.vx

def draw():
    screen.clear()
    ball.draw()

def on_key_down(key):
    if key == keys.SPACE:
        ball.vy = -500

pgzrun.go()