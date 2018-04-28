class Node:

    def __init__(self, name,points, next= None, previous = None):
        self.name = name
        self.points = points
        self.next = next
        self.prev = previous

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.points)


class UnidirectionalList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # [ADD] FUNCTIONS:

    def add_at_the_end(self, name, points):
        # first element (no head no tail)
        if not self.head:
            n = Node(name, points)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            p= self.tail
            new_node = Node(name, points, None, p)
            p.next = new_node
            self.tail = new_node
            self.size += 1

    def add_to_the_beggining(self, name, points):
        # first element (no head)
        if not self.head:
            n = Node(name, points)
            self.head = n
            self.tail = n
            self.size += 1
        else:
            n = self.head
            new_node = Node(name, points, n, None)
            n.prev = new_node
            self.head = new_node
            self.size += 1

    def add_at_position(self,name, points, position=1):
        if position == 1:
            self.add_to_the_beggining(name,points)
        elif position == self.size:
            self.add_at_the_end(name,points)
        else:
            n= self.head
            for i in range(1, position):
                n = n.next
            new_node = Node(name, points, n, n.prev)
            p = n.prev
            p.next = new_node
            n.prev = new_node
            self.size += 1

    # long version of add at the end
    '''def add_at_the_end_long(self, name, points):
        # first element (no head)
        if not self.head:
             n = Node(name,points)
             self.head = n
             self.tail = n
            self.size += 1
         # next elements
        else:
            n = self.head
            while n.next != None:
                n = n.next
             new_node = Node(name, points, None, n) # n set prev
             n.next = new_node
            self.tail = new_node
             self.size += 1'''

    # [DELETE] FUNCTIONS:

    def delete_from_the_beggining(self):
        n = self.head
        n = n.next
        self.head = n
        n.prev = None
        self.size -=1

    def delete_from_the_end(self):
        p = self.tail
        p = p.prev
        self.tail = p
        p.next = None
        self.size = -1

    # [PRINT] FUNCTIONS:

    def print_left_to_right(self):
        n = self.head
        while n:
            print(str(n), int(n))
            n = n.next

    def print_right_to_left(self):
        n = self.tail
        while n:
            print(str(n), int(n))
            n=n.prev

    # [FIND] FUNTIONS:

    def find_the_best(self):
        n = self.head
        current_points = n.points
        current_name = n.name
        best_points = current_points
        best_name = current_name

        while n.next != None:
            n = n.next
            current_points = n.points
            current_name = n.name
            if current_points > best_points:
                best_points = current_points
                best_name = current_name
        print("Najlepszy Pan", best_name, "z wynikiem ", best_points)
        return str(best_name), int(best_points)


ll = UnidirectionalList()
ll.add_at_the_end("Kowalski",7)
ll.add_at_the_end("Nowak", 8)
ll.add_at_the_end("Zalewka", 30)
ll.add_at_the_end("Panio", 21)
ll.add_to_the_beggining("Siemien", 15)
ll.add_at_position("helo",3,3)


ll.print_left_to_right()
ll.find_the_best()
