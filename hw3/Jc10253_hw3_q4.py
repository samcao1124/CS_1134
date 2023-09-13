from ArrayStack import ArrayStack
class Queue:
    def __init__(self):
        self.stack = ArrayStack()
        self.buffer = ArrayStack()

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)

    def enqueue(self, val):
        self.stack.push(val)

    def dequeue(self):
        if self.stack.is_empty():
            raise Exception ("stack is empty")
        while (not self.stack.is_empty()):
            self.buffer.push(self.stack.pop())
        result = self.buffer.pop()
        while (not self.buffer.is_empty()):
            self.stack.push(self.buffer.pop())
        return result

