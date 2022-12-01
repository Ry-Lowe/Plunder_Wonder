import pygame
pygame.init()
from pygame.sprite import Sprite

class Ship(Sprite):

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
        self.settings = game.settings
        self.x = float(self.rect.x)
        self.rect.y = self.rect.y - 20



    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def wreck(self):
        self.image = pygame.image.load("ship (13).png")
        self.image = pygame.transform.rotate(self.image, 137)
        self.settings.gold_fall_speed = 0
        self.settings.island_fall_speed = 0
        self.rect.y = 450
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.rect.y = self.rect.y - 20
        self.x = float(self.rect.x)