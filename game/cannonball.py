import pygame
from pygame.sprite import Sprite
from random import randint
from island import Island

import math
pygame.init()

class Cannonball(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('cannonBall.png')
        self.rect = self.image.get_rect()
        self.fall_time = 0
        self.speed_y = 0
        self.speed_x = 4
        self.island = Island(self)
        self.rect.y = 20
        self.rect.x = 20
        self.fall_time = 0

    def update(self):
        self.island = Island(self)
        self.rect.y = self.island.rect.y + 164
        if self.rect.y > 896:
            self.rect.y = -10
            #self.ship_gold_flag = False

