import pygame
import os
import random
from settings import *


# set up assets folders
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")



class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder,"p1_jump.png")).convert() # pygame.Surface((50,50))
        self.imagee.set_colorkey(BLACK) #przezroczyste
        self.rect = self.image.get_rect() #obramowka obrazka, sterowanie pozycja
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.y_speed = 5
        
    def update(self):
        self.rect.x += 5
        self.rect.y += self.y_speed
        if self.rect.bottom > HEIGHT -200:
            self.y_speed = -5
        if self.rect.top <200:
            self.y_speed = 5
        if self.rect.left > WIDTH: # jakby "ŁADOWANIE"
            self.rect.right = 0

# initizalize pygame and create window
pygame.init()
pygame.mixer.init() #dzwiek etc
screen= pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Bomberman")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


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



pygame.quit()
