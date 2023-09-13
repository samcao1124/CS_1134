def split_by_sign(lst, low, high):
   if (low == high):
       return
   mid = low + (high - low) // 2
   split_by_sign(lst, low, mid)
   split_by_sign(lst, mid + 1, high)
   new_list = lst.copy()
   left_index = low
   right_index = mid + 1

   while (left_index <= mid and right_index <= high):
       if(new_list[left_index] < new_list[right_index]):
           lst[low] = new_list[left_index]
           low += 1
           left_index += 1
       else:
           lst[low] = new_list[right_index]
           low += 1
           right_index += 1
   for i in range(left_index, mid + 1):
       lst[low] = new_list[i]
       low += 1
