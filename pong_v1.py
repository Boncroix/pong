from random import randint
import pygame

# CONSTANTES JUEGO
FPS = 30
# PANTALLA
BORDE = 20
ALTO = 600
ANCHO = 800
C_FONDO = (0, 255, 0)
C_OBJETOS = (255, 255, 255)
CENTRO_X = ANCHO / 2
CENTRO_Y = ALTO / 2

# RED
ALTO_RED = 10
ANCHO_RED = 5
# ZONA DE SAQUE
BORDE_ZONA_SAQUE = 100
ALTO_ZONA = ALTO - (BORDE_ZONA_SAQUE * 2)
ANCHO_ZONA = ANCHO - (BORDE_ZONA_SAQUE * 2)
GROSOR_ZONA = 5
# JUGADOR
ANCHO_PALA = 15
ALTO_PALA = 80
ARRIBA = True
ABAJO = False
VEL_JUGADOR = 10
# PELOTA
TAM_PELOTA = 15
VEL_PELOTA = 20


class Pelota(pygame.Rect):
    def __init__(self):
        super(Pelota, self).__init__(CENTRO_X - (TAM_PELOTA / 2),
                                     CENTRO_Y + (TAM_PELOTA / 2), TAM_PELOTA, TAM_PELOTA)

        self.velocidad_y = randint(-VEL_PELOTA, VEL_PELOTA)
        self.velocidad_x = randint(-VEL_PELOTA, VEL_PELOTA)
        while self.velocidad_x == 0:
            self.velocidad_x = randint(-VEL_PELOTA, VEL_PELOTA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self):
        self.x += self.velocidad_x
        self.y += self.velocidad_y

        if self.y <= 0:
            self.y = 0
            self.velocidad_y = - self.velocidad_y

        if self.y >= ALTO - TAM_PELOTA:
            self.y = ALTO - TAM_PELOTA
            self.velocidad_y = - self.velocidad_y

    def comprobar_punto(self):
        if self.x <= 0:
            print('Punto para el jugador 2')
            self.center = (CENTRO_X - (TAM_PELOTA / 2),
                           CENTRO_Y + (TAM_PELOTA / 2))


class Jugador(pygame.Rect):
    def __init__(self, x, y):
        super(Jugador, self).__init__(x, y, ANCHO_PALA, ALTO_PALA)

    def pintame(self, pantalla):
        pygame.draw.rect(pantalla, C_OBJETOS, self)

    def mover(self, direccion):
        if direccion == ARRIBA:
            print('arriba')
            if self.y <= 0:
                self.y = 0
            else:
                self.y -= VEL_JUGADOR

        if direccion == ABAJO:
            print('abajo')
            if self.y >= ALTO - ALTO_PALA:
                self.y = ALTO - ALTO_PALA
            else:
                self.y += VEL_JUGADOR


class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Ping / Pong')
        self.reloj = pygame.time.Clock()
        self.pantalla = pygame.display.set_mode((ANCHO, ALTO))
        self.jugador1 = Jugador(BORDE, (ALTO - ALTO_PALA) / 2)
        self.jugador2 = Jugador(
            ANCHO - BORDE - ANCHO_PALA, (ALTO - ALTO_PALA) / 2)
        self.pelota = Pelota()

    def jugar(self):
        salir = False
        while not salir:

            self.pantalla.fill(C_FONDO)
            self.pintar_red()
            self.comprobar_teclas()
            self.pintar_pelota()

            self.jugador1.pintame(self.pantalla)
            self.jugador2.pintame(self.pantalla)

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT or (evento.type == pygame.KEYUP and evento.key == pygame.K_ESCAPE):
                    salir = True

            pygame.display.flip()
            self.reloj.tick(FPS)

        pygame.quit()

    def comprobar_teclas(self):
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
        self.pelota.mover()

        if self.pelota.colliderect(self.jugador1):
            self.pelota.velocidad_x = randint(1, VEL_PELOTA)
            self.pelota.velocidad_y = randint(-VEL_PELOTA, VEL_PELOTA)
        if self.pelota.colliderect(self.jugador2):
            self.pelota.velocidad_x = randint(-VEL_PELOTA, -1)
            self.pelota.velocidad_y = randint(-VEL_PELOTA, VEL_PELOTA)

        self.pelota.pintame(self.pantalla)

    def pintar_red(self):
        pygame.draw.rect(self.pantalla, C_OBJETOS, (BORDE_ZONA_SAQUE,
                         BORDE_ZONA_SAQUE, ANCHO_ZONA, ALTO_ZONA), GROSOR_ZONA)

        tramo_pintado = 15
        tramo_vacio = 10
        for i in range(0, ALTO, tramo_pintado + tramo_vacio):
            pygame.draw.line(self.pantalla, C_OBJETOS, (CENTRO_X, i),
                             (CENTRO_X, i + tramo_pintado), ANCHO_RED)


if __name__ == '__main__':
    print(f'Estas llamando a pong directamente desde la línea de comandos')
    juego = Pong()
    juego.jugar()
else:
    print('Has llamado a pong desde una sentencia import')
    print(f'El nombre del paquete ahora es {__name__}')
