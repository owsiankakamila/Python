wys =5
def pascal(wiersz,nr):
        if nr == 1 or nr == wiersz+1:
            return 1
        else:
            return pascal(wiersz-1, nr-1) + pascal(wiersz-1, nr)

for w in range (0,wys):
    for i in range (0,wys-w):
        print(" ", end="")
    for j in range(1, w+2):
        n = pascal(w, j)
        print(n, end=" ")
    print("")
