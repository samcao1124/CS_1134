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
        rst = CompactString("")
        self_cur_node = self.data.header.next
        while (self_cur_node != self.data.trailer):
          rst.data.add_last(self_cur_node.data)
          self_cur_node = self_cur_node.next

        other_cur_node = other.data.header.next
        if rst.data.trailer.prev.data[0] == other_cur_node.data[0]:
          last_rst_node = rst.data.trailer.prev.data
          rst.data.delete_last()
          rst.data.add_last((last_rst_node[0],last_rst_node[1] + other_cur_node.data[1]))
          other_cur_node = other_cur_node.next

        while (other_cur_node != other.data.trailer):
          rst.data.add_last(other_cur_node.data)
          other_cur_node = other_cur_node.next
        return rst

    def __lt__(self, other):
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_freq = 0
        other_freq = 0
        if self_cur_node == self.data.trailer and other_cur_node == other.data.trailer:
                return False
        while (self_cur_node != self.data.trailer and other_cur_node != other.data.trailer):
            self_char = self_cur_node.data[0]
            other_char = other_cur_node.data[0]
            self_freq = self_cur_node.data[1] if self_freq == 0 else self_freq
            other_freq = other_cur_node.data[1] if other_freq == 0 else other_freq
            if (self_char > other_char):
                return False
            if (self_char < other_char):
                return True

            min_freq = min([self_freq, other_freq])
            self_freq -= min_freq
            other_freq -= min_freq
            self_cur_node = self_cur_node.next if self_freq == 0 else self_cur_node
            other_cur_node = other_cur_node.next if other_freq == 0 else other_cur_node
        return True if (other_cur_node != other.data.trailer) else False
    
    def __le__(self, other):
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_freq = 0
        other_freq = 0
        if self_cur_node == self.data.trailer and other_cur_node == other.data.trailer:
                return True
        while (self_cur_node != self.data.trailer and other_cur_node != other.data.trailer):
          self_char = self_cur_node.data[0]
          other_char = other_cur_node.data[0]
          self_freq = self_cur_node.data[1] if self_freq == 0 else self_freq
          other_freq = other_cur_node.data[1] if other_freq == 0 else other_freq
          if (self_char > other_char):
              return False
          if (self_char < other_char):
              return True
          min_freq = min([self_freq, other_freq])
          self_freq -= min_freq
          other_freq -= min_freq
          self_cur_node = self_cur_node.next if self_freq == 0 else self_cur_node
          other_cur_node = other_cur_node.next if other_freq == 0 else other_cur_node
        if (other_cur_node != other.data.trailer or self_cur_node == self.data.trailer \
            and self.data.trailer.prev.data[0] == other.data.trailer.prev.data[0]):
          return True


    def __gt__(self, other):
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_freq = 0
        other_freq = 0
        if self_cur_node == self.data.trailer and other_cur_node == other.data.trailer:
            return False
        while (self_cur_node != self.data.trailer and other_cur_node != other.data.trailer):
          self_char = self_cur_node.data[0]
          other_char = other_cur_node.data[0]
          self_freq = self_cur_node.data[1] if self_freq == 0 else self_freq
          other_freq = other_cur_node.data[1] if other_freq == 0 else other_freq
          if (self_char < other_char):
              return False
          if (self_char > other_char):
              return True
          min_freq = min([self_freq, other_freq])
          self_freq -= min_freq
          other_freq -= min_freq
          self_cur_node = self_cur_node.next if self_freq == 0 else self_cur_node
          other_cur_node = other_cur_node.next if other_freq == 0 else other_cur_node
        return True if (self_cur_node != self.data.trailer) else False

    def __ge__(self, other):
        self_cur_node = self.data.header.next
        other_cur_node = other.data.header.next
        self_freq = 0
        other_freq = 0
        if self_cur_node == self.data.trailer and other_cur_node == other.data.trailer:
            return True
        while (self_cur_node != self.data.trailer and other_cur_node != other.data.trailer):
          self_char = self_cur_node.data[0]
          other_char = other_cur_node.data[0]
          self_freq = self_cur_node.data[1] if self_freq == 0 else self_freq
          other_freq = other_cur_node.data[1] if other_freq == 0 else other_freq
          if (self_char < other_char):
              return False
          if (self_char > other_char):
              return True
          min_freq = min([self_freq, other_freq])
          self_freq -= min_freq
          other_freq -= min_freq
          self_cur_node = self_cur_node.next if self_freq == 0 else self_cur_node
          other_cur_node = other_cur_node.next if other_freq == 0 else other_cur_node
        if (other_cur_node != other.data.trailer \
          or self_cur_node == self.data.trailer and self.data.trailer.prev.data[0] == other.data.trailer.prev.data[0]):
          return True

    def __repr__(self):
        cur_node = self.data.header.next
        rst = ""
        while (cur_node != self.data.trailer):
          rst += cur_node.data[0] * cur_node.data[1]
          cur_node = cur_node.next
        return rst

