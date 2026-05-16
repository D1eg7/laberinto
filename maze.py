from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, imagen_jugador, jugador_x, jugador_y, velocidad_jugador):
        super().__init__()
        self.imagen = transform.scale(image.load(imagen_jugador), (40, 40))
        self.velocidad = velocidad_jugador
        self.rect = self.imagen.get_rect()
        self.rect.x = jugador_x
        self.rect.y = jugador_y




    def mostrar(self):
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        teclas_presionadas = key.get_pressed()
        if teclas_presionadas[K_LEFT]:
            self.rect.x -= self.velocidad
            self.colisionar(1, 0)
            if self.rect.x < 0:
                self.rect.x = 0
        if teclas_presionadas[K_RIGHT]:
            self.rect.x += self.velocidad
            self.colisionar(-1, 0)
            if self.rect.x > (ancho - 45):
                self.rect.x = (ancho - 45)
        if teclas_presionadas[K_UP]:
            self.rect.y -= self.velocidad
            self.colisionar(0, 1)
            if self.rect.y < 0:
                self.rect.y = 0
        if teclas_presionadas[K_DOWN]:
            self.rect.y += self.velocidad
            self.colisionar(0, -1)
            if self.rect.y > (alto - 45):
                self.rect.y = (alto - 45)
    def colisionar(self, move_x, move_y):
        for pared in lista_paredes:
            if sprite.collide_rect(self, pared):
                while sprite.collide_rect(self, pared):
                    self.rect.x += move_x
                    self.rect.y += move_y


class Enemy(GameSprite):
    def __init__(self, imagen_jugador, jugador_x, jugador_y, velocidad_jugador, x2, y2):
        super().__init__(imagen_jugador, jugador_x, jugador_y, velocidad_jugador)
        self.x2 = x2
        self.y2 = y2
        self.x1 = jugador_x
        self.y1 = jugador_y
    def update(self):
        if self.rect.x > self.x2:
            self.rect.x -= self.velocidad
        if self.x2 > self.rect.x:
            self.rect.x += self.velocidad
        if self.rect.y > self.y2:
            self.rect.y -= self.velocidad      
        if self.y2 > self.rect.y:
            self.rect.y += self.velocidad
        if self.rect.x == self.x2:
            self.x2 = self.x1
            self.x1 = self.rect.x
        if self.rect.y == self.y2:
            self.y2 = self.y1
            self.y1 = self.rect.y

class Wall(sprite.Sprite):
    def __init__(self, color_r, color_g, color_b, pared_x, pared_y, ancho, alto):
        super().__init__()
        self.color_r = color_r
        self.color_g = color_g
        self.color_b = color_b
        self.ancho = ancho
        self.alto = alto
        #Imagen de la pared
        self.imagen = Surface((self.ancho, self.alto))
        self.imagen.fill((color_r, color_g, color_b))
        #Almecenar propiedad rect
        self.rect = self.imagen.get_rect()
        self.rect.x = pared_x
        self.rect.y = pared_y
    def dibujar(self):
        ventana.blit(self.imagen, (self.rect.x, self.rect.y))

#Escena del juego
ancho = 500
alto = 500
ventana = display.set_mode((ancho, alto))
display.set_caption("background2.jpg")
fondo = transform.scale(image.load('background2.jpg'), (ancho, alto))

#Paredes  R  G  B  X   Y  Ancho Alto
w1 = Wall(0, 0, 0, 0, 0, ancho, 60)
w2 = Wall(0, 0, 0, 0, 430, ancho, 70)
w3 = Wall(0, 0, 0, 70, 30, 10, 330)
w4 = Wall(0, 0, 0, 240, 300, 10, 130)
w5 = Wall(0, 0, 0, 140, 300, 105, 10)
w6 = Wall(0, 0, 0, 410, 30, 10, 305)
w7 = Wall(0, 0, 0, 230, 190, 190, 10)
w8 = Wall(0, 0, 0, 315, 325, 105, 10)
w9 = Wall(0, 0, 0, 230, 120, 10, 70)
w10 = Wall(0, 0, 0, 410, 380, 10, 50)

lista_paredes = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10]
juego = True
finish = False
reloj = time.Clock()
fps = 60
#Musica
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()

sonido_derrota = mixer.Sound('lose.ogg')
sonido_victoria = mixer.Sound('win.ogg')
#Carteles
font.init()
font = font.SysFont(None, 70)
cartel_ganar = font.render('You win!', True, (111, 135, 146))
cartel_perder = font.render('You lose!', True, (255, 90, 80))

pacman = Player('hero.png', 5, alto -120, 5)
enemigo = Enemy('cyborg.png', ancho -200, alto -165, 2, ancho -60, alto -165)
tesoro = GameSprite('treasure.png', ancho -65, alto -120, 0)
enemigo2 = Enemy('cyborg.png', 250, 280, 3, 370, 280)
enemigo3 = Enemy('cyborg.png', 80, 325, 2, 200, 325)
enemigo4 = Enemy('cyborg.png', 80, 60, 2, 370, 60)


while juego:
    for e in event.get():
        if e.type == QUIT:
            juego = False

    if finish != True:
        ventana.blit(fondo, (0, 0))
        pacman.mostrar()
        enemigo.mostrar()
        enemigo2.mostrar()
        enemigo3.mostrar()
        enemigo4.mostrar()
        tesoro.mostrar()
        pacman.update()
        w1.dibujar()
        w2.dibujar()
        w3.dibujar()
        w4.dibujar()
        w5.dibujar()
        w6.dibujar()
        w7.dibujar()
        w8.dibujar()
        w9.dibujar()
        w10.dibujar()
        enemigo2.update()
        enemigo.update()
        enemigo3.update()
        enemigo4.update()
        if sprite.collide_rect(pacman, tesoro):
            finish = True
            sonido_victoria.play()
            ventana.blit(cartel_ganar, (150, 225))
        if sprite.collide_rect(pacman, enemigo) or sprite.collide_rect(pacman, enemigo2) or sprite.collide_rect(pacman, enemigo3) or sprite.collide_rect(pacman, enemigo4):
            finish = True
            sonido_derrota.play()
            ventana.blit(cartel_perder, (150, 225))
        #for pared in lista_paredes:
        #    if sprite.collide_rect(pacman, pared):
        #        finish = True
        #        sonido_derrota.play()
        #        ventana.blit(cartel_perder, (150, 225))
    display.update()
    reloj.tick(fps)