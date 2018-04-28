import time

start_time = time.clock()

max= 1000
tablica = [0,0] 
pierwsze = []

for z in range(2,max+1): 
    tablica.append(1)
    
for i in range(2,max+1):
    j=0
    j=2*i
    while(j<=max):
        tablica[j]=0
        j+=i
    
for k in range(0,max+1):
    if (tablica[k]==1):
        pierwsze.append(k)
        
        
end_time = time.clock()-start_time

for s in range(0,len(pierwsze)):
    print(pierwsze[s])
        
print("--- %s seconds ---" % (end_time))