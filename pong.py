from random import randint
import pygame

# CONSTANTES PANTALLA
MARGEN = 20
ANCHO = 800
ALTO = 600
CENTRO_X = ANCHO/2
CENTRO_Y = ALTO/2
FPS = 30

# CONSTANTES  COMUNES OBJETOS
C_OBJETOS = (255, 255, 255)
C_FONDO = (100, 100, 100)

# CONSTANTES JUGADORES
VELOCIDAD_JUGADOR = 10
ARRIBA = True
ABAJO = False
ANCHO_PALA = 10
ALTO_PALA = 60

# CONSTANTES RED
ANCHO_RED = 3

# CONSTANTES PELOTA
TAM_PELOTA = 15
VELOCIDAD_PELOTA = 30
CENTRO_X_RECTANGULO = (ANCHO - TAM_PELOTA)/2
CENTRO_Y_RECTANGULO = (ALTO - TAM_PELOTA)/2


class Pelota(pygame.Rect):  # heredamos de rectangulo y nuestra propia pelota es un rectangulo
    def __init__(self):
        super(Pelota, self).__init__(  # heredamos de la clase superior
            CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO, TAM_PELOTA, TAM_PELOTA)

        # movimiento de la bola
        self.velocidad_y = randint(-VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)
        self.velocidad_x = randint(-VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)
        while self.velocidad_x == 0:            # La velocidad no puede ser 0
            self.velocidad_x = randint(-VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)

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

    def comprobar_punto(self):
        if self.right <= 0:
            print('Punto para el jugador 2')
            self.center = (CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO)
            self.velocidad_y = randint(-VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)
            self.velocidad_x = randint(-VELOCIDAD_PELOTA, -1)
            return 2
        if self.left >= ANCHO:
            print('Punto para el jugador 1')
            self.center = (CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO)
            self.velocidad_y = randint(-VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)
            self.velocidad_x = randint(1, VELOCIDAD_PELOTA)
            return 2


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Jugador, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self, direccion):
        if direccion == ARRIBA:
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= VELOCIDAD_JUGADOR
        if direccion == ABAJO:
            if self.y >= ALTO - ALTO_PALA:
                self.y = ALTO - ALTO_PALA
            else:
                self.y += VELOCIDAD_JUGADOR


class Marcador:
    '''
        - Guardar la puntuación del jugador 1
        - Guardar la puntuación del jugador 2
        - Metodo para ponerse a cero
        - Metodo para pintarse, mostrarse en la pantalla
        - Pong tiene un atributo que llama a la instancia marcador
    '''
    pass


class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ping - Pong')
        self.clock = pygame.time.Clock()

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

            self.combrobar_teclas()

            # renderizar nuestros objetos
            self.pantalla.fill(C_FONDO)
            # pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO))) es igual que la línea de arriba, pinta la pantalla completa
            pygame.draw.line(self.pantalla, C_OBJETOS,
                             (0, ALTO_PALA), (ANCHO, ALTO_PALA))
            pygame.draw.line(self.pantalla, C_OBJETOS,
                             (0, ALTO - ALTO_PALA), (ANCHO, ALTO - ALTO_PALA))

            self.pintar_red()                       # Pintamos la red
            self.pintar_pelota()                    # Pintamos la pelota
            self.pelota.comprobar_punto()
            self.jugador1.pintame(self.pantalla)    # Pintamos jugador1
            self.jugador2.pintame(self.pantalla)    # Pintamos Jugador2

            pygame.display.flip()                   # mostrar los cambios en la pantalla
            self.clock.tick(FPS)

        pygame.quit()

    def combrobar_teclas(self):
        estado_teclas = pygame.key.get_pressed()
        if estado_teclas[pygame.K_a]:
            self.jugador1.mover(ARRIBA)
        if estado_teclas[pygame.K_z]:
            self.jugador1.mover(ABAJO)
        if estado_teclas[pygame.K_UP]:
            self.jugador2.mover(ARRIBA)
        if estado_teclas[pygame.K_DOWN]:
            self.jugador2.mover(ABAJO)

    def pintar_pelota(self):
        # Mover la pelota
        self.pelota.mover()
        # Comprobar rebotes con los jugadores(colliderect)
        if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self. jugador2):
            self.pelota.velocidad_x = -self.pelota.velocidad_x + randint(-2, 2)
            if self.pelota.velocidad_x < -VELOCIDAD_PELOTA:
                self.pelota.velocidad_x = -VELOCIDAD_PELOTA
            if self.pelota. velocidad_x > VELOCIDAD_PELOTA:
                self.pelota.velocidad_x = VELOCIDAD_PELOTA
                self .pelota.velocidad_y = randint(
                    -VELOCIDAD_PELOTA, VELOCIDAD_PELOTA)
                self.pelota.pintame(self.pantalla)

        self.pelota.pintame(self.pantalla)

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
