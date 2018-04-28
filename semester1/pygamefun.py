import pygame , sys
import Character from character


class Game (object):
    
    def __init__ (self):
        # Config
        self.tps_max = 100.0
        
        # Inicialization
        pygame.init()
        self.screen = pygame.display.set_mode((1280,720))
     
        self.tps_clock = pygame.time.Clock()
        self.tps_delta = 0.0

        self.player =  Character(self)

        while True:
            #Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    sys.exit(0)

            # Ticking:
            self.tps_delta += self.tps_clock.tick()/1000.0 # w sekundach 
            while self.tps_delta > 1/self.tps_max: # to w srodku wykonuje sie gdy minie 1/max_tps
                self.tps_delta -= 1/self.tps_max
                self.tick() #wywolanie tej funkcji nizej

            # Drawing:
            self.screen.fill((0,0,0))
            self.draw()    
            pygame.display.flip()

    def tick(self):
        self.player,tick():
        # Checking inputs:
        keys = pygame.key.get_pressed()

    def draw(self):
        self.player.draw()



if __name__=="__main__": #sprawdza czy uruchomiony bezposrednio czy zimportowany(?)
    Game()


