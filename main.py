import pygame
import os
import random
import sys
pygame.init()
font = pygame.font.SysFont('aria', 40)
current_path = os.path.dirname(__file__)
os.chdir(current_path)
WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
clock = pygame.time.Clock()
from load import *

def game():
    screen.fill('grey')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(WIDTH, WIDTH + 500)
        self.rect.bottom = HEIGHT - 60
        self.speed = 10
        self.speedx =-3
        self.speedy =-3
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy

class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = block_image
        self.rectt = self.image.get_rect()
        self.rect.topleft = pos

class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = platform_image
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
    def update(self):
        key = pygame.sprite


Player_group = pygame.sprite.Group()
Block_group = pygame.sprite.Group()
Platform_group = pygame.sprite.Group()



platform = Platform()
platform_group.add(platform)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()
    clock.tick(FPS)