from DoublyLinkedList import DoublyLinkedList
def copy_linked_list(lnk_lst):
  rst_list = DoublyLinkedList()
  for node in lnk_lst:
      rst_list.add_last(node)
  return rst_list


def deep_copy_linked_list(lnk_lst):
  rst = DoublyLinkedList()
  for node in lnk_lst:
    if (isinstance(node, DoublyLinkedList)):
      rst.add_last(deep_copy_linked_list(node))
    else:
      rst.add_last(node)
  return rst
