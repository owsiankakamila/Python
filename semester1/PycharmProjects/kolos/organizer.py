class Node:
    def __init__(self,name,money,next=None,prev=None):
        self.name=name
        self.money=money
        self.next=next
        self.prev=prev

    def __str__(self):
        return str(self.name)
    
    def __int__(self):
        return int(self.money)

class Organizer:
    def __init__(self):
        self.head = None

    def push_this_end(self, name, money, this):
        if not self.head:
            n= Node(name, money)
            self.head = n
        else:
            n=self.head
            while (n.name != this) and (n.next != None):
                n=n.next
            if n.name == this and n.next!=None:
                before=n
                after=n.next
                new = Node(name,money,before,after)
                before.prev = new
                after.next = new
            elif n.next==None: #jesli jest na koncu albo nie znajdzie to dodaj na koniec
                new = Node(name, money, None, n)
                n.next = new



    def push_front(self,name, money):
        n=self.head
        new = Node (name,money,n,None)
        n.prev = new
        self.head = new

    def print (self):
        n = self.head
        while n!= None:
            print(str(n), int(n))
            n=n.next




            
