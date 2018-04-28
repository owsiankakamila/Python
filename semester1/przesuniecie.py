def przygotowanie(tekst):
    tekst =tekst.replace(" ","")
    tekst= tekst.lower()
    return tekst

def podstawieniowy(tekst,alfabet):
    alfabet=list(alfabet)
    teskt = list(tekst)
    tekst2= []
    wielkosctxt = len(tekst)
    
    for i in range (0,wielkosctxt):
        odleglosc = ord(tekst[i]) -97
        tekst2.append(alfabet[odleglosc])
        
    tekst2="".join(tekst2)
    return tekst2

def dePodstawieniowy(tekst,alfabet):
    alfabet=list(alfabet)
    teskt = list(tekst)
    tekst2= []
    wielkosctxt = len(tekst)
    
    for i in range (0,wielkosctxt):
        odleglosc =alfabet.index(tekst[i]) +97
        tekst2.append(chr(odleglosc))
        
    tekst2="".join(tekst2)
    return tekst2



print("1. Chce zaszyfrowac tekst")
print("2. Chce odszyfrowac tekst")
decyzja=int(input())

if (decyzja==1):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    nalfabet =input("Nowy alfabet: ")
    zaszyfrowany = podstawieniowy(tekst1,nalfabet)
    print("Zaszyfrowany tekst: ",zaszyfrowany)
    
    
elif (decyzja ==2):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    nalfabet =input("Nowy alfabet: ")
    odszyfrowany = dePodstawieniowy(tekst1,nalfabet)
    print("Odszyfrowany tekst: ",odszyfrowany)


