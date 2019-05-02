import pygame
import sys

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s')
logging.debug('Dexter engine loaded!')

'''
pygame.init()
screen = pygame.display.set_mode((500, 300))

print(pygame)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.display.update()
'''
