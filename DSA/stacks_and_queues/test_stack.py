# Stack Implementation without deque


class Stack:
    def __int__(self):
        self._items = []

    def is_empty(self):
        # if len(self._items) == 0:
        #     return True
        # else:
        #     return False
        return not bool(self._items)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        else :
            # how to throw error
            raise Exception("Pop from empty stack")

    def push(self, value):
        self._items.append(value)

