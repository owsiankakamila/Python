a=input("Podaj liczbe: ")
z=int(input("Z jakiego systemu: "))
d=int(input("Do jakiego sytemu: "))
dziesietny=0
wybrany=0

#zamiana na system dziesietny

r=len(a)

for i in range(0,r):
    c=a[i]
    c=int(c)
    dziesietny+=c*(z**(r-1-i))

print(dziesietny)

#zamiana z dziesietnego na wybrany
dziesietny=str(dziesietny)
dl_dziesietny=len(dziesietny)
dziesietny=int(dziesietny)


for j in range(0,dl_dziesietny+1):
    reszta=dziesietny%d
    dziesietny=dziesietny//d
    
    
    wybrany+=reszta*(10**j)
    
print(wybrany)
