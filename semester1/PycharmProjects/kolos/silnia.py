def silniaRek(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n*(silniaRek(n-1))

def silniaIt(n):
    if n==0:
        return 0
    else:
        silnia=1
        for i in range (n, 0, -1):
            silnia*=i
        return silnia


print(silniaRek(34))
print(silniaIt(34))