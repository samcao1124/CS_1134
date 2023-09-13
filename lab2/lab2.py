# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def reverse_list(lst):
    """
    : lst type: list[]
    : return type: None
    """
    first = 0
    end = len(lst) - 1
    while first < end:
        lst[first], lst[end] = lst[end], lst[first]
        first += 1
        end -= 1
lst = [1, 2, 3, 4, 5, 6]
reverse_list(lst) #default, no parameters passed
print(lst)


def move_zeros(nums):
    """
: nums type: list[int]
: return type: None
"""
    number = 0
    for i in range(len(nums)):
        if i != 0 :
            nums[number], nums[i] = nums[i],nums[number]
            number +=1

def find_missing(lst):
    for num in range(len(lst) + 1):#n
        if num not in lst:
            if lst[0] != 0:
                return 0
            for i in range(len(lst)):
                if lst[i] - lst[i-1] >1 :
                    return lst[i] -1
            return lst
    return num

def find_missing(lst):
    """
: nums type: list[int] (sorted)
: return type: int
"""

    "I am confused about this quesiton, I checked the answer key"
    left = 0
    right = len(lst) - 1
    if lst[0] != 0 :
        return 0
    elif lst[len(lst) -1 ] == len(lst) -1:
        return len(lst)
    while lst[right] - lst[left] != 2:
        mid = (left + right) // 2
        if lst[right] -lst[mid] != right - mid:
            left = mid
        elif lst[mid] -lst[left] != mid - left:
            right = mid
        return lst[left] + 1

def sum_to(n):
    """
: n type: int
: return type: int
"""
    if n < 0:
        return 0
    sum = n+ sum_to(n)
    return sum

def binary_search(lst, low, high, val):
    """
    : lst type: list[int]
    : val type: int
    : low type, high type: int
    : return type: int (found),
    None"""
    while low <= high:
        mid = (high + low ) // 2
        if lst[mid] == val:
            return mid
        elif lst[mid] < val:
            return mid+1
        elif lst[mid] > val:
            return mid-1

def vc_count(word, low, high):
    """
    : word type: str
    : low, high type: int
    : return type: tuple (int, int)
    """
    "I only wrote the if part, I checked the answer for the else part."
    vovwels = "aeiouAEIOU"
    if low <= high:
        if word[low] in vovwels:
            return (word[low],low)
    else:
        prev = vc_count(word,low+1, high)
        if word[low] in vovwels:
            return (prev[0]+1, prev[1])
        return (prev[0]+1, prev[1])

