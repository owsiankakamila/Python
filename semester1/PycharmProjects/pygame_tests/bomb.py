import pygame as pg
from settings import *
from sprites import *


class Bomb(pg.sprite.Sprite):

    def __init__(self,game, player_x, player_y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)

        #image
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = player_x
        self.y = player_y


    def update(self):
        self.rect.x = self.x
        self.rect.y = self.y
        #time to explode
        #explosion
        #explosion spreading
        #check passing
        #taking lives
        #