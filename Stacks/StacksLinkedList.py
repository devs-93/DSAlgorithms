class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class StacksLinkedList:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def push(self, e):
        newest = _Node(e, None)
        if self.isempty():
            self._top = newest
        else:
            newest._next = self._top
            self._top = newest
        self._size = self._size + 1

    def pop(self):
        if self.isempty():
            print("no element to delete .")
            return
        else:
            deleted_element = self._top._element
            self._top = self._top._next
            self._size = self._size - 1
        return deleted_element

    def top(self):
        if self.isempty():
            print("nothing to return , stack is empty .")
            return
        else:
            return self._top._element

    def display(self):
        if self.isempty():
            print("nothing to display .")
            return
        else:
            p = self._top
            while p:
                print(p._element, end=" ")
                p = p._next
            print()


s=StacksLinkedList()
s.push(5)
s.push(3)
print("length",len(s))
s.display()
print(s.pop())
print(s.pop())
print(s.pop())
s.display()