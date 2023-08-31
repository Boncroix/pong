import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))

salir = False
while not salir:
    # bucle principal (o main loop)

    # mostrar los camios en la pantalla
    pygame.display.flip()
