import random
import os
import time

szerokosc = 11
wysokosc = 7

losy = []
seria =0

while seria<10:
    
    numer = int(random.randrange(szerokosc))
    losy.append(numer)
    miejsce = len(losy) -1
    
    for w in range (0,wysokosc):
        
        for s in range(0,szerokosc):
            if (miejsce>=0) and(s==losy[miejsce])  :
                print("x",end=" ")
            else:
                print("o",end=" ")
        miejsce-=1
        print("")
    print("")
    time.sleep(0.3)
    os.system('clear')
        