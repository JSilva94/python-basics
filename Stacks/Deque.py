class Deque(object):

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.append(item)

    def addBack(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeBack(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
