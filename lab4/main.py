def stack_sum(s):
    """
: s type: ArrayStack
: return type: int
"""

    total = 0
    if len(s) == 0:
        return total
    else:
        val = s.pop()
        total = val + stack_sum(s)
        s.push(val)
        return total

def eval_prefix(exp_str):
    """
: exp type: str
: return type: int

"""
    oper = "+-/*"
    exp_lst = exp_str.split( )
    for i in exp_lst:
        if i in oper:
            stack.push(i)
        if i.isdigit():
            number = int(i)


def flatten_list(lst):
    """
: lst type: list
: return type: None
"""
    s = ArrayStack()
    while len(lst) != 0:
        number = lst.pop()
        if isinstance(number,list):
            lst.extend(number)
        else:
            stack.push(number)
class ArrayDeque:
    INITIAL_CAPACITY = 0
    def __init__(self):
        '''Initializes an empty Deque using a list as self.data.'''

        self.data = make_array(ArrayDeque.INITIAL_CAPACITY)
        self.num = 0
        self.front = None
        self.back = None
    def __len__(self):
        return self.num

    def is_empty(self):
        '''Return True if the deque is empty.'''
        return self.num == 0

    def enqueue_first(self, elem):
        '''Add elem to the front of the Deque.'''
        if self.num == len(self.data):
            self.resize(2*len(self.data))
        self.front = 0
        self.back = 0
        self.num = 1
    def enqueue_last(self, elem):
        '''Add elem to the back of the Deque.'''
        if self.num == len(self.data):
            self.resize(2*len(self.data))
        self.front = 0
        self.back = 0
        self.num = 1
    def dequeue_first(self):
        '''Remove and return the first element from the Deque.
    Or raises an Exception if the Deque is empty'''
        if self.is_empty():
            raise Exception ("Queue is empty")
        value = self.data[self.front]
        self.data[self.front = None]
    def dequeue_last(self):
        if self.is_empty():
            raise Exception ("Queue is empty")
        value = self.data[self.front]
        self.data[self.front]= None

class MeanQueue:
    def __init__(self):
        self.data = ArrayQueue()
    def __len__(self):
        '''Return the number of elements in the queue'''
        return len(self.data)
    def is_empty(self):
        ''' Return True if queue is empty'''
        return self.data.is_empty()
    def enqueue(self, e):
        ''' Add element e to the front of the queue. If e is not
    an int or float, raise a TypeError '''
        self.data.enqueue(e)
    def dequeue(self):
        ''' Remove and return the first element from the queue. If
    the queue is empty, raise an exception'''
        elem = self.data.dequeue()
    def first(self):
        return self.data.first



class QueueStack:
    def __init__(self):
        self.data = ArrayQueue()
    def __len__(self):
        return len(self.data)
    def is_empty(self):
        return len(self) == 0
    def push(self, e):
        ''' Add element e to the top of the stack '''
        self.queue.enqueue(data)
    def pop(self):
        ''' Remove and return the top element from the stack. If the stack
    is empty, raise an exception'''
        if self.is_empty():
            raise Exception
        return self.queue.dequeue()
    def top(self):
        ''' Return a reference to the top element of the stack without
    removing it. If the stack is empty, raise an exception '''
        if self.is_empty():
            raise Exception('stack is empty')
        return self.queue.first()
