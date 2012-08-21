# Extraido de: http://www.losersjuegos.com.ar/referencia/ejemplos
import pygame
from pygame.sprite import Sprite

def load(index):
    "Carga una imagen de cofre en base al indice."
    image = pygame.image.load("ima/cofre_%d.bmp" %(index)).convert()
    transparent_color = image.get_at((0, 0))
    image.set_colorkey(transparent_color)
    return image


class Closed:

    def __init__(self, cofre):
        self.cofre = cofre
        self.cofre.set_frame(0)

    def update(self, key):
        if key[pygame.K_SPACE]:
            self.cofre.change_state(Opening(self.cofre))

class Opening:

    def __init__(self, cofre):
        self.cofre = cofre
        self.frames = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.delay = 0

    def update(self, key):
        self._update_animation()

    def _update_animation(self):
        self.delay -= 1

        if self.delay <= 0:
            self.delay = 60
            try:
                next_frame = self.frames.pop(0)
                self.cofre.set_frame(next_frame -1)
            except:
                self.cofre.change_state(Open(self.cofre))

class Closing:

    def __init__(self, cofre):
        self.cofre = cofre
        self.frames = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11][::-1]
        self.delay = 0

    def update(self, key):
        self._update_animation()

    def _update_animation(self):
        self.delay -= 1

        if self.delay <= 0:
            self.delay = 60
            try:
                next_frame = self.frames.pop(0)
                self.cofre.set_frame(next_frame -1)
            except:
                self.cofre.change_state(Closed(self.cofre))

class Open:

    def __init__(self, cofre):
        self.cofre = cofre

    def update(self, key):
        if key[pygame.K_SPACE]:
            self.cofre.change_state(Closing(self.cofre))


class Cofre(Sprite):
    "Representa una caja que se abre cuando el usuario pulsa la tecla SPACE."

    def __init__(self):
        Sprite.__init__(self)
        self._load_images()
        self.change_state(Closed(self))

    def change_state(self, state):
        self.state = state

    def set_frame(self, index):
        self.image = self.frames[index]

    def _load_images(self):
        "Carga todos los cuadros del cofre."
        self.frames = [load(index) for index in range(0, 12)]

    def update(self):
        key = pygame.key.get_pressed()
        self.state.update(key)

    def draw(self, screen):
        screen.blit(self.image, (120, 80))


quit = False
screen = pygame.display.set_mode((320, 240))
cofre = Cofre()
pygame.font.init()
fuente = pygame.font.Font(None, 25)
texto = fuente.render("Pulse la tecla 'space' por favor", True, (0,0,0))


while not quit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                quit = True

    screen.fill((200, 200, 200))
    cofre.update()
    screen.blit(texto, (0, 0))
    cofre.draw(screen)
    pygame.display.flip()
    pygame.time.wait(1)
