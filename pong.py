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
VEL_MAXIMA = 20
CENTRO_X_RECTANGULO = (ANCHO - TAM_PELOTA)/2
CENTRO_Y_RECTANGULO = (ALTO - TAM_PELOTA)/2

# CONSTANTES MARCADOR
TAM_FUENTE = 80
POSX_FUENTE = 310
POSY_FUENTE = 0
PUNTUACION_MAXIMA = 3

TAM_LETRA_GANADOR = 50


class Pelota(pygame.Rect):  # heredamos de rectangulo y nuestra propia pelota es un rectangulo
    def __init__(self):
        super(Pelota, self).__init__(  # heredamos de la clase superior
            CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO, TAM_PELOTA, TAM_PELOTA)

        # movimiento de la bola
        self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
        self.velocidad_x = randint(-VEL_MAXIMA, VEL_MAXIMA)
        while self.velocidad_x == 0:            # La velocidad no puede ser 0
            self.velocidad_x = randint(-VEL_MAXIMA, VEL_MAXIMA)

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
            self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
            self.velocidad_x = randint(-VEL_MAXIMA, -1)
            return 2
        if self.left >= ANCHO:
            print('Punto para el jugador 1')
            self.center = (CENTRO_X_RECTANGULO, CENTRO_Y_RECTANGULO)
            self.velocidad_y = randint(-VEL_MAXIMA, VEL_MAXIMA)
            self.velocidad_x = randint(1, VEL_MAXIMA)
            return 1
        return 0


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

    def __init__(self):
        self.reset()
        self.tipografia = pygame.font.SysFont('arialunicode', TAM_FUENTE)

    def incrementar(self, jugador):
        self.puntos[jugador-1] += 1

    def reset(self):
        self.puntos = [0, 0]

    def pintame(self, pantalla):
        '''
        forma mia 
        marcador = self.tipografia .render(
            f'{self.puntos[0]}                {self.puntos[1]}', True, C_OBJETOS)
        tam_img_marcador = marcador.get_width()
        posx = (ANCHO / 2) - (tam_img_marcador/2)
        pantalla.blit(marcador, (posx, POSY_FUENTE))
        '''
        i = 1
        for punto in self.puntos:
            puntuacion = str(punto)
            texto = self.tipografia.render(puntuacion, True, C_OBJETOS)
            tam_img_marcador = texto.get_width()
            pos_x = i / 4 * ANCHO - tam_img_marcador / 2
            pantalla.blit(texto, (pos_x, POSY_FUENTE))
            i += 2

    def comprobar_ganador(self):
        for jugador in range(len(self.puntos)):
            if self.puntos[jugador] == PUNTUACION_MAXIMA:
                return (f'Ha ganado el {jugador + 1} ')


class Pong:
    def __init__(self):
        pygame.init()
        # Cambiar nombre de pantalla
        pygame.display.set_caption('Ping - Pong')
        self.clock = pygame.time.Clock()
        self.tipografia = pygame.font.SysFont(
            'arialunicode', TAM_LETRA_GANADOR)

        self.pantalla = pygame.display.set_mode((800, 600))
        self.pelota = Pelota()
        pos_y = (ALTO - ALTO_PALA)/2
        self.jugador1 = Jugador(MARGEN, pos_y)
        self.jugador2 = Jugador(ANCHO - MARGEN - ANCHO_PALA, pos_y)
        self.marcador = Marcador()

    def jugar(self):    # contiene el bucle principal
        salir = False
        while not salir:
            # bucle principal (o main loop)
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

            # renderizar nuestros objetos
            self.pantalla.fill(C_FONDO)
            # pygame.draw.rect(self.pantalla, C_FONDO, ((0, 0), (ANCHO, ALTO))) es igual que la línea de arriba, pinta la pantalla completa

            self.pintar_red()                       # Pintamos la red
            hay_ganador = self.marcador.comprobar_ganador()
            if hay_ganador:
                mensaje = self.tipografia.render(hay_ganador, False, C_OBJETOS)
                tam_img_marcador = mensaje.get_size()
                pos_x = ANCHO / 2 - tam_img_marcador[0] / 2
                pos_y = ALTO / 2 - tam_img_marcador[1] / 2
                self.pantalla.blit(mensaje, (pos_x, pos_y))
            else:
                self.combrobar_teclas()
                self.pintar_pelota()                    # Pintamos la pelota

            hay_punto = self.pelota.comprobar_punto()
            if hay_punto > 0:
                self.marcador.incrementar(hay_punto)

            self.marcador.pintame(self.pantalla)

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
        '''
        if self.pelota.colliderect(self.jugador1) or self.pelota.colliderect(self. jugador2):
            self.pelota.velocidad_x = -self.pelota.velocidad_x + randint(-2, 2)
            if self.pelota.velocidad_x < -VEL_MAXIMA:
                self.pelota.velocidad_x = -VEL_MAXIMA
            if self.pelota. velocidad_x > VEL_MAXIMA:
                self.pelota.velocidad_x = VEL_MAXIMA
                self .pelota.velocidad_y = randint(
                    -VEL_MAXIMA, VEL_MAXIMA)
                self.pelota.pintame(self.pantalla)
        '''

        # ALTERNATIVA
        if self.pelota.colliderect(self.jugador1):
            self.pelota.velocidad_x = randint(1, VEL_MAXIMA)
            self.pelota.velocidad_y = randint(-VEL_MAXIMA,
                                              VEL_MAXIMA)
        if self.pelota.colliderect(self.jugador2):
            self.pelota.velocidad_x = randint(-VEL_MAXIMA, -1)
            self.pelota.velocidad_y = randint(-VEL_MAXIMA,
                                              VEL_MAXIMA)

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
