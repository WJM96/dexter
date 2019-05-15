import sys
import pygame
from dexter.phys import *

pygame.init()
screen = pygame.display.set_mode((500, 300))

box = Box(Vec2(20, 30), 64, 64)

print(pygame)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # screen.fill((255, 255, 255))
    box.debug_draw(screen)
    pygame.display.update()