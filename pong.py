from random import randint
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
ANCHO_PALA = 10
ALTO_PALA = 60

# CONSTANTES RED
ANCHO_RED = 3

# CONSTANTES PELOTA
TAM_PELOTA = 15
CENTRO_X_RECTANGULO = (ANCHO - TAM_PELOTA)/2
CENTRO_Y_RECTANGULO = (ALTO - TAM_PELOTA)/2


TAMANO_FUENTE = 100
POS_MARCADOR1 = (200, 20)
POS_MARCADOR2 = (520, 20)


class Pelota(pygame.Rect):  # heredamos de rectangulo y nuestra propia pelota es un rectangulo
    def __init__(self):
        super(Pelota, self).__init__(  # heredamos de la clase superior
            CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO, TAM_PELOTA, TAM_PELOTA)

        # movimiento de la bola
        self.velocidad_y = randint(-5, 5)
        self.velocidad_x = randint(-5, 5)
        while self.velocidad_x == 0:            # La velocidad no puede ser 0
            self.velocidad_x = randint(-5, 5)

    def pintame(self, pantalla):
        # pintar el rectangulo
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self):
        self.x = self.x + self.velocidad_x
        self.y = self.y + self.velocidad_y
        if self.y <= 0:
            self.y = 0
            self.velocidad_y = - self.velocidad_y

        if self.y >= ALTO - TAM_PELOTA:
            self.y = ALTO - TAM_PELOTA
            self.velocidad_y = - self.velocidad_y

        if self.x <= 0:
            self.x = 0
            self.velocidad_x = - self.velocidad_x

        if self.x >= ANCHO - TAM_PELOTA:
            self.x = ANCHO - TAM_PELOTA
            self.velocidad_x = - self.velocidad_x


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Jugador, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)


class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ping - Pong')
        self.pantalla = pygame.display.set_mode((800, 600))
        self.pelota = Pelota()
        pos_y = (ALTO - ALTO_PALA)/2
        self.jugador1 = Jugador(MARGEN, pos_y)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA, pos_y)

    def jugar(self):    # contiene el bucle principal
        salir = False
        while not salir:
            # bucle principal (o main loop)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

            # renderizar nuestros objetos
            pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO)))

            self.pintar_red()                       # Pintamos la red
            self.pelota.mover()                     # Mover la pelota
            self.pelota.pintame(self.pantalla)      # Pintamos la pelota
            self.jugador1.pintame(self.pantalla)    # Pintamos jugador1
            self.jugador2.pintame(self.pantalla)    # Pintamos Jugador2

            pygame.display.flip()                   # mostrar los cambios en la pantalla

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
