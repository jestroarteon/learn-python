import pygame, sys
from pygame.locals import *

#print(pygame.font.get_fonts())

pygame.init()
screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('holow')

y = 0
x = 0

while True:
    pygame.font.init()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                x1 = x - 15
                screen.blit(player, (x1, y))
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                screen.blit(player, (x, y))
            if event.key == pygame.K_UP or event.key == ord('w'):
                screen.blit(player, (x, y))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                print('left stop')
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                print('right stop')

    player = pygame.image.load('holow1.png')
    player = pygame.transform.scale(player, (300, 410))
    screen.blit(player, (x1, y))
    pygame.display.flip()
    screen.fill((255, 255, 255))