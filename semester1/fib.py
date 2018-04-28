import time

def fibRek(n):
    if (n==0):
        return 0
    elif (n==1):
        return 1
    else:
        return fibRek(n-2)+ fibRek(n-1)
        
        
        
x = int(input("Fiboncci z "))
start = time.clock()
z=fibRek(x)
end = time.clock()
total = end-start
print("Rek.wynosi:",z," i zajmuje: ", total)


def fibIt(n):
    if (n==0):
        return 0
    if (n==1):
        return 1
    
    a=1
    b=0
    s=a+b
    for i in range (3,n+1):
        b=a
        a=s
        s=a+b
        
    return s
    
start = time.clock()
y=fibIt(x)
end = time.clock()
total = end-start
print("Ite.wynosi:",y," i zajmuje: ", total)
    
    










