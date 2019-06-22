

'''
Time complexity : O(N^2)
Space complexity: O(1)
'''
def selection_sort(arr):
    '''
    two pointer
    '''
    if not arr or len(arr) < 2:
        return arr

    for i in range(len(arr)-1):
        min_index = i
        # find the min value between i+1 and len(arr)
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # if find a value smaller than i, swap them.
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr


# test
t1 = [54,26,93,17,77,31,44,55,20]
print(t1)
print(selection_sort(t1))
t2 = [-99, -12, 3, -1000]
print(t2)
print(selection_sort(t2))