import pygame
import random
import os
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
lvl = 0
map_list = [
    ["1", "2", "x", "1", "2", "x", "1", "2", "x", "1", "2", "x"],
    ["2", "x", "1", "2", "x", "1", "2", "x", "1", "2", "x", "1"],
    ["x", "1", "2", "x", "1", "2", "x", "1", "2", "x", "1", "2"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
]
map_list_2 = [
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
    ["2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2", "2"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x", "x"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0 "],
]
map_list_3 = [
    ["0", "x", "1", "2", "0", "x", "1", "2", "0", "1", "2", "0"],
    ["0", "x", "1", "2", "0", "x", "1", "2", "0", "1", "2", "0"],
    ["0", "x", "1", "2", "0", "x", "1", "2", "0", "1", "0", "0"],
    ["0", "x", "1", "2", "0", "x", "1", "2", "0", "1", "0", "0"],
    ["0", "x", "1", "2", "0", "x", "1", "2", "0", "1", "0", "0"],
]
map_list_4 = [
    ["2", "2", "2", "2", "0", "2", "2", "0", "2", "2", "2", "2"],
    ["0", "0", "0", "0", "0", "1", "1", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "x", "x", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "2", "2", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
]
map_list_5 = [
    ["1", "0", "2", "x", "1", "0", "x", "2", "1", "0", "x", "2"],
    ["1", "0", "x", "2", "1", "0", "2", "x", "1", "0", "2", "x"],
    ["1", "0", "2", "x", "1", "0", "x", "2", "1", "0", "x", "1"],
    ["1", "0", "x", "2", "1", "0", "2", "x", "1", "0", "1", "x"],
    ["1", "0", "2", "x", "1", "0", "x", "2", "1", "0", "x", "1"],
]
def drawmaps(maps):
    pos = [0, 0]
    for i in range (0, len(maps)):
        for j in range(len(maps[i])):
            pos[0] = 50 * j
            pos[1] = 50 * i
            if maps[i][j] == "x":
                block = Block(pos)
                Block_group.add(block)
            if maps[i][j] == "1":
                block = Block_1(pos)
                Block1_group.add(block)
            if maps[i][j] == "2":
                block = Block_2(pos)
                Block2_group.add(block)
from load import *

def game():
    screen.fill('grey')
    ball_group.update()
    ball_group.draw(screen)
    Platform_group.update()
    Platform_group.draw(screen)
    Block_group.update()
    Block_group.draw(screen)
    Block1_group.update()
    Block1_group.draw(screen)
    Block2_group.update()
    Block2_group.draw(screen)
    pygame.display.update()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ball_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH - 50)
        self.rect.bottom = HEIGHT - 60
        if lvl == 0:
            self.speedx =5
            self.speedy =5
        if lvl == 1:
            self.speedx =8
            self.speedy =8
        if lvl == 2:
            self.speedx =11
            self.speedy =11
        if lvl == 3:
            self.speedx = 14
            self.speedy = 14
        if lvl == 4:
            self.speedx = 15
            self.speedy = 15

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.left <=0 or self.rect.right >= WIDTH:
            self.speedx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speedy *= -1
        if pygame.sprite.spritecollide(self, Block_group, True):
            self.speedx *= -1
            self.speedy *= -1
        if pygame.sprite.spritecollide(self, Platform_group, False):
            self.speedx *= -1
            self.speedy *= -1
        if pygame.sprite.spritecollide(self, Block1_group, False):
            block = pygame.sprite.spritecollide(self, Block1_group, False)[0]
            block.hp -= 1
            self.speedx *= -1
            self.speedy *= -1


class Block(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = block_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Block_1(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = block2_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hp = 2
    def update(self):


        if self.hp <= 0:
            self.kill()


class Block_2(pygame.sprite.Sprite):
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = block3_image
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hp = 3




class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = platform_image
        self.rect = self.image.get_rect()
        self.rect.bottom = 600
        self.speed = 10
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed

        if key[pygame.K_a]:
            self.rect.x -= self.speed

        if self.rect.left > 600:
            self.rectleft = 600

        if self.rect.right > 600:
            self.rect.right = 600



ball_group = pygame.sprite.Group()
Block_group = pygame.sprite.Group()
Block1_group = pygame.sprite.Group()
Block2_group = pygame.sprite.Group()
Platform_group = pygame.sprite.Group()



platform = Platform()

Platform_group.add(platform)
drawmaps(map_list)
ball = Ball()
ball_group.add(ball)
maps = [map_list, map_list_2, map_list_3, map_list_4, map_list_5]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    game()
    if len(Block_group) == 12:
        lvl += 1
        ball.rect.center = 300, 400
        drawmaps(maps[lvl])

    clock.tick(FPS)