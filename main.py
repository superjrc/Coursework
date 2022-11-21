import pygame
import sys
import random
import numpy
import time

# setup variables
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill("black")
clock = pygame.time.Clock()
walls = []
font = pygame.font.SysFont("Comic Sans MS", 25)

# classes
class Player:
    def __init__(self, x=10, y=10, hp=100, xspeed=0, yspeed=0):
        self.rectcoll = None
        self.icon = pygame.image.load("player.png")
        self.rect = self.icon.get_rect()
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.hp = hp

    def checkMove(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.xspeed = -2
        if key_press[pygame.K_RIGHT]:
            self.xspeed = 2
        if key_press[pygame.K_UP]:
            self.yspeed = 2
        if key_press[pygame.K_DOWN]:
            self.yspeed = -2



        self.rect.midleft = (p.x, p.y)

    def playerMove(self):
        if self.yspeed > 1:
            self.y = self.y - 2
        if self.yspeed < 0:
            self.y = self.y + 2
        if self.xspeed < 0:
            self.x = self.x - 2
        if self.xspeed > 1:
            self.x = self.x + 2
        self.yspeed = 0
        self.xspeed = 0

    def CheckCollision(self,rectcoll):
        if self.rect.colliderect(rectcoll):
            print(rectcoll.top - 16)
            self.xspeed = self.xspeed * 0
            self.yspeed = self.yspeed * 0
            if self.x >= (rectcoll.left - 30) and self.x < (rectcoll.right - 30):
                self.x = self.x - 2
            elif self.x <= (rectcoll.right) and self.x > rectcoll.left:
                self.x = self.x + 2
            if self.y <= (rectcoll.top - 14):
                self.y = self.y - 5



class Dungeon:
    def __init__(self, length=0, width=0):
        self.wall = pygame.image.load("wall.png")
        self.floor = pygame.image.load("floor.png")
        self.length = length
        self.width = width
        self.tiles = []



    def MakeWall(self):
        self.width = random.randint(100, 200)
        self.length = random.randint(100, 200)
        self.offsetx = random.randint(100, 200)
        self.offsety = random.randint(100, 200)
        walls.append([self.offsety, self.offsetx, self.width, self.length])



    def Draw1(self):

        for i in walls:
            z = pygame.draw.rect(screen, (255, 255, 255), (i[2], i[3], i[0], i[1]))
            p.CheckCollision(z)



d = Dungeon()
p = Player()
Player()

d.MakeWall()
d.MakeWall()
# d.GenRoom()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill("black")
    p.checkMove()
    d.Draw1()
    p.playerMove()
    text = font.render((str(p.y)), False, (255, 255, 0))
    screen.blit(text, (0,0))


    # d.GenRoom()
    # screen.blit(walls, (0,10))
    screen.blit(p.icon, p.rect)
    pygame.display.flip()
    clock.tick(60)
