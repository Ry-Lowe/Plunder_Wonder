import pygame
import sys
from ship import Ship
from settings import Settings
from gold import Gold
from random import randint
from island import Island
import time
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
        self.endgame = False

    def run_game(self):
        clock = pygame.time.Clock()
        while True:
            self.check_events()
            self.check_collisions()
            if self.endgame == True:
                self.ship.update()
                self.update_screen()
                time.sleep(2)
                self.restart()
                break
            self.ship.update()
            self.gold.update()
            self.island.update()
            self.update_screen()
            clock.tick(60)

    def restart(self):
        self.endgame = False
        self.settings.gold_fall_speed = 5
        self.settings.island_fall_speed = 5
        self.island.rect.y = -256
        self.ship.image = pygame.image.load("ship (1).png")
        self.ship.image = pygame.transform.rotate(self.ship.image, 180)
        self.ship.rect.midbottom = self.screen_rect.midbottom
        self.ship.rect.y -= 20
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
            self.endgame = True

        if gold_island == True:
            if self.island.rect.x > 70:
                self.gold.rect.x = randint(0, self.island.rect.x)
            elif self.island.rect.x < 70:
                self.gold.rect.x = randint(self.island.rect.x + 256, 826)





    def update_screen(self):
        self.screen.blit(background, (0,0))
        self.objects.draw(self.screen)
        pygame.display.flip()


screen = pygame.display.set_mode((896, 640))
screen_rect = screen.get_rect()
def menu():
    start = pygame.surface.Surface((896, 640))
    font1 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
    font2 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 75)
    title = font1.render("Plunder_Wonder!", True, (0, 0, 255), (0, 0, 0))
    title_rect = title.get_rect()
    begin = font2.render("Click to Begin", True, (0, 0, 255), (0, 0, 0))
    begin_rect = begin.get_rect()
    begin_rect.x = 248
    begin_rect.y = 400
    title_rect.x = 140
    start.blit(title, title_rect)
    start.blit(begin, begin_rect)
    start_rect = start.get_rect()
    start_rect.center = screen_rect.center
    screen.blit(start, start_rect)
def end_screen():

    go = pygame.surface.Surface((896,640))
    font = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 200)
    text = font.render("Wrecked", True, (255, 0, 0), (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.x = 165
    go.blit(text, text_rect)
    font1 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
    restart = font1.render("Click to restart", True, (255, 0, 0), (0, 0, 0))
    restart_rect = restart.get_rect()
    restart_rect.x = 210
    restart_rect.y = 400
    go.blit(text, text_rect)
    go.blit(restart, restart_rect)
    go_rect = go.get_rect()
    go_rect.center = screen_rect.center
    screen.blit(go, go_rect)
    pygame.display.flip()
PW = PlunderWonder()
menu()
pygame.display.flip()
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            PW.run_game()
            end_screen()
            continue
        if event.type == pygame.QUIT:
            sys.exit()













