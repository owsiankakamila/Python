import pygame as pg
import sys
from os import path
from settings import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.what_time = self.clock.tick()
        self.running = True

        self.count_time=0
        self.count_frtime=0
        self.frightened_mode=False

        self.level_number=1
        self.level=0
        self.level_maps=['map1.txt', 'map2.txt', 'map3.txt', 'map4.txt']
        self.level_coins=[MAP1_COINS, MAP2_COINS, MAP3_COINS, MAP4_COINS]

        self.map_tunel_x=[MAP1_TUNNEL,MAP2_TUNNEL, MAP3_TUNNEL, MAP4_TUNNEL]


        self.load_data()

    def load_data(self):
        self.game_folder = path.dirname(__file__)
        self.img_folder = path.join(self.game_folder, 'img')

        with open(path.join(self.game_folder, HSCORE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0

        self.player_img = pg.image.load(path.join(self.img_folder, PLAYER_IMG)).convert_alpha()
        self.player2_img = pg.image.load(path.join(self.img_folder, PLAYER2_IMG)).convert_alpha()
        self.player3_img = pg.image.load(path.join(self.img_folder, PLAYER3_IMG)).convert_alpha()

        self.fright_img = pg.image.load(path.join(self.img_folder, FRIGHTEND_IMG)).convert_alpha()
        self.fright2_img = pg.image.load(path.join(self.img_folder, FRIGHTEND2_IMG)).convert_alpha()
        self.fright3_img = pg.image.load(path.join(self.img_folder, FRIGHTEND3_IMG)).convert_alpha()

        self.frightend_img = pg.image.load(path.join(self.img_folder, FRIGHTEND_IMG)).convert_alpha()

        self.wall0_img= pg.image.load(path.join(self.img_folder, WALL0_IMG)).convert_alpha()
        self.wall1_img = pg.image.load(path.join(self.img_folder, WALL1_IMG)).convert_alpha()
        self.wall2_img = pg.image.load(path.join(self.img_folder, WALL2_IMG)).convert_alpha()
        self.wall3_img = pg.image.load(path.join(self.img_folder, WALL3_IMG)).convert_alpha()

        self.coin_img = pg.image.load(path.join(self.img_folder, COIN_IMG)).convert_alpha()
        self.blinky_img = pg.image.load(path.join(self.img_folder, BLINKY_IMG)).convert_alpha()

    def new(self):
        self.stopped = False
        self.paused = False

        # SET GROUPS
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.coins = pg.sprite.Group()
        self.supercoins = pg.sprite.Group()
        self.players = pg.sprite.Group()
        self.ghosts = pg.sprite.Group()

        self.new_map(self.level)


    def new_map(self,level):
        #clear all previous group except pacman?
        for sprite in self.walls:
            if isinstance(sprite, Wall):
                sprite.kill()
        for sprite in self.ghosts:
            if isinstance(sprite, Ghost):
                sprite.kill()

        #self.ghosts(self.screen,self.screen)

        self.map_data = []
        with open(path.join(self.game_folder, self.level_maps[level]), 'rt') as f:
            for line in f:
                self.map_data.append(line)

        # DRAW MAP
        # if lvl =.... pdodielny przez 1 przez 2 przez 3 przezz 4 albo po tablicy leveli
        for row,tiles in enumerate(self.map_data): #nr rzedu, rzad
            for column, tile in enumerate(tiles):        #nr znaku, znak
                if tile == '1':
                    Wall(self, column, row)
                if tile == '.':
                    Coin(self, column, row)
                if tile == 's':
                    SuperCoin(self, column, row)
                if tile == 'P':
                    if self.level_number==1:
                        self.pacman = Player(self, row, column) #na odwrot?
                    else:
                        self.pacman.rect.top = row * TILESIZE
                        self.pacman.rect.left = column * TILESIZE
                if tile == 'b':
                    #self.ghost =
                    Ghost(self, column, row)



    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()

            if not self.paused and not self.stopped:
                self.update()

            if self.stopped:
                self.count_time += 1/60
                if self.count_time >1.5:
                    self.count_time=0
                    self.stopped = False

                    for row, tiles in enumerate(self.map_data):  # nr rzedu, rzad
                        for column, tile in enumerate(tiles):  # nr znaku, znak
                            if tile == 'P':
                                self.pacman.rect.top = row * TILESIZE
                                self.pacman.rect.left = column * TILESIZE
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()



    def update(self):
        # update sprites
        self.all_sprites.update()


        if self.frightened_mode ==False:
            hits_ghost =  pg.sprite.spritecollide(self.pacman, self.ghosts, False, pg.sprite.collide_circle)
            if hits_ghost:
                self.pacman.life -=1
                self.pacman.current_move=(0,0)
                self.stopped =True
        else:
            hits_ghost = pg.sprite.spritecollide(self.pacman, self.ghosts, True, pg.sprite.collide_circle)
            if hits_ghost:
                self.pacman.score+=400


                Ghost(self, 10, 10,)
            self.count_frtime += 1 / 60
            if self.count_frtime > 4:
                self.count_frtime = 0
                self.frightened_mode = False


        if self.pacman.life ==0:
            self.playing=False
            self.running=False

        #jesli nie ma juz coinow to narysuj mape2 jeszzcze raz i dodaj level
        if self.level_coins[self.level] == self.pacman.coins:
            print("teraz")
            self.pacman.coins=0
            self.level_number+=1
            self.level+=1
            if self.level==len(self.level_maps):
                self.level =0
            self.new_map(self.level)







    def draw(self):
        self.screen.fill(BGCOLOR)
        #self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.draw_text(self.screen, str(self.pacman.score), 24, WIDTH-5, 15, "mr")
        self.draw_text(self.screen, str(self.highscore), 24, WIDTH/2, 5)
        self.draw_text(self.screen, str(self.level_number), 24, WIDTH-42, HEIGHT-12, 'mr')
        self.draw_text(self.screen, "LVL", 24, WIDTH - 5, HEIGHT - 12, 'mr')
        for i in range(0,self.pacman.life):
            pg.draw.circle(self.screen, YELLOW, (12+(24*i),HEIGHT-12), 10)
        if self.paused:
            self.draw_text(self.screen,"PAUSED",24,10,12, 'ml')
        if self.frightened_mode:
            self.draw_text(self.screen, "EAT THEM ALL!", 24, 10, 12, 'ml')

        pg.display.flip()

    def draw_text(self,surf, text, size, x, y, allign="mt"):
        font_name = pg.font.match_font('arial')
        font= pg.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        if allign == "mr":
            text_rect.midright = (x,y)
        if allign == "ml":
            text_rect.midleft =(x,y)
        if allign == "mt":
            text_rect.midtop = (x,y)
        surf.blit(text_surface, text_rect)

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))



    def events(self):
        # catch all events here
        for event in pg.event.get():

            if event.type == pg.QUIT: #quit
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE: #quit
                    self.quit()
                if event.key == pg.K_p:
                    self.paused = not self.paused


                # PACMAN MOVEMENT
                if event.key == pg.K_UP:
                    self.pacman.change_direction(-PLAYER_SPEED, 0)
                elif event.key == pg.K_DOWN:
                    self.pacman.change_direction(PLAYER_SPEED, 0)
                elif event.key == pg.K_RIGHT:
                    self.pacman.change_direction(0, PLAYER_SPEED)
                elif event.key == pg.K_LEFT:
                    self.pacman.change_direction(0, -PLAYER_SPEED)


    def show_start_screen(self):
        self.screen.fill(BGCOLOR)
        self.draw_text(self.screen, TITLE, 100, WIDTH / 2, HEIGHT / 4)

        self.draw_text(self.screen, "Arrows to MOVE", 22, WIDTH / 2, HEIGHT / 2)
        self.draw_text(self.screen, "P to PAUSE", 22, WIDTH / 2, HEIGHT / 2 +30)
        self.draw_text(self.screen, "Press a key to play", 22, WIDTH / 2, HEIGHT * 3 / 4)
        self.draw_text(self.screen, "High Score: " + str(self.highscore), 22, WIDTH / 2, 15)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYDOWN:
                    waiting = False
                    if self.running==False:
                        self.running=True
                    if event.key == pg.K_ESCAPE:
                        self.running = False


    def show_over_screen(self):
        if not self.running:

            self.screen.fill(BGCOLOR)
            self.level_number = 1
            self.level = 0
            self.draw_text(self.screen, "GAME", 100, WIDTH / 2, HEIGHT / 4 - 50)
            self.draw_text(self.screen, "OVER", 100, WIDTH / 2, HEIGHT / 4 + 20)
            self.draw_text(self.screen, "Score: " + str(self.pacman.score), 22, WIDTH / 2, HEIGHT / 2)
            self.draw_text(self.screen, "Press a key to play again", 22, WIDTH / 2, HEIGHT * 3 / 4)
            if self.pacman.score > self.highscore:
                self.highscore = self.pacman.score
                self.draw_text(self.screen, "NEW HIGH SCORE!", 22, WIDTH / 2, HEIGHT / 2 + 40)
                with open(path.join(self.game_folder, HSCORE), 'w') as f:
                    f.write(str(self.pacman.score))
            else:
                self.draw_text(self.screen,"High Score: " + str(self.highscore), 22, WIDTH / 2, HEIGHT / 2 + 40)

            pg.display.flip()
            self.wait_for_key()


# create the game object
g = Game()
g.show_start_screen()
while g.running==True:
    g.new()
    g.run()
    g.show_over_screen()