import pygame
import time
print(pygame.font.get_fonts())
print(pygame.font.match_font('informalroman'))
screen = pygame.display.set_mode((800, 600))

pygame.init()
go = pygame.surface.Surface((500, 200))
font = pygame.font.SysFont('C:\Windows\Fonts\INFROMAN.TTF', 100)
text = font.render("Wrecked", True, (255, 0, 0), (0, 80, 0))
text_rect = text.get_rect()
go.blit(text, text_rect)
go_rect = go.get_rect()

screen.blit(go, (0,0))
pygame.display.flip()

time.sleep(4)