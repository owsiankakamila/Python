import pygame
import os
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,40))# pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert() # pygame.Surface((50,50))
        self.image.fill(GREEN)
        self.image.set_colorkey(BLACK) #przezroczyste
        self.rect = self.image.get_rect() #obramowka obrazka, sterowanie pozycja
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
     
    def update(self):
        self.speedx = 0
        keystates = pygame.key.get_pressed()
        if keystates[pygame.K_a]:
            self.speedx= -5
        if keystates[pygame.K_d]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left <0:
            self.rect.left = 0


class Mob (pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange (-100,-40)
        self.speedy = random.randrange(1,8)
        self.speedx = random.randrange(-3,3)
    def update(self):
        self.rect.x +=self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT +10 or self.rect.left < -20  or self.rect.right > WIDTH:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange (-100,-40)
            self.speedy = random.randrange(1,8)

   


# initizalize pygame and create window
pygame.init()
pygame.mixer.init() #dzwiek etc
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range (8):
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type  == pygame.QUIT:
            running = False


    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after drawing everything, flip display
    pygame.display.flip()



