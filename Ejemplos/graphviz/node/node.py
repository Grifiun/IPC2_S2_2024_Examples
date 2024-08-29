class Node:
    def __init__(self, id, text, next=None, x = 0, y = 0):
        self.id = id
        self.text = text
        self.next = next
        self.x = x
        self.y = y

    def __iter__(self):
        self.current = self
        return self

    def __next__(self):
        if self.current is None:
            raise StopIteration
        else:
            current_node = self.current
            self.current = self.current.next
            return current_node

    def set_next(self, node):
        self.next = node