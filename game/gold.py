import pygame
from pygame.sprite import Sprite
from random import randint
pygame.init()

class Gold(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('treasurechest.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 5
        if self.rect.y > 896:
            self.rect.y = -64
            self.rect.x = randint(0, 640 - 64)

