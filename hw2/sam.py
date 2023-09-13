def insertion_sort_R(lst):
    def insertion_sort_helper(lst, low, high):
        if (low == high):
            return
        else:
            insertion_sort_helper(lst, low, high - 1)
            ind = high
            while ((lst[ind - 1] > lst[ind]) and
                       (ind >= low + 1)):
                lst[ind], lst[ind - 1] = lst[ind - 1], lst[ind]
                ind -= 1

    insertion_sort_helper(lst, 0, len(lst)-1)


lst1 = [4,-1,2,-6,9,-4]


print(insertion_sort_R(lst1))
