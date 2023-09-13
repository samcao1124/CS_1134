from ArrayStack import ArrayStack
class MaxStack:
    def __init__(self):
      self.stack = ArrayStack()

    def is_empty(self):
      return self.stack.is_empty()

    def __len__(self):
      return len(self.stack)

    def push(self, val):
      cur_max = None if self.is_empty() else self.stack.top()[1]
      if cur_max == None or val > cur_max:
        self.stack.push((val, val))
      else:
        self.stack.push((val, cur_max))

    def top(self):
      if (self.is_empty()):
        raise Exception("Stack is empty")
      return self.stack.top()[0]

    def pop(self):
      if(self.is_empty()):
        raise Exception("Stack is empty")
      return self.stack.pop()[0]

    def max(self):
      if (self.is_empty()):
          raise Exception("Stack is empty")
      return self.stack.top()[1]

