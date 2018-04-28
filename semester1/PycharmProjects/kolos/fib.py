def fibRek (n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibRek(n-1)+fibRek(n-2)

def fibIt(n):
    a=0
    b=1
    for i in range(1, n):
       a, b = b, (a+b)

    return b


print(fibIt(19))
print(fibRek(19))