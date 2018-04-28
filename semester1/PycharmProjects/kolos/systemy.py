num = input("Liczba ")
zsys = int(input("z systemu "))
dosys = int(input("do systemu "))

decymal =0
wynik =0
tab= []


for i in range (0, len(num)):
    x = num[i]
    x =int(x)  #!
    p=len(num)-1-i #!
    decymal+= x*zsys**p

print("dziesietnie: ", decymal)

while decymal!=0:
    tab.append(decymal%dosys) #!
    decymal=decymal//dosys

for i in range(0,len(tab)):
    wynik += tab[i]*10**i

print(wynik)
