class Node:
    def __init__(self, num):
        self.num = num
        self.next = None
    def __int__(self):
        return int(self.num)

class ONP:
    def __init__(self):
        self.head = None

    def add(self, num):
        if not self.head:
            n = Node(num)
            self.head =n
        else:
            n = self.head
            while (n.next != None):
                n=n.next
            new = Node(num)
            n.next = new

    def count (self,operator):
        n = self.head
        while n.next.next != None:
            n= n.next

        if operator == '+':
            wynik = int(n.num) + int(n.next.num)
        elif operator == '-':
            wynik = int(n.num) - int(n.next.num)
        elif operator == '/':
            wynik = int(n.num) / int(n.next.num)
        elif operator == '*':
            wynik = int(n.num) * int(n.next.num)

        n.num = wynik
        n.next =None




wyrazenie = input("Podaj wyrazenie: ")
wyrazenie= "".join(wyrazenie).split(" ")

stos = ONP()

for i in range(0, len(wyrazenie)):
    if wyrazenie[i] == '+' or wyrazenie[i] == '-' or wyrazenie[i] == '/' or wyrazenie[i] == '*':
        stos.count(wyrazenie[i])
    else:
        stos.add(wyrazenie[i])

print("Wynik to:", int(stos.head.num))


