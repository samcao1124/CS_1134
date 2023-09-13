from ArrayStack import ArrayStack
from ArrayDeque import ArrayDeque

class MidStack:
    def __init__(self):
        self.stack = ArrayStack()
        self.array_deque = ArrayDeque()

    def is_empty(self):
        return (len(self.stack) == 0 and len(self.array_deque) == 0)

    def __len__(self):
        return len(self.stack) + len(self.array_deque)

    def push(self, val):
      if (len(self.stack) == len(self.array_deque)):
        if (self.is_empty()):
          self.stack.push(val)
        else:
          self.stack.push(self.array_deque.dequeue_first())
          self.array_deque.enqueue_last(val)
      else:
        self.array_deque.enqueue_last(val)

    def mid_push(self, val):
      self.array_deque.enqueue_first(val)
      if (len(self.array_deque) > len(self.stack)):
        self.stack.push(self.array_deque.dequeue_first())

    def top(self):
      if (self.is_empty()):
          raise Exception("Stack is empty")
      return self.stack.top() if self.array_deque.is_empty() else self.array_deque.last()

    def pop(self):
      if(self.is_empty()):
          raise Exception("Stack is empty")
      return self.stack.pop() if self.array_deque.is_empty() else self.array_deque.dequeue_last()
