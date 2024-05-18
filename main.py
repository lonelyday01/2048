import sys

import pygame

import constantes

# Inicializar Pygame
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))

# titulo del juego
pygame.display.set_caption("2048")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
