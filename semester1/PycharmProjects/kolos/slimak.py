h = int(input("Podaj dlugosc slupa: "))

x=5 #predkosc na dzien
y=3 #predkosc na noc

p=6 #co ile polka

s=0 #droga ktora pokonal
d=0 #ile dni

while s<h:
    s+=5

    lastP= p*(s//p) # na jakiej wys ostatnia polka

    if (s-y)<lastP:
        s=lastP
    else:
        s=s-y
    d+=1

print("Dotarl po", d, "dniach")

