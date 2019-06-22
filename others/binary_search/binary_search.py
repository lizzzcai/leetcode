

# Template

def binarySearch(arr, target):
    
    '''
    range [l, r], both side closed, so while loop need
    to include r
    '''
    l, r = 0, len(arr) - 1
    
    while l <= r:
        mid = (l + r) // 2
        # mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            l = mid + 1
        else: # target < arr[mid]
            r = mid - 1

    return -1 