class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def add_at_the_last(self, e):
        new_element = _Node(e, None)
        if self.is_empty():
            new_element._next = new_element
            self._head = new_element
        else:
            new_element._next = self._tail._next
            self._tail._next = new_element
        self._tail = new_element
        self._size = self._size + 1

    def add_at_the_beginning(self, e):
        new_element = _Node(e, None)
        if self.is_empty():
            new_element._next = new_element
            self._head = new_element
            self._tail = new_element
            self._size = self._size + 1
        else:
            new_element._next = self._head
            self._tail._next = new_element
        self._head = new_element
        self._size = self._size + 1

    def add_at_any_position(self, e, pos):
        new_element = _Node(e, None)
        p = self._head
        pos_count = 1
        if self._size == 0:
            print("No element found in the circular linked list :")
            return -1
        else:
            while pos_count < pos - 1:
                p = p._next
                pos_count = pos_count + 1
            new_element._next = p._next
            p._next = new_element
            self._size = self._size + 1

    def delete_first_element(self):
        if self.is_empty():
            print("no element to delete ..")
            return
        else:
            deleted_element = self._head._element
            self._tail._next = self._head._next
            self._head = self._head._next
            self._size = self._size - 1
        if self.is_empty():
            self._head = None
            self._tail = None
        return deleted_element

    def delete_last_element(self):
        if self.is_empty():
            print("no element to delete..")
            return
        else:
            p = self._head
            i = 1
            while i < self._size - 1:
                p = p._next
                i = i + 1
            self._tail = p
            p = p._next
            self._tail._next = p._next
            self._size = self._size - 1
        return p._element

    def display(self):
        p = self._head
        i = 0
        if self.is_empty():
            print("nothing to print on console ..")
            print()
            return
        else:
            while i < self._size:
                print(p._element, end=" ")
                p = p._next
                i = i + 1


n = CircularLinkedList()
n.add_at_the_last(101)
n.add_at_the_last(201)
n.add_at_the_last(301)
n.add_at_the_last(401)
n.add_at_the_last(501)
n.add_at_the_last(521)
n.add_at_the_last(50001)
print(len(n))
print("#################################################################")
print("Circular Linked List add at the end: ")
n.display()
print()
print("Size of the Linked List: ", len(n))

print()
print("#################################################################")
print("Circular Linked List add at the starting: ")
n.add_at_the_beginning(100)
n.add_at_the_beginning(200)
n.display()
print()
print("Size of the Linked List: ", len(n))

print()
print("#################################################################")
print("Circular Linked List add at given position in the list: ")
n.add_at_any_position(1223221, 3)
n.add_at_any_position(12521, 4)
n.display()
print()
print("Size of the Linked List: ", len(n))

print()
print("#################################################################")
print("Delete first element from Circular Linked List .... ")
print("Before Deletion :")
n.display()
n.delete_first_element()
print("\nAfter Deletion :")
n.display()
print()
print("Size of the Linked List: ", len(n))

print()
print("#################################################################")
print("Delete last element from Circular Linked List .... ")
print("Before Deletion :")
n.display()
n.delete_last_element()
n.delete_last_element()
print("\nAfter Deletion :")
n.display()
print()
print("Size of the Linked List: ", len(n))
