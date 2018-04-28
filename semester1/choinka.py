n=int(input("Podaj liczbe: "))

for k in range (2,n+2,1):   
    for i in range (1,k+1,1):
        print("")
        l=2*i-1
        c=(2*n +2)-2*i
        for p in range (1,c+1,1):
            print(" ",end="")     
        for j in range (1,l+1,1):
            print ("x",end=" ")
            