class DEQueueArrays:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def add_first(self, e):
        self._data.insert(0, e)

    def add_last(self, e):
        self._data.append(e)

    def remove_first(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            return self._data.pop(0)

    def remove_last(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            return self._data.pop()

    def first_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            return self._data[0]

    def last_element(self):
        if self.is_empty():
            print("Queue is empty.")
            return
        else:
            return self._data[-1]


dq = DEQueueArrays()
dq.add_first(10)
dq.add_first(20)
dq.add_first(30)
dq.add_first(40)
print(dq._data)
dq.add_last(100)
dq.add_last(200)
dq.add_last(300)
dq.add_last(400)
print(dq._data)
dq.remove_last()
print(dq._data)
dq.remove_last()
dq.remove_last()
print(dq._data)
