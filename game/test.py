import pygame
import time
pygame.init()
x = pygame.time.Clock
pygame.time.get_ticks()
print(pygame.time.get_ticks())

if self.rect.y > 350:
    self.rect.x += 4
    self.rect.y = 350
elif self.rect.y < 350:
    self.rect.y = self.island.rect.y + 164
elif self.rect.x > 640 or self.rect.y > 896:
    self.rect.y = 0
    self.rect.x = self.island.rect.x + 228
    # self.image = pygame.image.load('cannonBall.png')