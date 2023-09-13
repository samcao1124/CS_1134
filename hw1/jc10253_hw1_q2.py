def shift(lst, k, direction = "left"):
    if direction == "left":
        for i in range(k):
            remove_left = lst.pop(0)
            lst.append(remove_left)
    else:
        for i in range(k):
            remove_right = lst.pop()
            lst.insert(0,remove_right)
    return lst



