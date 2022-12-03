import pygame
import time

pygame.init()
x = pygame.time.Clock
class Settings():
    def __init__(self):
        self.ship_speed = 8
        self.gold_fall_speed = 5
        self.island_fall_speed = 5

