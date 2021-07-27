class QueuesArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def isempty(self):
        return len(self._data) == 0

    def enqueue(self, e):
        self._data.append(e)

    def dequeue(self):
        if self.isempty():
            print("empty queue found ..")
            return
        else:
            return self._data.pop(0)

    def first(self):
        if self.isempty():
            print("empty queue found ..")
            return
        else:
            return self._data[0]


Q = QueuesArray()
Q.enqueue(5)
Q.enqueue(3)
Q.enqueue(7)
Q.enqueue(12)

print("Length of the Queue : ", len(Q))
print("Displaying queue : ", Q._data)
print("dequeue items from the queue :",Q.dequeue())
print("Displaying queue : ", Q._data)
print("first element of the queue :" , Q.first())
