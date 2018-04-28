# STOS Z ONP

class Node:
  def __init__(self,value,prev = None):
    self.value = value
    self.prev = prev
  def __int__(self):
    return int(self.value)
    
class ONP:
  def __init__(self):
    self.head = None
    self.tail = None
    
  def add_at_the_end(self,value):
    # pierwszy element listy:
    if self.tail == None:
      n=Node(value)
      self.tail=n
      self.head=n
    else:
      n=Node(value)
      n.prev= self.tail
      self.tail = n
      
  def count_it(self, operator):
    #jesli jest to zarazem pierwszy element
     #if self.tail == self.head:
      # print("Zle wpisales wyrazenie")
       #break
     
    # weź ostatni i przedostatni element
    n=self.tail
    ostatni = n.value
    n=n.prev
    przedostatni = n.value
    
    # wykonaj operacje (+ = * /)
    if operator == '+':
      wynik = ostatni+przedostatni
    elif operator == '-':
      wynik = ostatni-przedostatni
      
    elif operator == '*':
      wynik = ostatni*przedostatni
    elif operator == '/':
      wynik = ostatni/przedostatni
      
    #usun ostatni el. listy
    n=self.tail
    self.tail = n.prev # wsk na przedostatni
    n.prev = None
    
    #wynik zastap przedostatnim
    n=self.tail
    n.value = wynik
  
  def __int__(self):
    n=self.head
    return int(n.value)
    
      

stos = ONP()

wyrazenie = input("Podaj wyrazenie: ")
wyrazenie = "".join(wyrazenie).split(' ')
#wyrazenie = list(wyrazenie)

for i in range (0,len(wyrazenie)):
  if wyrazenie[i]== '+' or wyrazenie[i]== '-' or wyrazenie[i]== '*' or wyrazenie[i]== '/':
    operator = wyrazenie[i]
    stos.count_it(operator)
  else:
    value = wyrazenie[i]
    stos.add_at_the_end(int(value))
    
print("wynik to: ", int(stos))
