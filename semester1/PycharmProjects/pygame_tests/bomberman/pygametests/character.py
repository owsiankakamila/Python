import pygame
from pygame.math import Vector2


class Rocket(object):
    def __init__(self,game): #dlaczego tu game -  bo Character(game)
        self.game = game  #GAme  w  inicie przekazane do Character -> self.player= Character(self) przez self
        self.speed = 4.0 #cos za wolno?? WHY
        self.gravity = 0.5

        size = self.game.screen.get_size()

        self.pos = Vector2(size[0]/2,size[1]/2) # [1] pierwszye lement
        self.vel = Vector2(0,0) #szybkosc
        self.acc = Vector2(0,0) #przyspieszenie
    def add_force(self, force):
        self.acc += force #force to ten wektor dodany w tick


    def tick(self):
        # Input
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]:
            self.add_force (Vector2(0,-self.speed))
        if pressed[pygame.K_s]:
            self.add_force (Vector2(0,self.speed))
        if pressed[pygame.K_a]:
            self.add_force (Vector2(-self.speed,0))
        if pressed[pygame.K_d]:
            self.add_force (Vector2(self.speed,0))


        # Physics
        self.vel *=0.9  #opor powietrza bo predkosc staje sie podana czescia
        self.vel = Vector2(0,self.gravity) #na filmiku -?????????

        self.vel += self.acc
        self.pos += self.vel
        self.acc *= 0 #zeruje obie wart

    def draw(self):
        # Base triangle
        points = [Vector2(0,-10),Vector2(5,5),Vector2(-5,5)]
        
        # Rotate points
        angle = self.vel.angle_to(Vector2(0,1)) # nagle between vel and horizontal line
        points = [p.rotate(angle) for p in points]

        # Fix y axis
        points = [Vector2(p.x,p.y*-1) for p in points]

        
        # Add current position and size *2
        points = [Vector2(self.pos +p*2) for p in points]
        
        # Draw triangle
        pygame.draw.polygon(self.game.screen,(0,100,255),points)


