
"""
SZYFROWANIE Z KLUCZEM


#gdy alfabet jest dluzszy od klucza - metoda powtarzania
        ileRazy = miejsceAlf/wielkoscKey
        miejsceKey = miejsceAlf -(ileRazy*wielkoscKey)
"""
def przygotowanie(tekst):
    tekst =tekst.replace(" ","")
    tekst= tekst.lower()
    return tekst

def stworzKlucz(klucz): 
    #usuwa powtorzenia z klucza i dodaje niepowtaarzajace sie litery alfabetu
    klucz= klucz + "abdefghijklmnopqrstuvwxyz"
    klucz1 = []
    for i in klucz:
        if i not in klucz1:
            klucz1.append(i)
    klucz1="".join(klucz1)
    return klucz1

def zKluczem(tekst,klucz):
    tekst2= []
    wielkoscTxt = len(tekst)  
    
    for i in range (0,wielkoscTxt):
        miejsceAlf = ord(tekst[i])-97 #miejsce w alfabecie i-litery w tekscie
        tekst2.append(klucz[miejsceAlf])
        
    tekst2="".join(tekst2)
    return tekst2

def deZKluczem(tekst,klucz):
    tekst2= []
    wielkoscTxt = len(tekst)
    
    for i in range (0,wielkoscTxt):
        ordAlf =klucz.index(tekst[i]) +97
        tekst2.append(chr(ordAlf))
    
    tekst2="".join(tekst2)
    return tekst2
    
    

print("1. Chce zaszyfrowac tekst")
print("2. Chce odszyfrowac tekst")
decyzja=int(input())

if (decyzja==1):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    
    klucz =input("Klucz: ")
    klucz=przygotowanie(klucz)
    klucz=stworzKlucz(klucz)
    
    zaszyfrowany = zKluczem(tekst1,klucz)
    print("Zaszyfrowany tekst: ",zaszyfrowany)
    
    
elif (decyzja ==2):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    
    klucz =input("Klucz: ")
    klucz=przygotowanie(klucz)
    klucz=stworzKlucz(klucz)
    
    odszyfrowany = deZKluczem(tekst1,klucz)
    print("Odszyfrowany tekst: ",odszyfrowany)