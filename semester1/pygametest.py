'''PYGAME'''
import pygame,sys

#zmienne konfiguracyjne

max_tps = 20.0 #tick per second, maxymalna liczba 

pygame.init()
screen = pygame.display.set_mode((1280,720))
box = pygame.Rect(10,10,50,50)
clock = pygame.time.Clock()
delta = 0.0 #float

while True:
    #Handle events / nie są ciągłe. występuje i nara
    for event in pygame.event.get(): #sprawdza wszystkie zdarzenia ktore wystapily
        if event.type == pygame.QUIT:#jesli typ zdarzenia to quit to wylacz
            sys.exit(0)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            sys.exit(0)
            
    #Ticking
    delta += clock.tick()/1000.0
    while delta > 1/max_tps:
        delta -=1/max_tps
        
        
            
            
        # checking Input czy klawisz wcisniety
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_d]):
            box.x +=1
        if (keys[pygame.K_s]):
            box.y +=1
        if (keys[pygame.K_w]):
            box.y -=1
        if (keys[pygame.K_a]):
            box.x -=1
        
    
    
    #Drawing
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,20,100),box)
    pygame.display.flip()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
