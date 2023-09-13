def findChange(lst01):
    left = 0
    right = len(lst01) -1
    ind = None
    found = False
    while found == False and left <= right:
        mid = (left + right) // 2
        if lst01[mid] == 0 and lst01[mid + 1] == 1:
            ind = mid + 1
            found = True
        elif lst01[mid] == 0 and lst01[mid + 1] == 0:
            left = mid + 1
        elif lst01[mid] == 1:
            right = mid - 1
    return ind



