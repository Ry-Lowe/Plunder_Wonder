import pygame
from pygame.sprite import Sprite
from random import randint

import math
pygame.init()

class Gold(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('treasurechest.png')
        self.rect = self.image.get_rect()
        self.ship_gold_flag = False
        self.fall_time = 0
        self.fall_speed = 0

    def update(self):
        self.fall_speed = 3 + math.sqrt((self.fall_time) / (1000))
        self.rect.y += self.fall_speed
        if self.rect.y > 896 or self.ship_gold_flag == True:
            self.rect.y = -64
            self.rect.x = randint(0, 640 - 64)
            self.image = pygame.image.load('treasurechest.png')
            self.ship_gold_flag = False








