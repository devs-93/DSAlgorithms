class StackArray:
    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self,e):
        self._data.append(e)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self._data.pop()

    def top(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self._data[-1]



s=StackArray()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print(s._data)
print(len(s))
print(s.pop())
print(s._data)
print(s.top())


