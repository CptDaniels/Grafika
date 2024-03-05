import pygame

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Figury")

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

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(win, BIALY, (0, 0, 600, 600))
    pygame.draw.rect(win, CZARNY, (0, 0, 600, 600), 5)
    pygame.draw.circle(win, CZARNY, (300, 300), 200, 0)
    pygame.draw.rect(win, ZOLTY, (200, 200, 200, 200))
    #pygame.draw.rect(win, ZOLTY, (160, 30, 100, 100))

    pygame.display.update()