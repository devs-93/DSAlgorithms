class _Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next):
        self._element = element
        self._next = next


class QueueLinkedList:
    def __init__(self):
        self._front = None
        self._rear = None
        self._size = 0

    def __len__(self):
        return self._size

    def isempty(self):
        return self._size == 0

    def enqueue(self, e):
        new_element = _Node(e, None)
        if self.isempty():
            self._front = new_element
        else:
            self._rear._next = new_element

        self._rear = new_element
        self._size = self._size + 1

    def dequeue(self):
        if self.isempty():
            print("queue is empty ..")
            return
        else:
            deleted_element = self._front._element
            self._front = self._front._next
            self._size = self._size - 1
        if self.isempty():
            self._rear = None
        return deleted_element

    def first(self):
        if self.isempty():
            print("queue is empty ..")
            return
        else:
            return self._front._element

    def display(self):
        p=self._front
        while p:
            print(p._element,end=" ")
            p=p._next
        print()

Q=QueueLinkedList()
Q.enqueue(5)
Q.enqueue(3)
Q.enqueue(4)
Q.enqueue(10)
print("Length :",len(Q))
Q.display()
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())
print(Q.dequeue())

Q.display()
