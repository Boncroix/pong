import pygame

ANCHO = 800
ALTO = 600

C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

ANCHO_PALA = 20
ALTO_PALA = 60

ANCHO_RED = 5
ALTO_RED = 10

CENTRO = (ANCHO/2, ALTO/2)
RADIO = 10

TAMANO_FUENTE = 100
POS_MARCADOR1 = (200, 20)
POS_MARCADOR2 = (520, 20)

MARGEN = 20


class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ping - Pong')
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

            # pintar jugador 1 (izquierda)
            jugador1 = pygame.Rect(
                MARGEN, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador1)

            # pintar marcador jugador 1 (izquierda)
            score1 = '00'
            marcador1 = pygame.font.Font(None, TAMANO_FUENTE)
            text1 = marcador1.render(score1, True, C_OBJETOS)
            self.pantalla.blit(text1, POS_MARCADOR1)

            # pintar jugador 2 (derecha)
            jugador2 = pygame.Rect(
                ANCHO - MARGEN - ANCHO_PALA, pos_alto_inicial, ANCHO_PALA, ALTO_PALA)
            pygame.draw.rect(self.pantalla, C_OBJETOS, jugador2)

            # pintar marcador jugador 2 (derecha)
            score2 = '10'
            marcador2 = pygame.font.Font(None, TAMANO_FUENTE)
            text2 = marcador2.render(score2, True, C_OBJETOS)
            self.pantalla.blit(text2, POS_MARCADOR2)

            # pintar la red
            pos_alto_red = ALTO
            while pos_alto_red > -5:
                red = pygame.Rect(ANCHO/2 - ANCHO_RED/2,
                                  pos_alto_red, ANCHO_RED, ALTO_RED)
                pygame.draw.rect(self.pantalla, C_OBJETOS, red)
                pos_alto_red -= 20

            # pintar pelota
            pygame.draw.circle(self.pantalla, C_OBJETOS, CENTRO, RADIO)

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
