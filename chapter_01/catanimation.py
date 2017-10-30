import pygame, sys
from pygame.locals import *

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Cat Animation")

WHITE = (255, 255, 255)
catImg = pygame.image.load('cat.png')
catX = 10
catY = 10
velocity = 5

right = 'r'
left = 'l'
up = 'u'
down = 'd'

soundObj = pygame.mixer.Sound('pickup.wav')

direction = right

while True:
    DISPLAYSURF.fill(WHITE)

    changedDir = False

    if direction == right:
        catX += velocity
        if catX == 280:
            direction = down
            changedDir = True
    elif direction == down:
        catY += velocity
        if catY == 220:
            direction = left
            changedDir = True
    elif direction == left:
        catX -= velocity
        if catX == 10:
            direction = up
            changedDir = True
    elif direction == up:
        catY -= velocity
        if catY == 10:
            direction = right
            changedDir = True

    DISPLAYSURF.blit(catImg, (catX, catY))
    if changedDir:
        soundObj.play(0, 0, 0)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)
