def count_lowercase(s,low,high):
    if (len(s) == 0):
        return 0
    elif low == high:
        if s[low].islower():
            return(1)
        else:
            return(0)
    mid = low + (high-low) // 2
    left_count = count_lowercase(s,low,mid)
    right_count = count_lowercase(s,mid+1,high)
    return left_count + right_count

def is_number_of_lowercase_even(s,low,high):
    if low == high:
        if s[low].islower():
            return False
        else:
            return True
    mid = low + (high-low) // 2
    left = is_number_of_lowercase_even(s,low,mid)
    right = is_number_of_lowercase_even(s,mid+1,high)
    if left == True and right == True:#condition 1
        return True
    elif left == True and right == False:#condition 2
        return False
    elif left == False and right == False:# condition 3
        return True
    else:
        return False





