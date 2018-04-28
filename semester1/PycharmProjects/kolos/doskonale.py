number = int(input("Doskonale od 0 do "))


for n in range (1, number):
    suma = 0

    for i in range (1, (n//2+1)):
        if n%i ==0:

            suma+=i
    if n==suma:
        print(n)

