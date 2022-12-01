import pygame
from pygame.sprite import Sprite
import settings
from random import randint

pygame.init()

class Island(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.surface.Surface((256, 256))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (0, 0))
        self.image.blit(pygame.image.load("tile_06.png"),
                        (0, 0))

        self.image.blit(pygame.image.load("tile_73.png"),
                        (64, 0))
        self.image.blit(pygame.image.load("tile_07.png"),
                        (64, 0))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (128, 0))
        self.image.blit(pygame.image.load("tile_08.png"),
                        (128, 0))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (192, 0))
        self.image.blit(pygame.image.load("tile_09.png"),
                        (192, 0))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (0, 64))
        self.image.blit(pygame.image.load("tile_22.png"),
                        (0, 64))
        self.image.blit(pygame.image.load("tile_23.png"),
                        (64, 64))
        self.image.blit(pygame.image.load("tile_24.png"),
                        (128, 64))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (192, 64))
        self.image.blit(pygame.image.load("tile_25.png"),
                        (192, 64))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (0, 128))
        self.image.blit(pygame.image.load("tile_38.png"),
                        (0, 128))
        self.image.blit(pygame.image.load("tile_39.png"),
                        (64, 128))
        self.image.blit(pygame.image.load("tile_40.png"),
                        (128, 128))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (192, 128))
        self.image.blit(pygame.image.load("tile_41.png"),
                        (192, 128))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (0, 192))
        self.image.blit(pygame.image.load("tile_54.png"),
                        (0, 192))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (64, 192))
        self.image.blit(pygame.image.load("tile_55.png"),
                        (64, 192))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (128, 192))
        self.image.blit(pygame.image.load("tile_56.png"),
                        (128, 192))
        self.image.blit(pygame.image.load("tile_73.png"),
                        (192, 192))
        self.image.blit(pygame.image.load("tile_57.png"),
                        (192, 192))

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midtop
        self.settings = game.settings

    def update(self):
        self.rect.y += self.settings.island_fall_speed
        if self.rect.y > 896:
            self.rect.y = -256
            self.rect.x = randint(0, 896 - 256)


        go = pygame.surface.Surface((500, 200))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Wrecked", True, (255, 0, 0), (0, 0, 0))
        text_rect = text.get_rect()
        go.blit(text, text_rect)

