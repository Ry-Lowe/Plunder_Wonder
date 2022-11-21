import pygame
from pygame.sprite import Sprite
pygame.init()

class Gold(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('treasurechest.png')
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.y += 10
        if self.rect.y > 896:
            self.rect.y = -64

