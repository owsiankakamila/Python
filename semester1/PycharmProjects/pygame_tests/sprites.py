import pygame as pg
from settings import *
import bomb

class Player(pg.sprite.Sprite):
    live = 1
    speed = 1
    power = 1
    avail_bombs = 1
    maxBombs = 1
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()import pygame as pg
from settings import *
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0): #events -> move -> collide ->..->  update
        if not self.collide_with_walls(dx, dy):
            self.x += dx
            self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE
        # check if dead


    def dropBomb(self):
        if self.avail_bombs >0:
            self.avail_bombs-=1
            bomb.Bomb(self.game, self.rect.x,self.rect.y)

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
