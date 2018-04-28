import random
rozmiar = 10

tablica= []

for x in range(0,rozmiar):
    random.seed()
    losowana = random.randrange(100)
    tablica.append(losowana)
    print(tablica[x], end=" ")

tab=tablica [:]
print(" ")


poz_najmn=0

for i in range (0,rozmiar):
    najmn = tab[i]
    poz_najmn = i
    for j in range (i, rozmiar):
        if tab[j] < najmn:
            najmn = tab[j]
            poz_najmn = j
    tab[i], tab[poz_najmn] = tab[poz_najmn], tab[i]


for x in range(0,rozmiar):
    print(tab[x], end=" ")