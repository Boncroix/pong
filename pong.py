import pygame

ANCHO = 800
ALTO = 600

C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

ANCHO_PALA = 20
ALTO_PALA = 60

MARGEN = 20


class Pong:
    def __init__(self):
        pygame.init()
        self.pantalla = pygame.display.set_mode((800, 600))

    def jugar(self):    # contiene el bucle principal
        pos_alto_inicial = ALTO/2 - ALTO_PALA/2
        salir = False
        while not salir:
            # bucle principal (o main loop)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    salir = True

            # renderizar nuestros objetos

            pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO)))

            # pintar jugador 1 (izqquierda)
            jugador1 = pygame.Rect(
                MARGEN, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador1)

            # pintar jugador 2 (izqquierda)
            jugador2 = pygame.Rect(
                ANCHO - MARGEN - ANCHO_PALA, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador2)

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()


if __name__ == '__main__':
    print('Has llamado a pong.py directamente desde la línea de comandos')
    print(f'Tamaño de la pantalla {ANCHO} X {ALTO}')
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)
