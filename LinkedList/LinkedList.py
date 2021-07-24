class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
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
            self._head = new_element
        else:
            self._tail._next = new_element
        self._tail = new_element
        self._size = self._size + 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end=" ")
            p = p._next


n = LinkedList()
n.add_at_the_last(10)
n.add_at_the_last(20)
n.add_at_the_last(30)
n.add_at_the_last(40)
n.add_at_the_last(50)
print(len(n))
n.display()
