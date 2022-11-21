import pygame
import time
import sys
from ship import Ship
from settings import Settings
from gold import Gold
from random import randint

water = pygame.image.load('tile_73.png')
water_rect = water.get_rect()


class PlunderWonder:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((896, 640))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.gold = pygame.sprite.Group()
        self.create_gold()


    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            self.gold.update()
            clock.tick(60)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self.check_keyup_events(event)

    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def create_gold(self):
        gold = Gold(self)
        gold.rect.x = randint(0, 640-64)
        gold.rect.y = -64
        self.gold.add(gold)



    def draw_background(self):
        for y in range(10):
            for x in range(14):
                self.screen.blit(water, water_rect)
                water_rect.x += water_rect.width
            water_rect.x = 0
            water_rect.y += water_rect.height
        water_rect.topleft = self.screen_rect.topleft
    def update_screen(self):
        self.draw_background()
        self.ship.blitme()
        self.gold.draw(self.screen)
        pygame.display.flip()


PW = PlunderWonder()
PW.run_game()









