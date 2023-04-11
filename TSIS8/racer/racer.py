import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

#setup
BLACK = (0, 0, 0)
RED = (255, 0, 0)
W = 500
H = 400
sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("RACER")

#images
bg = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS8\racer\img\background.png")
car_img = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS8\racer\img\porsche_blue.png")
enemy_img = pygame.image.load(r"C:\pp2\pp2-22B030512\TSIS8\racer\img\porsche_red.png")

#boundaries
west_b = 157
east_b = 359

class Enemy:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

        self.image = enemy_img
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = int(x)
        self.rect.y = int(y)

        self.speedy = 3

    def draw(self, sc):
        0

class Player:
    def __init__ (self):
        self.image = car_img
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.x = int(W*.5)
        self.rect.y = int(H*.7)

        self.speedx = 0
    
    def update(self):
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -7
        if keystate[pygame.K_RIGHT]:
            self.speedx = 7

        self.rect.x = self.rect.x + self.speedx

        #check boundaries
        if self.rect.left < west_b:
            self.rect.left = west_b
        if self.rect.right > east_b:
            self.rect.right = east_b

#game function
def game_loop():
    enemy_x = random.randrange(west_b, east_b-51)
    enemy_y = 100

    enemy = Enemy(enemy_x, enemy_y)
    player = Player()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        player.update()
        sc.blit(bg, (0, 0))
        sc.blit(player.image, (player.rect.x, player.rect.y))
        sc.blit(enemy.image, (0, 0))
        pygame.display.update()
        clock.tick(60)

#main loop
game_loop()

pygame.quit()
quit()