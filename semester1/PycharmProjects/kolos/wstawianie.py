import random
rozmiar = 10
tablica = []

random.seed()
for i in range (0,rozmiar):
    losowana = random.randrange(100)
    tablica.append(losowana)

print(tablica)

for i in range (1,rozmiar):
    pozycja = i
    for j in range (i-1,-1,-1):
        if tablica[pozycja] < tablica[j]:
            tablica[pozycja], tablica[j] = tablica[j], tablica[pozycja]
            pozycja = j
        else:
            break #nie ma sensu dalej sprawdzac

print (tablica)
