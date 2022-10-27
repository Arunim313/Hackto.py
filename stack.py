class Stack:
        def __init__(self):
                    self.items = []
        def is_empty(self):
                    return self.items == []
        def push(self, item):
                    self.items.append(item)
        def pop(self):
                    return self.items.pop()
        def peek(self):
                    l = len(self.items)-1
                    return self.items[l]
        def size(self):                                                                             return len(self.items)
