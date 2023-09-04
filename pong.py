import pygame
# CONSTANTES PANTALLA
MARGEN = 20
ANCHO = 800
ALTO = 600
CENTRO_X = ANCHO/2
CENTRO_Y = ALTO/2

# CONSTANTES  COMUNES OBJETOS
C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

# CONSTANTES PALAS
ANCHO_PALA = 20
ALTO_PALA = 60

# CONSTANTES RED
ANCHO_RED = 3

# CONSTANTES PELOTA
TAM_PELOTA = 10


TAMANO_FUENTE = 100
POS_MARCADOR1 = (200, 20)
POS_MARCADOR2 = (520, 20)


class Pelota:
    def __init__(self):
        # definición del rectangulo
        self.rectangulo = pygame.Rect(
            (ANCHO - TAM_PELOTA)/2, (ALTO - TAM_PELOTA)/2, TAM_PELOTA, TAM_PELOTA)

    def pintame(self, pantalla):
        # pintar el rectangulo
        pygame.draw.rect(pantalla, C_OBJETOS, self.rectangulo)


class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ping - Pong')
        self.pantalla = pygame.display.set_mode((800, 600))
        self.pelota = Pelota()

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

            self.pintar_red()

            self.pelota.pintame(self.pantalla)

            # mostrar los cambios en la pantalla
            pygame.display.flip()

        pygame.quit()

    def pintar_red(self):
        # pintar la red Tonny
        tramo_pintado = 15
        tramo_vacio = 10
        centro_red = ANCHO / 2
        for y in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(self.pantalla, C_OBJETOS, (centro_red, y),
                             (centro_red, y + tramo_pintado), ANCHO_RED)


if __name__ == '__main__':
    print('Has llamado a pong.py directamente desde la línea de comandos')
    print(f'Tamaño de la pantalla {ANCHO} X {ALTO}')
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong.py desde una sentencia import')
    print('El nombre del paquete ahora es', __name__)
