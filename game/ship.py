import pygame
from pygame.sprite import Sprite
pygame.init()


class Ship(Sprite):  # define ship object

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('ship (1).png')
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)
        self.rect.y = self.rect.y - 20

    def update(self):  # allow ship to move left and right
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 8
        if self.moving_left and self.rect.left > 0:
            self.x -= 8
        self.rect.x = self.x

    def wreck(self):  # define a wrecked state
        self.image = pygame.image.load("ship (13).png")
        self.image = pygame.transform.rotate(self.image, 137)
        self.rect.y = 450

