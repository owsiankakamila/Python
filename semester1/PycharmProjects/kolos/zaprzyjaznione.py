zakres =10000

def sumaDzielnikow(liczba):
    suma=0
    for i in range (1,liczba//2 +1):
        if liczba % i ==0:
            suma += i

    return suma

print ("Liczby zaprzyjaznione: ")
for liczba in range (3,zakres+1):
    dzielnikiLiczby =0
    dzielnikiLiczby = sumaDzielnikow(liczba)
    dzielnikiSumy = sumaDzielnikow(dzielnikiLiczby)
    if liczba ==dzielnikiSumy and liczba !=dzielnikiLiczby:
        print(liczba, "i", dzielnikiLiczby )
