import pygame

pygame.init()
pantalla = pygame.display.set_mode((800, 600))

salir = False
while not salir:
    # bucle principal (o main loop)

    for evento in pygame.event.get():
        print('Se ha producido un evento de tipo', evento.type)
        if evento.type == pygame.QUIT:
            print('Se ha cerrado la ventana')
            salir = True

    # renderizar nuestros objetos
    rectangulo = pygame.Rect(50, 100, 300, 150)
    pygame.draw.rect(pantalla, (255, 255, 255), rectangulo)

    # mostrar los cambios en la pantalla
    pygame.display.flip()

pygame.quit()
