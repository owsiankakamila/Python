"""import time
def silniaIt (n):
    silnia =1
    for i in range (2,n+1):
        silnia*=i
        return silnia
    
def silniaRek (n):
    if n==1 or n==0:
        return 1  

  
def fibRek (n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return fibRek(n-2)+fibRek(n-1)


def fibIt (n):
    a, b = 0, 1
    if a<n:
        a, b = b, a+b
    return a
        
k=20
start = time.clock()
silniaRek(k)
end=time.clock()
total = end-start
print ("sit=",total)"""

for i in range (0,10):
    print(i)