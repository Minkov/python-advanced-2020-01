class Stack:
    def __init__(self):
        self.internal_values = []

    def push(self, value):
        return self.internal_values.append(value)

    def pop(self):
        return self.internal_values.pop()

    def peek(self):
        return self.internal_values[-1]

    @property
    def is_empty(self):
        return self.size == 0

    @property
    def size(self):
        return len(self.internal_values)


s = Stack()

[s.push(x) for x in range(5)]

while not s.is_empty:
    print(s.pop())
