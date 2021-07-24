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

    def display(self):
        p = self._head
        i = 0
        if self.is_empty():
            print("nothing to print on console ..")
            print()
            return
        else:
            while i < self._size:
                print(p._element,end=" ")
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
print("####################################")
print("Circular Linked List : ")
n.display()
print()
print(len(n))