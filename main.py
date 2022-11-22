import pygame
import random

# setup variables
pygame.init()
screen = pygame.display.set_mode((810, 600))
screen.fill("black")
clock = pygame.time.Clock()
walls = []
font = pygame.font.SysFont("Comic Sans MS", 25)
tileset = []

for x in range(0, 12):
    for y in range(0, 16):
        tileset.insert(x, [x * 50, y * 50])
tileset.sort()
print(tileset)


# classes
class Player:
    def __init__(self):
        self.rect_coll = None
        self.icon = pygame.image.load("player.png")
        self.rect = self.icon.get_rect()
        self.x = 10
        self.y = 10
        self.x_speed = 0
        self.y_speed = 0
        self.hp = 100

    def checkMove(self):
        key_press = pygame.key.get_pressed()
        if key_press[pygame.K_LEFT]:
            self.x_speed = -2
        if key_press[pygame.K_RIGHT]:
            self.x_speed = 2
        if key_press[pygame.K_UP]:
            self.y_speed = 2
        if key_press[pygame.K_DOWN]:
            self.y_speed = -2

        self.rect.midleft = (p.x, p.y)

    def playerMove(self):
        if self.y_speed > 1:
            self.y = self.y - 2
        if self.y_speed < 0:
            self.y = self.y + 2
        if self.x_speed < 0:
            self.x = self.x - 2
        if self.x_speed > 1:
            self.x = self.x + 2
        self.y_speed = 0
        self.x_speed = 0

    def Stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def CheckCollision(self, rect_coll):
        if self.rect.colliderect(rect_coll):
            self.Stop()
            if (rect_coll.left - 30) <= self.x < (rect_coll.right - 30):
                self.x_speed = -2
            if rect_coll.right >= self.x > rect_coll.left:
                self.x_speed = 2
            if self.y <= (rect_coll.top - 14):
                self.y_speed = 2
            if self.y >= (rect_coll.bottom - 14):
                self.y_speed = -2
            else:
                self.x = self.x - 1

        if p.x <= 0:
            self.Stop()
            self.x_speed = 2
        if p.x >= 770:
            self.Stop()
            self.x_speed = -2
        if p.y <= 15:
            self.Stop()
            self.y_speed = -2
        if p.y >= 585:
            self.Stop()
            self.y_speed = 2


class Dungeon:
    def __init__(self, length=0, width=0):
        self.offsetx = None
        self.offsety = None
        self.wall = pygame.image.load("wall.png")
        self.floor = pygame.image.load("floor.png")
        self.length = length
        self.width = width
        self.tiles = []

    def MakeTunnel(self, n, hor):
        self.width = 10
        self.length = 60
        self.offsetx = tileset[n][0]
        self.offsety = tileset[n][1] + 20
        for i in range(2):
            walls.append([self.offsety + self.length * i * hor, self.offsetx, self.width, self.length])

    def MakeBox(self, n, h):
        self.width = 10
        self.length = 50
        self.offsetx = tileset[n][0]
        self.offsety = tileset[n][1]
        for i in range(2):
            walls.append([self.offsety + h * i, self.offsetx, self.width, h])
            walls.append([self.offsety, self.offsetx + h * i, h + 10, self.width])

    def MakeBoxDoorLeft(self, n, h,l,r,t,b):
        self.width = 10
        self.offsetx = tileset[n][0]
        self.offsety = tileset[n][1]
        if l == 1:
            walls.append([self.offsety, self.offsetx, self.width, h/2 - 30])
            walls.append([self.offsety, self.offsetx + h/2 + 30 , self.width, h/2 - 30])

        else:
            walls.append([self.offsety, self.offsetx, self.width, h])
        if r == 1:
            walls.append([self.offsety + h, self.offsetx, self.width, h/2 - 30])
            walls.append([self.offsety + h, self.offsetx + h/2 + 30 , self.width, h/2 - 30])

        else:
            walls.append([self.offsety + h, self.offsetx, self.width, h])
        if b == 1:
            walls.append([self.offsety, self.offsetx + h, (h + 10)/2 -30, self.width])
            walls.append([self.offsety + h/2 + 30 + 5, self.offsetx + h, (h + 10) / 2 - 30, self.width])
        else:
            walls.append([self.offsety, self.offsetx + h, h + 10, self.width])
        if t == 1:
            walls.append([self.offsety, self.offsetx, (h + 10)/2 -30, self.width])
            walls.append([self.offsety + h/2 + 30 + 5, self.offsetx, (h + 10) / 2 - 30, self.width])
        else:
            walls.append([self.offsety, self.offsetx, h + 10, self.width])
def Draw():
    for i in walls:
        z = pygame.draw.rect(screen, (255, 255, 255), (i[0], i[1], i[2], i[3]))
        p.CheckCollision(z)


d = Dungeon()
p = Player()
Player()

d.MakeTunnel(7+32,1)
d.MakeBoxDoorLeft(7,100,0,1,0,1)
d.MakeBoxDoorLeft(9,100,1,1,0,1)
d.MakeBoxDoorLeft(7+32+16,100,0,0,1,1)
# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill("black")
    p.checkMove()
    Draw()
    p.playerMove()
    text = font.render((str(p.x)), False, (255, 255, 0))
    text1 = font.render((str(p.y)), False, (255, 255, 0))
    text2 = font.render((str(int(clock.get_fps()))), False, (255, 255, 0))
    screen.blit(text, (0, 0))
    screen.blit(text1, (50, 0))
    screen.blit(text2, (100, 0))
    screen.blit(p.icon, p.rect)
    pygame.display.flip()
    clock.tick(60)
