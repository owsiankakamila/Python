a=input("Podaj liczbe(2): ")

o=len(a)-1
j=0
s=0
for i in range(o,-1,-1):
    p=2**j
    x=int(a[i])
    s+=x*p
    j+=1
    print(s)

    



