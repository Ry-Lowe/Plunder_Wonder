import pygame
from pygame.sprite import Sprite
pygame.init()
import random

class Gold(Sprite):

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.image.load('treasurechest.png')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.midtop


    def update(self):
