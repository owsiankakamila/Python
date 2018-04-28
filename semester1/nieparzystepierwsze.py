#ELIMINACJA POWTARZAJĄCYH SIĘ NIEPARZYCIE LICZB PIERWSZYCH

'''FUNKCJA CZY LICZBA PIERWSZA'''
def isPrime (number):
    for i in range(3, number):
        if number%i == 0:
            return 0
        return 1

def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]


liczby = input("Wprowadz liczby:") # wprowadz jako oddzielone spacjami

liczby= "".join(liczby).split(' ') #do listy, przerywnikiem spacja
liczby = list(map(int, liczby))  # char to int
print(liczby)

print(liczby)

for i in range(0,len(liczby)-1): #sprawdzam kazda
    if (isPrime(liczby[i])==1):  #jesli jest l pierwsza
        if(((liczby.count(liczby[i]))%2)!=0): #jesli nieparzysta liczba powtorzen
            liczby = remove_values_from_list(liczby, liczby[i])#usuń wszystkie takie elementy w liście


print(liczby)