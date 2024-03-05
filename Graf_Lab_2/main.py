import pygame
import math
import sys

pygame.init()
width = 600
height = 600
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Zadanie 1")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

r = 150
srodek= (width // 2, height // 2)

def draw_polygon(surface):
    a = []
    for i in range(15):
        angle = 2 * math.pi * i / 15
        x = srodek[0] + int(r * math.cos(angle))
        y = srodek[1] + int(r * math.sin(angle))
        a.append((x, y))
    pygame.draw.polygon(surface, CZERWONY, a, 0)

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        win.fill(BIALY)

        wielokat = pygame.Surface((width, height), pygame.SRCALPHA)
        pygame.draw.rect(wielokat, CZARNY, (300, 300, 200, 200))
        draw_polygon(win)
        #pygame.draw.polygon(wielokat, CZERWONY, a, 2)
        pygame.display.update()


    #pygame.draw.rect(wielokat, CZARNY, (300, 300, 200, 200))
    # pygame.draw.polygon(win, CZERWONY, a, 2)
    #pygame.draw.circle(win, CZARNY, (300, 300), 200, 0)
    #pygame.draw.rect(win, ZOLTY, (200, 200, 200, 200))
    #pygame.draw.rect(win, ZOLTY, (160, 30, 100, 100))

        