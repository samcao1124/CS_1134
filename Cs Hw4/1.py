from DoublyLinkedList import DoublyLinkedList
class CompactString:
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        for c in orig_str:
          if len(self.data) == 0:
            self.data.add_last((c, 1))
          else:
            if c == self.data.trailer.prev.data[0]:
              last_node = self.data.trailer.prev.data
              self.data.delete_last()
              self.data.add_last((last_node[0], last_node[1] + 1))
            else:
              self.data.add_last((c, 1))

    def __add__(self, other):
        ''' Creates and returns a CompactString object that
        represent the concatenation of self and other,
            also of type CompactString'''

        # step 1: add all nodes from self to rst
        rst = CompactString("")
        self_cur_node = self.data.header.next
        while (self_cur_node != self.data.trailer):
          rst.data.add_last(self_cur_node.data)
          self_cur_node = self_cur_node.next

        # self's last character is the same as the first
        # character of the other
        other_cur_node = other.data.header.next
        if rst.data.trailer.prev.data[0] == \
        other_cur_node.data[0]:
          last_rst_node = rst.data.trailer.prev.data
          rst.data.delete_last()
          rst.data.add_last((last_rst_node[0], \
          last_rst_node[1] + other_cur_node.data[1]))
          other_cur_node = other_cur_node.next

        while (other_cur_node != other.data.trailer):
          rst.data.add_last(other_cur_node.data)
          other_cur_node = other_cur_node.next
        return rst

    def __lt__(self, other):
        ''' returns True if”f self is lexicographically
        less than other, also of type CompactString'''
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_str = ""
        other_str = ""
        while (self_cur_node != self.data.trailer):
          self_cur_data = self_cur_node.data
          self_str += self_cur_data[0] * self_cur_data[1]
          self_cur_node = self_cur_node.next

        while (other_cur_node != other.data.trailer):
          other_cur_data = other_cur_node.data
          other_str += other_cur_data[0] * other_cur_data[1]
          other_cur_node = other_cur_node.next

        return self_str < other_str

    def __le__(self, other):
        ''' returns True if”f self is lexicographically
        less than or equal to other, also of type
        CompactString'''
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_str = ""
        other_str = ""
        while (self_cur_node != self.data.trailer):
          self_cur_data = self_cur_node.data
          self_str += self_cur_data[0] * self_cur_data[1]
          self_cur_node = self_cur_node.next

        while (other_cur_node != other.data.trailer):
          other_cur_data = other_cur_node.data
          other_str += other_cur_data[0] * other_cur_data[1]
          other_cur_node = other_cur_node.next

        return self_str <= other_str

    def __gt__(self, other):
        ''' returns True if”f self is lexicographically
        greater than other, also of type CompactString'''
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_str = ""
        other_str = ""
        while (self_cur_node != self.data.trailer):
          self_cur_data = self_cur_node.data
          self_str += self_cur_data[0] * self_cur_data[1]
          self_cur_node = self_cur_node.next

        while (other_cur_node != other.data.trailer):
          other_cur_data = other_cur_node.data
          other_str += other_cur_data[0] * other_cur_data[1]
          other_cur_node = other_cur_node.next

        return self_str > other_str

    def __ge__(self, other):
        ''' returns True if”f self is lexicographically
        greater than or equal to other, also of type
        CompactString'''
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_str = ""
        other_str = ""
        while (self_cur_node != self.data.trailer):
          self_cur_data = self_cur_node.data
          self_str += self_cur_data[0] * self_cur_data[1]
          self_cur_node = self_cur_node.next

        while (other_cur_node != other.data.trailer):
          other_cur_data = other_cur_node.data
          other_str += other_cur_data[0] * other_cur_data[1]
          other_cur_node = other_cur_node.next

        return self_str >= other_str

    def __repr__(self):
        cur_node = self.data.header.next
        rst = ""
        while (cur_node != self.data.trailer):
          freq = cur_node.data[1]
          for i in range(0, freq):
            rst += cur_node.data[0]
          cur_node = cur_node.next
        return rst
