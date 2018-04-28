
import time

def silRek (n):
    if (n==1) or (n==0):
       return 1
    else:
        return n*(silRek(n-1))
    

x=int(input("Silnia z "))
start = time.clock()
z=silRek(x)
end = time.clock()
total = end-start
print("Rek.wynosi:",z," i zajmuje: ", total)

        
def silIt (n):
    sil = 1
    for i in range (1,n+1):
        sil= sil*i
    return sil
    
start = time.clock()
y=silIt(x)
end = time.clock()
total = end-start
print("Ite.wynosi:",y," i zajmuje: ", total)
        
