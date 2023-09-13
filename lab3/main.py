"Q1:"
def __repr__(self):
    if:
        isinstance(val,str) == True
    else:
        str
    return("[" + ",".join("'" + val + "'"+ "]")

def __add__(self,other):
    lst = Arraylist()
    lst += other
    lst += self
    return lst
def __iadd__(self,other):
    self.extend(other)
    return self

def __setitem__(self,ind,val):
    if -self <= ind <= self:
        raise IndexError

def __rmul__(self,scalar):
    return self*scalar

def remove(self,val): ## Im confused about this one also the remove all

    if val in self:
        data =  make_array(self.capacity)

        i = 0
        while self[i] != self.n-1
            data[i] = self[i]
            i+=1
        self.data = data
        self.n = -1

def removeall(self,val):
    count = 0
    for i in self:
        if i != val:
            data[index] = i
        self.data = data
        self.n -= count

def find_min(lst,low,high):
    if low == high:
        return lst[low]
    curr_min = find_min(lst,low+1,high)
    return min(curr_min,lst[low])

def find_second_min(lst):
    first = None
    second = None
    for i in lst:
        if first == None:
            first = i
        elif i < first:
            second = first
            i = second
    return second

def deep_reverse(lst,left,right):
    """
: lst type: list
: output type: None
"""
    if left > right :
        return
    if isinstance(lst[left],list):
        deep_reverse(lst,0,right-1)

    lst[left],lst[right] = lst[right],lst[left]
    deep_reverse(lst,left-1,right-1)









