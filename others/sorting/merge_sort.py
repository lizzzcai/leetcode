


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
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else: # left[i] >= right[j]
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res



# Unit Test
import unittest
class selection_sortCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_selection_sort(self):

        func = merge_sort
        # test 1
        self.assertEqual(func([54,26,93,17,77,31,44,55,20]), [17, 20, 26, 31, 44, 54, 55, 77, 93])

        # test 2
        self.assertEqual(func([-99, -12, 3, -1000]), [-1000, -99, -12, 3])

        # test 3
        self.assertEqual(func([9,9,8,7,6,5,4,3,2,1,0]), [0,1,2,3,4,5,6,7,8,9,9])

        # test 4
        self.assertEqual(func([2]), [2])

        # test 5
        self.assertEqual(func([]), [])


if __name__ == '__main__':
    unittest.main()