class Stack(object):

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peak(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


s = Stack()

print(s.isEmpty())
s.push(1)
s.push(2)
s.push(4)

print(s.peak())
print(s.size())
s.pop()
print(s.isEmpty())
s.pop()
s.pop()
print(s.isEmpty())
