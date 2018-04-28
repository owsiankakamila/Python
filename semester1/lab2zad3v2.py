n = int(input("Podaj liczbe:"))
x = int(input("Podaj system:"))
lista=[]
wynik=0

while (n!=0):
    m=n%x
    lista.append(m)
    n=n//x

r=len(lista)

for i in range(0,r):
    wynik+=lista[i]*(10**i)
    
print(wynik)

    


#print(wynik)
    
'''
# Over-explaining a bit:
def magic(numList):         # [1,2,3]
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    s = int(s)              # 123
    return s
lista.reverse()
wynik = int(''.join(map(str,lista))) #list to int'''