# LICZBY ZAPRZYJAZNIONE
liczba1 = 118
suma_dzielnikow = 0

for i in range (1,liczba1):
  if liczba1%i ==0: #jeśli to dzielnik
    suma_dzielnikow += i

liczba2 = suma_dzielnikow
suma_dzielnikow = 0
for i in range (1,liczba2):
  if liczba2%i ==0:
        suma_dzielnikow += i

if suma_dzielnikow == liczba1:
  print("jest to liczba zaprzyjaznona!")
else:
  print("to nie liczba zaprzyjaznona")
