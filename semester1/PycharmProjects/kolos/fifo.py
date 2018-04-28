class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class Fifo:
    def __init__(self):
        self.head = None

    def push(self,data):
        if not self.head:
            n= Node(data)
            self.head = n
            print("Dodano!")
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new = Node(data)
            n.next = new
            print("Dodano!")

    def pop (self):
        if not self.head:
            print ("Nie mozna wykonac - brak elementow na liscie")
        else:
            n=self.head
            if n.next == None:
                self.head = None
                print("Usunieto! Na liscie nie ma elementow")
            else:
                while n.next.next != None:
                    n = n.next
                n.next = None
                print("Usunieto!")

    def print(self):
        n = self.head
        while n!= None:
            print(n.data, end=" ")
            n=n.next
        print("")


lista = Fifo()

lista.push(2)
lista.print()
lista.push(2)
lista.push(2)
lista.print()
lista.pop()
lista.print()
lista.pop()
lista.print()
lista.pop()
lista.print()
lista.pop()



