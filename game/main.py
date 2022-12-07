import pygame
import sys
from ship import Ship
from gold import Gold
from random import randint
from island import Island
import time

pygame.init()
pygame.mixer.music.load('intense.mp3')  # Background music
pygame.mixer.music.play(-1)
pygame.display.set_caption("Plunder Wonder!")  # window title
water = pygame.image.load('tile_73.png')  # create background
water_rect = water.get_rect()
background = pygame.surface.Surface((896, 640))
for y in range(10):
    for x in range(14):
        background.blit(water, water_rect)
        water_rect.x += water_rect.width
    water_rect.x = 0
    water_rect.y += water_rect.height
water_rect.topleft = (0, 0)
score_surface = pygame.surface.Surface((140, 65))  # creates a surface to draw score
final_score = 0
high_scoren = 0
game_end_time = 1
screen = pygame.display.set_mode((896, 640))  # create screen and rect
screen_rect = screen.get_rect()


class PlunderWonder:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((896, 640))
        self.screen_rect = self.screen.get_rect()
        self.ship = Ship(self)
        self.island = Island()
        self.gold = Gold(self)
        self.objects = pygame.sprite.Group()
        self.objects.add((self.gold, self.island, self.ship))
        self.endgame = False
        self.scoren = 0
        self.time = 0
        self.game_end_time = game_end_time
        self.final_score = self.scoren

    def run_game(self):
        clock = pygame.time.Clock()
        self.game_end_time = pygame.time.get_ticks()
        while True:
            self.check_events()
            self.check_collisions()
            if self.endgame:
                self.ship.update()
                self.update_screen()
                self.final_score = self.scoren
                time.sleep(2)
                self.restart()
                break
            self.ship.update()
            self.gold.update()
            self.island.update()
            self.score()
            self.update_screen()
            self.time = pygame.time.get_ticks()
            self.new_game_time = self.time - self.game_end_time
            self.gold.fall_time = self.new_game_time
            self.island.fall_time = self.new_game_time
            print(self.gold.fall_speed)
            clock.tick(60)

    def restart(self):
        self.endgame = False
        self.island.rect.y = -256
        self.ship.image = pygame.image.load("ship (1).png")
        self.ship.image = pygame.transform.rotate(self.ship.image, 180)
        self.ship.rect.midbottom = self.screen_rect.midbottom
        self.ship.rect.y -= 20
        self.scoren = 0
        self.gold.fall_time = self.new_game_time
        self.island.fall_time = self.new_game_time
        self.ship.moving_right = False
        self.ship.moving_left = False
        score_surface.fill((0, 0, 0))

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
        if ship_gold:
            self.gold.ship_gold_flag = True
            self.gold.kill()
            self.gold.update()
            self.scoren += 1
            self.objects.add(self.gold)
        if ship_island:
            self.ship.wreck()
            self.endgame = True

        if gold_island:
            if self.island.rect.x > 70:
                self.gold.rect.x = randint(0, self.island.rect.x)
            elif self.island.rect.x < 70:
                self.gold.rect.x = randint(self.island.rect.x + 256, 826)

    def score(self):
        score_font = pygame.font.Font('Radio_Space.ttf', 65)
        scorer = score_font.render(f"{self.scoren}", True, (255, 255, 255), (0, 0, 0))
        scorer_rect = scorer.get_rect()
        scorer_rect.x = 0
        scorer_rect.y = 10
        score_surface.blit(scorer, scorer_rect)

    def update_screen(self):
        self.screen.blit(background, (0, 0))
        self.objects.draw(self.screen)
        self.screen.blit(score_surface, (760, 0))
        pygame.display.flip()


def menu():  # start screen
    start = pygame.surface.Surface((896, 640))  # create start surface
    font1 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
    font2 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 75)
    title = font1.render("Plunder_Wonder!", True, (0, 0, 255), (0, 0, 0))
    title_rect = title.get_rect()
    begin = font2.render("Click to Begin", True, (0, 0, 255), (0, 0, 0))
    begin_rect = begin.get_rect()
    begin_rect.x = 248
    begin_rect.y = 400
    title_rect.x = 140
    font4 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 75)
    quit1 = font4.render("Press q to quit", True, (255, 0, 0), (0, 0, 0))
    quit_rect = quit1.get_rect()
    quit_rect.x = 250
    quit_rect.y = 550
    start.blit(quit1, quit_rect)
    start.blit(title, title_rect)
    start.blit(begin, begin_rect)
    start_rect = start.get_rect()
    start_rect.center = screen_rect.center
    screen.blit(start, start_rect)


PW = PlunderWonder()  # call game class
menu()  # run start screen


def end_screen():  # create end screen
    global high_scoren
    go = pygame.surface.Surface((896, 640))
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
    font2 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
    your_score = font2.render(f"Your Score: {PW.final_score}", True, (255, 0, 0), (0, 0, 0))
    your_score_rect = your_score.get_rect()
    your_score_rect.x = 210
    your_score_rect.y = 210
    go.blit(your_score, your_score_rect)
    go.blit(restart, restart_rect)
    if PW.final_score > high_scoren:
        high_scoren = PW.final_score
    font3 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
    high_score = font3.render(f"High Score: {high_scoren}", True, (255, 0, 0), (0, 0, 0))
    high_score_rect = high_score.get_rect()
    high_score_rect.x = 210
    high_score_rect.y = 310
    go.blit(high_score, high_score_rect)
    font4 = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 75)
    quit1 = font4.render("Press q to quit", True, (255, 0, 0), (0, 0, 0))
    quit_rect = quit1.get_rect()
    quit_rect.x = 250
    quit_rect.y = 550
    go.blit(quit1, quit_rect)
    go_rect = go.get_rect()
    go_rect.center = screen_rect.center
    screen.blit(go, go_rect)
    pygame.display.flip()


pygame.display.flip()  # display screens

while True:  # main loop

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:  # repeat between running game and end game screen
            PW.run_game()
            end_screen()
            continue
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()
