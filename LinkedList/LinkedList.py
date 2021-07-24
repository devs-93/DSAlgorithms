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

    def add_at_the_beginning(self, e):
        new_element = _Node(e, None)
        if self.is_empty():
            self._head = new_element
            self._tail = new_element
        else:
            new_element._next = self._head
            self._head = new_element
        self._size = self._size + 1

    def add_at_any_position(self, e, pos):
        new_element = _Node(e, None)
        p = self._head
        index = 1
        if self._size < pos or pos < index:
            return -1
        while index < pos-1:
            p = p._next
            index = index + 1
        temp = p._next
        p._next = new_element
        new_element._next = temp
        self._size = self._size + 1

    def display(self):
        p = self._head
        while p:
            print(p._element, end=" ")
            p = p._next

    def search(self, key):
        p = self._head
        index = 0
        while p != None:
            if p._element == key:
                return index
            else:
                p = p._next
                index = index + 1
        return -1


n = LinkedList()
n.add_at_the_last(10)
n.add_at_the_last(20)
n.add_at_the_last(30)
n.add_at_the_last(40)
n.add_at_the_last(50)
print(len(n))
print("Linked List")
n.display()
print()
print("Add at the beginning :")
n.add_at_the_beginning(100)
n.display()
print()
print(len(n))
print("Insert at Given Position")
print("insert element and position :")
e, p = input().split(" ")
n.add_at_any_position(int(e), int(p))
print("display after insertion :")
n.display()
# key = int(input("enter key to search into the lined list: "))
# print("Result :", n.search(key))
