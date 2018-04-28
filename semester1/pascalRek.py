# TROJKAT PASCALA, REKURENCJA

def pascal(wiersz,numer):
    if numer==1:
        return 1
    if (wiersz==numer):
        return 1
    #z poprzedniego wiersza 
    if wiersz>2:
        return pascal(wiersz-1,numer-1) + pascal(wiersz-1,numer)



#wybieram ile wierszy ma miec trojkat
w=int(input("Podaj liczbe wierszy: "))

#rysowanie wierszy
for i in range(1,w+1):
    #rysowanie pustych miejsc
    for j in range (0,w-i):
        print(" ",end="")
    #rysowanie numerow
    for k in range (1,i+1):
        print(pascal(i,k), end=" ")
    print("") #enter po koncu wiersza
      