class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class Nawiasy:
    def __init__(self):
        self.head = None


    def isEmpty (self):
        if self.head == None:
            return True
        else:
            return False

    def push(self, data):
        if not self.head:
            n = Node(data)
            self.head = n
            self.tail =n
        else:
            n = self.head
            while n.next != None:
                n = n.next
            new = Node(data)
            n.next = new

    def pop(self, data):
        n = self.head
        p = n
        while n.next != None:
            p = n
            n = n.next
        if n.data == data:
            n=None
            p.next = None
        else:
            print( "Bledne wyrazenie")
            self.head = None



stos = Nawiasy()

wyrazenie = input("Podaj wyrazenie: ")

wyrazenie = list(wyrazenie)
print(wyrazenie)

for i in range (0,len(wyrazenie)):
    while not stos.isEmpty():
        if wyrazenie[i] == '(' or wyrazenie[i] == '[':
            stos.push(wyrazenie[i])
        elif wyrazenie[i] == ')':
            stos.pop('(')
        elif wyrazenie[i] == ']':
            stos.pop('[')


