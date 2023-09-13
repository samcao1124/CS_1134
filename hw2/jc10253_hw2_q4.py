def split_parity(lst):
    odd_index = 0
    for i in range(len(lst)):
        if lst[i] % 2 != 0:
            lst[i],lst[odd_index] = lst[odd_index],lst[i]
            odd_index += 1
