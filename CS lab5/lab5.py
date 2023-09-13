class LinkedStack:
    def __init__(self):
        self.data = DoublyLinkedist()
    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)

    def is_empty(self):
        ''' Returns true if the stack is empty,false otherwise. '''
        return len(self) == 0
    def push(self, e):
        self.data.add_last(e)
    def top(self):
        ''' Returns the element at the top of the stack. An exception is raised if the stack is empty. '''
        if self.is_empty():
            raise Exception("")
        return self.data.trailer.prev.data

    def pop(self):
        if self.is_empty():
            raise Exception("")
        return self.data.delete_last()


def __getitem__(self, i):
    '''Return the value at the ith node. If i is out of range, an IndexError is raised'''
    if 0<= i <= len(self) // 2:
        start = self.header.next
        for i in range(i):
            start = start.next
        return start.data


class MidStack:
    def __init__(self):
        self.data = DoublyLinkedList()
    def __len__(self):
        ''' Returns the number of elements in the stack. '''
        return len(self.data)
    def is_empty(self):
        ''' Returns true if stack is empty and false otherwise. '''
        return len(self) == 0
    def push(self, e):
        ''' Adds an element, e, to the top of the stack. '''
        self.data.add_last(e)
        if len(self) == 1 :
            self.mid = self.data.trailer.prev
        elif len(self) % 2 != 0  :
            self.mid = self.mid.next
    def top(self):
        ''' Returns the element at the top of the stack. An exception is raised if the stack is empty. '''
        if self.is_empty():
            return Exception
        return self.data.trailer.prev.data
    def pop(self):
        ''' Removes and returns the element at the top of the stack.An exception is raised if the stack is empty. '''
        if self.is_empty():
            return Exception
        return self.data.trailer.delete.last
        elif self.is_empty():
        self.mid = None

    def mid_push(self, e):
        self.data.add_after(self.mid,e)
        if len(self) == 1:
            self.mid = self.data.trailer.prev
        elif len(self) % 2 != 0 :
            self.mid = self.mid.next



class SinglyLinkedList:
    class Node:
        def __init__(self, data=None, next=None):
            self.data = data
            self.next = next
        def disconnect(self):
            self.data = None
            self.next = None
    def __init__(self):
        self.header = SinglyLinkedList.Node()
        self.size = 0
    def __len__(self):
        return self.size
    def is_empty(self):
        return (len(self) == 0)
    def add_after(self, node, val):
        ''' Creates a new node containing val as its data and adds it after an existing node in the SinglyLinkedList'''
        new_node = SinglyLinkedList.Node(val)
        new_node.next = node.next
        node.next = new_node
        self.size +=1
        return new_node

    def add_before(self, node, val):
        ''' Creates a new node containing val as its data and adds it before an existing node in the SinglyLinkedList'''
        curr = self.header
        while curr.next is not node:
            curr = curr.next
        new_node = SinglyLinkedList
        curr.next = new_node
        new_node.next = node
        self.size += 1
        return new_node
    def add_first(self, val):
        ''' Creates a new node containing val as its data and adds it to the front of the SinglyLinkedList'''
        node = self.add_after(self.header,val)
        if len(self) == 1:
            self.last = node
        return node
def add_last(self, val):
    ''' Creates a new node containing val as its data and adds it to the back of the SinglyLinkedList'''
    self.last = self.add_after(self.last,val)
    return self.last
def delete_node(self, node):
    ''' Removes an existing node from the SinglyLinkedList and returns its value'''
    curr = self.header
    while curr.next is not node:
            curr = curr.next
    new_node = SinglyLinkedList
    curr.next = new_node
    new_node.next = node
    self.size -= 1
    val = node.data
    node.disconnect()
    return val
def delete_first(self):
    ''' Removes an existing node from the front of the SinglyLinkedList and returns its value'''
    if self.is_empty == True:
        raise Exception
    return self.delete_node(self.header.next)
def delete_last(self):
    ''' Removes an existing node from the back of the SinglyLinkedList and returns its value'''
    if  self.is_empty == True:
        raise Exception
    curr = self.header
    while curr.next is not self.last:
            curr = curr.next
    val = self.delete_node(self.last)
    self.last = curr
    return val
def bt_even_sum(root):
    if root.left is None and root.right is None:
        if root.data % 2 == 0:
            return root.data
        return 0

def bt_contains(root, val):
    if root:
        return bt_even_sum(root.left)+bt_even_sum(root.right)
    return 0

def add_bts(root1, root):
    root = merge(root1, root2)
    return root


def invert_bt2(root):
    ''' Inverts the binary tree without recursion '''
    queue = ArrayQueue
    queue.enqueue(root)
    while not queue is_empty():
        node = queue.dequeue()
        node.left, node.right == node.right, node.left
        if node.left:
            queue.enqueue(node.left)
        if node.right:
            queue.enqueue(node.right)


def is_full(root):
    ''' Returns True if the Binary Tree is full and false
if not '''
    if root :
        has2_children = root.left and root.right
        has0_children = not root.left or root.right
        return has2_children or has0_children and is_full(root.right) or is_full(root.left)
    return True

def preorder_with_stack(self):
    if self.root is not None:
        node = self.root
        s = ArrayStack
        s.push(node)
        while not s.is_empty():
            node = s.pop()
            yield node.data

            if node.right is not None:
                s.push(node.right)
            if node.left is not None:
                s.push(node.left)
