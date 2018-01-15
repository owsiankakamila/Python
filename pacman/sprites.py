import pygame as pg
from settings import *
from random import randint


class Player(pg.sprite.Sprite):
    life = 3
    score = 0
    coins =0
    def __init__(self, game, pos_x, pos_y):

        self.groups = game.all_sprites, game.players
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # image settings
        self.walking= False
        self.last_update=0
        self.current_frame =0


        self.walk_frames_r = (game.player_img, game.player2_img)
        self.walk_frames_l = (game.player_img, pg.transform.flip(game.player2_img, True, False))
        self.walk_frames_u = (game.player_img, pg.transform.flip(game.player3_img, False, True))
        self.walk_frames_d = (game.player_img, game.player3_img)

        self.image = self.walk_frames_l[0]
        self.rect = self.image.get_rect()
        self.radius = 8
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        # position settings
        self.rect.top = pos_x * TILESIZE
        self.rect.left = pos_y * TILESIZE
        self.old_pos_x = self.rect.top
        self.old_pos_y = self.rect.left

        # movement settings
        self.next_move = (0, 0)
        self.current_move = (0, 0)

    def change_direction(self,x, y):
        self.next_move = (x, y)

    def update(self):


        self.old_pos_x = self.rect.top
        self.old_pos_y = self.rect.left

        ## NONE KEY PRESSED
        if self.next_move == (0,0):

            # change position
            self.rect.top += self.current_move[0]
            self.rect.left += self.current_move[1]

            # IF HIT WALL
            if pg.sprite.spritecollideany(self, self.game.walls):

                # return to previous position
                self.rect.top = self.old_pos_x
                self.rect.left = self.old_pos_y

        ## KEYDOWN EVENT DETECTED
        else:
            # change position
            self.rect.top  += self.next_move[0]
            self.rect.left += self.next_move[1]


            # IF HIT WALL
            if pg.sprite.spritecollideany(self, self.game.walls):

                # return to previous position
                self.rect.top = self.old_pos_x
                self.rect.left = self.old_pos_y


                # use previous speed
                self.rect.top += self.current_move[0]
                self.rect.left += self.current_move[1]

                # HIT WALL
                if pg.sprite.spritecollideany(self, self.game.walls):
                    x=1
                    # return to previous position
                    self.rect.top = self.old_pos_x
                    self.rect.left = self.old_pos_y


            # IF NOT HIT WALL
            else:
                # replace current with new
                self.current_move = self.next_move
                self.next_move = (0, 0)

        ## IF WENT OUTSIDE THE MAP -> GO from the other side

        if self.rect.left > WIDTH:
            self.rect.top = self.game.map_tunel_x[self.game.level]
            self.rect.left = 0

        if self.rect.right < 0:
            self.rect.top = self.game.map_tunel_x[self.game.level]
            self.rect.left = WIDTH


        ## SCORE /EATING COINS
        hits = pg.sprite.spritecollide(self, self.game.coins, True, pg.sprite.collide_circle)
        if hits:
            self.score +=10
            self.coins+=1
        hits2 = pg.sprite.spritecollide(self, self.game.supercoins, True, pg.sprite.collide_circle)
        if hits2:
            self.score += 10
            self.coins += 1
            self.game.frightened_mode =True
        ## FRIGHTEND
        if self.game.frightened_mode == False:
            self.walk_frames_r = (self.game.player_img, self.game.player2_img)
            self.walk_frames_l = (self.game.player_img, pg.transform.flip(self.game.player2_img, True, False))
            self.walk_frames_u = (self.game.player_img, pg.transform.flip(self.game.player3_img, False, True))
            self.walk_frames_d = (self.game.player_img, self.game.player3_img)

        else:
            self.walk_frames_r = (self.game.fright_img, self.game.fright2_img)
            self.walk_frames_l = (self.game.fright_img, pg.transform.flip(self.game.fright2_img, True, False))
            self.walk_frames_u = (self.game.fright_img, pg.transform.flip(self.game.fright3_img, False, True))
            self.walk_frames_d = (self.game.fright_img, self.game.fright3_img)

        ## EATING ANIMATION
        now = pg.time.get_ticks()
        if self.current_move != (0, 0):
            self.walking = True

        else:
            self.walking = False

        if self.walking :
            if now - self.last_update > 300:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frames_l)

            if self.current_move[0] == -PLAYER_SPEED:
                 self.image = self.walk_frames_u[self.current_frame]
            elif self.current_move[0] == PLAYER_SPEED:
                self.image = self.walk_frames_d[self.current_frame]
            elif self.current_move[1] == -PLAYER_SPEED:
                self.image = self.walk_frames_l[self.current_frame]
            elif self.current_move[1] == PLAYER_SPEED:
                self.image = self.walk_frames_r[self.current_frame]





