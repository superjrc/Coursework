import pygame
import sys
import random
import numpy

# setup variables
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill("black")
clock = pygame.time.Clock()
walls = []

# classes
class Player:
    def __init__(self, x=10, y=10, hp=100):
        self.icon = pygame.image.load("player.png")
        self.rect = self.icon.get_rect()
        self.x = x
        self.y = y
        self.hp = hp

    def checkMove(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.x = self.x - 2
        if key_press[pygame.K_RIGHT]:
            self.x = self.x + 2
        if key_press[pygame.K_UP]:
            self.y = self.y - 2
        if key_press[pygame.K_DOWN]:
            self.y = self.y + 2

        self.rect.midleft = (p.x, p.y)


class Dungeon:
    def __init__(self, length=0, width=0):
        self.wall = pygame.image.load("wall.png")
        self.floor = pygame.image.load("floor.png")
        self.length = length
        self.width = width
        self.tiles = []

    def MakeWallImg(self):
        self.width = random.randint(200, 400)
        self.length = random.randint(200, 400)
        for x in range(0, self.width):
            if self.width > -45:
                self.tiles.append(self.width)
                self.width = self.width - 45

    def MakeWall(self):
        self.width = random.randint(100,200)
        self.length = random.randint(100,200)
        self.offsetx = random.randint(100,200)
        self.offsety = random.randint(100,200)
        walls.append(pygame.Rect((self.offsety, self.offsetx),(self.width, self.length)))



    def ShowWall(self, walltype, offsetx, offsety):
        if walltype == 0:
            for y in self.tiles:
                screen.blit(self.wall, (offsetx, y + offsety))
        elif walltype == 1:
            for y in self.tiles:
                screen.blit(self.wall, (y + offsetx, offsety))

    def GenRoom(self):
        for x in range(random.randint(10, 20)):
            self.MakeWall()
            self.ShowWall(random.randint(0, 1), random.randint(0, 400), random.randint(0, 400))

    def Draw1(self):

        for i in walls:
            pygame.draw.rect(screen, (255,255,255), (100, 100 ,100, 100))



d = Dungeon()
p = Player()
Player()
d.MakeWall()
d.Draw1()
#d.GenRoom()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    p.checkMove()

    #screen.fill("black")
    #d.GenRoom()
    #screen.blit(walls, (0,10))
    screen.blit(p.icon, p.rect)
    pygame.display.flip()
    clock.tick(60)
