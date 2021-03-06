''' RAPORT SORTOWANIE''' #Kamila Owsianka gr.1b wtorek 9:30

import random
import time

'''TWORZENIE TABLICY'''
def tworzeTablice (tab,rozmiar):
    for i in range(0,rozmiar):
        random.seed()
        losowana = random.randrange(100)  
        tab.append(losowana)
    print(tab)
    
'''SELECTION SORT/ WYBIERANIE '''
def selectionSort(tab):
    tablica = tab [:]
    pozycja=0
    for i in range(0,len(tablica)): #wybrany element to tab i
        najmniejszy=tablica[i]
        pozycja=i
        for j in range(i+1,len(tablica)):
            if(najmniejszy>tablica[j]): #szuka mniejszego elemnetu po prawo od wybranego (i)
                najmniejszy=tablica[j] #jesli mniejszy zapisywany do 'najmniejszy'
                pozycja=j

        tablica[i],tablica[pozycja]=tablica[pozycja],tablica[i] #zamiana miejscami wybranego z najmniejszym

 
'''INSERTION SORT/ WYSTAWIANIE'''
def insertionSort(tab):
    tablica = tab [:]
    for i in range(1,len(tablica)): # wybrana liczba to tab i
        wybrana = tablica[i]
        x=i          # x jest indeksem gdzie znajduje sie nasza wybrana liczba, wzgledem ktorej sortujemy              
        for j in range(i-1,-1,-1):  # sprawdzaj na lewo od wybranej liczby, do -1 bo musi objac index 0
            if(tablica[j] > wybrana):  
                tablica[x],tablica[j]=tablica[j],tablica[x] #jeśli liczba po lewo większa to zamien kolejnoscią
                x=x-1   #nasza wybrana liczba przesunela sie o jeden w lewo
            else:
                break # po lewo od wybranej są tylko mniejsze wiec nie ma sensu dalej sprawdzac

'''BUBBLE SORT/ BABELKOWE'''
def bubbleSort(tab): 
    tablica=tab [:]
    flag=True
    for i in range(0,len(tablica) -1):
        if flag==False: break #jesli przelecialo po calej tablicy i nic nie zamienilo to przerwij(sa posortowane)
        flag=False
        for j in range(0,len(tablica) -1 -i): # -i bo będzie już i największych uporządkowanych na końcu
            if (tablica[j]>tablica[j+1]): #jesli wybrana liczba jest wieksza od tej po prawo to zamien miejscami = przesun w prawo
                tablica[j],tablica[j+1]=tablica[j+1],tablica[j]
                flag=True
            
     
'''QUICK SORT/ SZYBKIE'''
def quickSort(tab): # funkcja pomocnicza,aby podac jako argument tylko tablice
    tablica = tab [:]
    quickAction(tablica,0,len(tablica)-1)
    
def quickAction (tab, start, stop):
    if start < stop:
        end = quickDivide(tab,start,stop) # porzadkuje pivot(1. element)
       
        quickAction(tab,start,end-1) # uporzadkuj mniejsze od pivota
        
        quickAction(tab,end+1,stop) # uporzadkuje wieksze do pivota
        
def quickDivide(tab,start,end):
    pivot=start #pivot pierwszy element tablicy
    pointerLeft=pivot +1
    pointerRight=end
    
    action = True
    while action == True: # dopoki pointery sie nie krzyzuja
        '''!!! kolejnosc warunkow ma znaczenie:'''
        while (pointerLeft<=pointerRight) and (tab[pointerLeft]<= tab[pivot]): #az znajde taki left ktory jest wiekszy od pivota
            pointerLeft+=1
            
        while (pointerLeft<=pointerRight) and (tab[pointerRight]>=tab[pivot]): #az znajde taki right ktory jest mniejszy od pivota
            pointerRight-=1
          
        if (pointerLeft>pointerRight): # krzyzuja sie = trafiaja na nie swoj obszar, gdzie kazdy nastepny by podmienily
            action = False
        else:
            
            tab[pointerLeft],tab[pointerRight] = tab[pointerRight],tab[pointerLeft]#zamieniamy taki left ktory jest wiekszy od pivota na taki right ktory jest mniejszy od pivota
           
    tab[pivot], tab[pointerRight] = tab[pointerRight], tab[pivot] #ustawia pivot na "posegregowanym miejscu"
   
    
    return pointerRight #pointRight wskazuje na miejsce gdzie teraz znajduje sie pivot (uporzadkowany element)
    