class Ghost(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.ghosts
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        #self.ghost_time = 2


        # image settings
        self.image= game.blinky_img
        transColor = self.image.get_at((12, 12))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.radius = 8
        #pg.draw.circle(self.image, BLUE, self.rect.center, self.radius)

        #movement settings
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
        self.current_move = [-GHOST_SPEED, 0]
        self.next_move = [0, 0]



    def random_dir(self):
        x=randint(0,1)
        if x == 0:
            return -1
        return 1

    def random_move(self,current_dir):
        if current_dir==0:
            return self.random_dir() * GHOST_SPEED
        else:
            return 0

    def update(self):
        self.old_pos_x = self.rect.top
        self.old_pos_y = self.rect.left

        '''NOTE:
            current_move is direction which ghost was currently moving
            next_move is direction perpendicular to current_move'''

        #self.ghost_time += 1 / 60
        #print(self.ghost_time)
        #if self.ghost_time >2:

        # randomly choose next move (co jakis czas?):

        x = self.random_move(self.current_move[0])
        y = self.random_move(self.current_move[1])
        self.next_move= [x,y]

            #self.ghost_time =0

        # change position
        self.rect.top += self.next_move[0]
        self.rect.left += self.next_move[1]

        # IF HIT WALL
        if pg.sprite.spritecollideany(self, self.game.walls):

            # return to previous position
            self.rect.top = self.old_pos_x
            self.rect.left = self.old_pos_y

            # use previous speed
            self.rect.top += self.current_move[0]
            self.rect.left += self.current_move[1]

            # HIT WALL
            if pg.sprite.spritecollideany(self, self.game.walls):
                # return to previous position
                self.rect.top = self.old_pos_x
                self.rect.left = self.old_pos_y

                # CHOSE THE LAST POSSIBLE DIRECTION (except coming back)

                # "reverse" next_move direction

                self.next_move[0] = -self.next_move[0]
                self.next_move[1] = -self.next_move[1]

                # change position
                self.rect.top += self.next_move[0]
                self.rect.left += self.next_move[1]

                # HIT WALL
                if pg.sprite.spritecollideany(self, self.game.walls):
                    # return to previous position
                    self.rect.top = self.old_pos_x
                    self.rect.left = self.old_pos_y

                    # NOW YOU CAN ONLY COME BACK

                    # "reverse" current_move direction
                    self.current_move[0] = -self.current_move[0]
                    self.current_move[1] = -self.current_move[1]

                    # change position


            # IF NOT HIT WALL
        else:
            # replace current with new
            self.current_move = self.next_move
            #self.next_move = (0, 0) do not because must change direction properly (no coming back)

        ## IF WENT OUTSIDE THE MAP -> GO from the other side

        if self.rect.left > WIDTH:
            self.rect.left = 0
            self.rect.top = self.game.map_tunel_x[self.game.level]
        if self.rect.right < 0:
            self.rect.left = WIDTH
            self.rect.top = self.game.map_tunel_x[self.game.level]







class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # wall type:
        if self.game.level==0:
            self.image= game.wall0_img
        if self.game.level==1:
            self.image= game.wall1_img
        if self.game.level==2:
            self.image= game.wall2_img
        if self.game.level==3:
            self.image= game.wall3_img

        # image settings
        transColor = self.image.get_at((12, 12))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()

        # movement settings
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


class Coin(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.coins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # image settings
        self.image = game.coin_img
        transColor = self.image.get_at((0, 0))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.radius = 1
        #pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        # position settings
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class SuperCoin(pg.sprite.Sprite):
    def __init__(self, game, x, y):

        self.groups = game.all_sprites, game.supercoins
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        # image settings
        self.image = pg.Surface((24,24))
        self.image.fill(BGCOLOR)
        self.rect = self.image.get_rect()
        self.radius = 7
        pg.draw.circle(self.image, RED, self.rect.center, self.radius)

        # position settings
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE


'''
    def changed_direction(self,x,y):
        self.speed_x = x
        self.speed_y = y

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def updated(self):
        self.old_pos_x = self.rect.top
        self.old_pos_y = self.rect.left
        self.rect.top += self.speed_x
        self.rect.left += self.speed_y
        # if x if y
        if pg.sprite.spritecollideany(self, self.game.walls):
            self.rect.top = self.old_pos_x
            self.rect.left = self.old_pos_y
        # check if dead
        
        
            


'''
