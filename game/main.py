import pygame
import sys
from ship import Ship
from settings import Settings
from gold import Gold
from random import randint
from island import Island
pygame.init()
pygame.display.set_caption("Plunder Wonder!")
water = pygame.image.load('tile_73.png')
water_rect = water.get_rect()
background = pygame.surface.Surface((896, 640))
for y in range(10):
    for x in range(14):
        background.blit(water, water_rect)
        water_rect.x += water_rect.width
    water_rect.x = 0
    water_rect.y += water_rect.height
water_rect.topleft = (0,0)

go = pygame.surface.Surface((500, 200))
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render("Wrecked", True, (255, 0, 0), (0, 0, 0))
text_rect = text.get_rect()
go.blit(text, text_rect)
go_rect = go.get_rect()

class PlunderWonder:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((896, 640))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.island = Island(self)
        self.gold = Gold(self)
        self.objects = pygame.sprite.Group()
        self.objects.add((self.gold, self.island, self.ship))

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            self.check_collisions()
            self.ship.update()
            self.gold.update()
            self.island.update()
            self.update_screen()
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

    def check_collisions(self):
        ship_gold = pygame.sprite.collide_rect(self.ship, self.gold)
        ship_island = pygame.sprite.collide_rect(self.ship, self.island)
        gold_island = pygame.sprite.collide_rect(self.gold, self.island)
        if ship_gold == True:
            self.gold.collect()
        if ship_island == True:
            self.ship.wreck()
            go_rect.center = self.screen_rect.center
            self.screen.blit(go, go_rect)
        if gold_island == True:
            if self.island.rect.x > 70:
                self.gold.rect.x = randint(0, self.island.rect.x)
            elif self.island.rect.x < 70:
                self.gold.rect.x = randint(self.island.rect.x + 256, 826)





    def update_screen(self):
        self.screen.blit(background, (0,0))
        self.objects.draw(self.screen)
        pygame.display.flip()


PW = PlunderWonder()
PW.run_game()









