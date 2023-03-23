import pygame
import datetime
pygame.init()

W = 1000
H = 1000
FPS = 20
clock = pygame.time.Clock()

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Do not give up!! Do not quit there!!")

clocks = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS7\photos-chasy\back.png")
back = clocks.get_rect(center = (W//2, H//2))

nurs = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS7\photos-chasy\body.png")
smlHand = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS7\photos-chasy\hand1.png")
bgHand = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS7\photos-chasy\hand2.png")

sc.blit(clocks, back)
sc.blit(nurs, (400, 200))
sc.blit(bgHand, (100, 320))
sc.blit(smlHand, (0, 0))
pygame.display.update()

t = datetime.datetime.now()
angle = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)