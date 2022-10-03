import pygame
import sys

# setup variables
pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill("black")
clock = pygame.time.Clock()


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
            self.x = self.x - 1
        if key_press[pygame.K_RIGHT]:
            self.x = self.x + 1
        if key_press[pygame.K_UP]:
            self.y = self.y - 1
        if key_press[pygame.K_DOWN]:
            self.y = self.y + 1

        self.rect.midleft = (p.x, p.y)


p = Player()
Player()

# main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    p.checkMove()
    screen.fill("black")
    screen.blit(p.icon, p.rect)
    pygame.display.flip()
    clock.tick(120)
