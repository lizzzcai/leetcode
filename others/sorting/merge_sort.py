


'''
Time complexity : O(nlogn)
Space complexity: O(N)

https://github.com/yuzhoujr/leetcode/issues/39

'''

def merge_sort(array):
    """Merge sort algorithm implementation."""
    if not array or len(array) < 2:
        return array
    
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)

def merge(left, right):
    """Merge sort merging function."""
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else: # left[i] >= right[j]
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res



t1 = [54,26,93,17,77,31,44,55,20]
t2 = [-99, -12, 3, -1000]
print(merge_sort(t1))
print(merge_sort(t2))