from DoublyLinkedList import DoublyLinkedList
def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(head1, head2, srt_lnk_lst1, srt_lnk_lst2, rst):
        if (head1 == srt_lnk_lst1.trailer and head2 == srt_lnk_lst2.trailer):
            return

        if (head1 == srt_lnk_lst1.trailer):
            rst.add_last(head2.data)
            head2 = head2.next
        elif (head2 == srt_lnk_lst2.trailer):
            rst.add_last(head1.data)
            head1 = head1.next
        elif (head1.data < head2.data):
            rst.add_last(head1.data)
            head1 = head1.next
        elif (head2.data < head1.data):
            rst.add_last(head2.data)
            head2 = head2.next
        else:
            rst.add_last(head1.data)
            rst.add_last(head2.data)
            head1 = head1.next
            head2 = head2.next
        merge_sublists(head1, head2, srt_lnk_lst1, srt_lnk_lst2, rst)

    rst = DoublyLinkedList()
    merge_sublists(srt_lnk_lst1.header.next, srt_lnk_lst2.header.next,srt_lnk_lst1, srt_lnk_lst2, rst)
    return rst



