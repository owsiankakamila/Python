#PROGRAM ANIMACJI POWIEKSZAJACEGO SIE KWADRATU
import os
import time

#wprowadzanie nieparzyste szerokosci i wysokosci
bool=0
while (bool==0):
    szerokosc=int(input("Podaj nieparzystą szerokość: "))
    if ((szerokosc/2) == (szerokosc//2)):
        print("To liczba parzysta!")
    else:
        bool+=1

bool=0
while (bool==0):
    wysokosc=int(input("Podaj nieparzystą wysokość: "))
    if ((wysokosc/2) == (wysokosc//2)):
        print("To liczba parzysta!")
    else:
        bool+=1


#srodek wysokosci i srodek szerokosci
srw = wysokosc//2+1
srs = szerokosc//2+1

#sprawdzanie ktora bedzie mniejsza
if (wysokosc>szerokosc):
    mniejsza=szerokosc
    srodek=srs
else:
    mniejsza=wysokosc
    srodek=srw


krok =-1
maximum= mniejsza - srodek
minimum=0
znak=1
p=0


print("srodek: ",srodek," maximum: ",maximum)

while(p<20):
    
#krok dodatni (powiekszenie) czy krok ujemny (pomniejszenie)
    
    if (krok==maximum):
        znak=-1
    elif(krok==minimum):
        znak=1
        
    krok= krok+znak
      
    
#znalezienie obramowki gorna,dolna,lewa,prawa
    
    if (krok==0):
        gwys,dwys,lszer,pszer= 0,0,0,0
    else:
        gwys = srw - krok
        dwys = srw + krok
        lszer = srs - krok
        pszer = srs + krok
        
        
    #wprowadzam wysokosc
    for w in range (1,wysokosc+1):
        #SRODEK KWADRATU
        if (w==srw):
            for s in range (1,szerokosc + 1):
                if (s==srs) or (s==lszer) or (s==pszer):
                    print("X", end=" ")
                else:
                    print("o", end=" ")
                    
        #WNETRZE KWADRATU
        elif ((w<dwys) and (w>gwys)):
           
            for s in range (1,szerokosc + 1):
                if (lszer==s) or (pszer==s):
                    print("X", end=" ")
                else:
                    print("o", end=" ")
                
        #OBRAMOWKA KWADRATU
        elif (w==dwys) or (w==gwys):
            for s in range (1,szerokosc +1):
                if (s>=lszer) and (s<=pszer):
                    print ("X", end=" ")
                else:
                    print("o", end=" ")
                    
        #POZOSTALE
        
        else:
            for s in range (1,szerokosc +1):
                print ("o",end =" ")
                
        print("")
    time.sleep(0.3)
    os.system('clear')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    