ile = 50
tablica= []

for i in range (0,ile+1):
    tablica.append(1)

tablica[0]=0
tablica[1]=0

for i in range (2, ile+1):
    j=0
    j=2*i
    while j<=ile:
        tablica[j] = 0
        j+=i

for x in range(0,ile+1):
    if tablica[x]==1:
        print(x)