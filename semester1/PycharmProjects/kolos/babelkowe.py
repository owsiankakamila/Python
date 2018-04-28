import random

rozmiar = 10
tablica = []

random.seed()

for i in range (0,rozmiar):
    losowana= random.randrange(100)
    tablica.append(losowana)

print(tablica)
flag =True
for i in range(0,rozmiar):
    if flag == False: break
    flag =False
    for j in range (0,rozmiar):
        if (j+1 <rozmiar) and tablica[j] > tablica[j+1]:
            tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
            flag = True

print(tablica)