'''MERGE SORT/ SCALANIE'''
def mergeSort(tab): # funkcja pomocnicza,aby podac jako argument tylko tablice
    tablica = tab [:]
    tablica =mergeAction(tablica)
    
def mergeAction (tab):
    if len(tab)<2:
        return tab
    mid = len(tab)//2 #dzieli na pol i tak sie dzieli az jedno elementowe i wtedy zaczyna sie wykonywac merge
    left = mergeAction(tab[:mid])
    right = mergeAction(tab[mid:])
    
    return merge(left,right)
    
def merge (left,right): #scala dwie posortowane tablice w jedna
    sortedPart = []
    i=0
    j=0
    while (len(sortedPart)!=(len(left)+len(right))): #az rozmiar bedzie dobry
        if left[i]<right[j]:
            sortedPart.append(left[i]) #z left dodaje do tablicy, wskaznik w prawo
            i+=1
        elif left[i]>=right[j]:
            sortedPart.append(right[j])#z right dodaje do tablicy, wskaznik w prawo
            j+=1
        
        if i == len(left): #gdy dojdzie do konca lewej tablicy
            sortedPart.extend(right[j:]) #dopisz wszystko co zostalo z prawej tablicy do naszej posortowanej
            
        if j == len(right):#analogicznie
            sortedPart.extend(left[i:])  
            
    return sortedPart

'''HEAP SORT/ KOPCOWANIE'''
def heapSort(tab):
    tablica = tab [:]
    lastIndex = len(tablica) - 1
    '''przygotowanie drzewa(od dolu, od lisci)'''
    '''od ostatniego rodzica'''
    lastParent = lastIndex//2
    for x in range (lastParent,-1,-1):
        heapify(tablica,x,lastIndex)
    
    lastTofirst(tablica,lastIndex) #zamiana ostatniego z pierwszym
    lastIndex -= 1 #last index jest juz posortowany
    
    '''sortowanie drzewa (od korzenia)'''
    for y in range (0,lastIndex,1):
        heapify(tablica,0,lastIndex)
        lastTofirst(tablica,lastIndex)
        lastIndex -= 1
    
        
def heapify(tab,parent,lastIndex):
    
    kidLeft =  2*parent + 1
    kidRight = 2*parent + 2
    
    largest = parent
    
    if kidLeft <=  lastIndex and tab[kidLeft]  > tab[parent]: #index nalezy do tablicy, wiekszy od rodzica
        largest = kidLeft
        
    if kidRight <= lastIndex and tab[kidRight] > tab[largest]: #większy z dzieci!
        largest = kidRight
        
    if largest != parent:
        tab[largest], tab[parent] = tab[parent], tab[largest]
        heapify(tab,largest,lastIndex) #rekursywnie sprawdzanie w dol czy zmieniony jest ok
        
def lastTofirst(tab,lastIndex):
    tab[lastIndex], tab[0] = tab[0], tab[lastIndex]
    

    
     
liczby=[]

liczbyRozmiar =5000


tworzeTablice(liczby,liczbyRozmiar)

czas = time.clock()
selectionSort(liczby)
czas = time.clock()-czas
print("selectionSort: ",czas)

czas = time.clock()
insertionSort(liczby)
czas = time.clock()-czas
print("insertionSort: ",czas)

czas = time.clock()
bubbleSort(liczby)
czas = time.clock()-czas
print("bubbleSort:    ",czas)

czas = time.clock()
quickSort(liczby)
czas = time.clock()-czas
print("quickSort:     ",czas)

czas = time.clock()
mergeSort(liczby)
czas = time.clock()-czas
print("mergeSort:     ",czas)

czas = time.clock()
heapSort(liczby)
czas = time.clock()-czas
print("heapSort:      ",czas)















