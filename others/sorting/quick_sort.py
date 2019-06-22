from __future__ import print_function


def partition(array, left, right):
    """quick sort partition function"""
    i = left-1
    for j in range(left, right):
        if array[j] <= array[right]:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[right] = array[right], array[i+1]
    return i+1

def quicksort(array, left, right):
    """Quick sort algorithm implementation"""
    if left < right:
        pivot = partition(array, left, right)
        quicksort(array, left, pivot-1)
        quicksort(array, pivot+1, right)



array = [3, 2, 1, 0, 9, 8, 7, 7, 5, 6, 5, 4]
quicksort(array, 0, len(array)-1)
print(array)
