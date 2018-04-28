def przygotowanie(tekst):
    tekst =tekst.replace(" ","")
    tekst= tekst.lower()
    return tekst

def cezar(tekst,przesuniecie):
    wielkosc= len(tekst)
    tekst=list(tekst)
    for i in range(0,wielkosc):
        if ((ord(tekst[i]) + przesuniecie)>121):
            nowaInt =ord(tekst[i]) + przesuniecie -26
            tekst[i] =chr(nowaInt)
        else:
            nowaInt =ord(tekst[i]) + przesuniecie
            tekst[i] = chr(nowaInt)
    tekst="".join(tekst)
    return tekst

def deCezar(tekst, przesuniecie):
    wielkosc = len(tekst)
    tekst=list(tekst)
    for i in range(0,wielkosc):
        if ((ord(tekst[i]) - przesuniecie)<97):
            nowaInt =ord(tekst[i]) - przesuniecie +26
            tekst[i] =chr(nowaInt)
        else:
            nowaInt =ord(tekst[i]) - przesuniecie
            tekst[i] = chr(nowaInt)
    tekst="".join(tekst)
    return tekst

print("1. Chce zaszyfrowac tekst")
print("2. Chce odszyfrowac tekst")
decyzja=int(input())

if (decyzja==1):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    przesun =int(input("Szyfr cezara o: "))
    zaszyfrowany = cezar(tekst1,przesun)
    print("Zaszyfrowany tekst: ",zaszyfrowany)
elif (decyzja ==2):
    tekst1=input("Tekst: ")
    tekst1=przygotowanie(tekst1)
    przesun =int(input("Szyfr cezara o: "))
    odszyfrowany = deCezar(tekst1,przesun)
    print("Odszyfrowany tekst: ",odszyfrowany)


