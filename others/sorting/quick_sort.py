from __future__ import print_function

class Solution1:
    def partition(slef, array, left, right):
        """quick sort partition function"""
        i = left-1 # index of smaller element
        for j in range(left, right):
            # if the current element is smaller than the pivot
            if array[j] <= array[right]:
                # increase index of smaller element
                i += 1
                # swap the values
                array[j], array[i] = array[i], array[j]
        # swap the pivot
        array[i+1], array[right] = array[right], array[i+1]
        return i+1

    def quicksort(self, array, left, right):
        """Quick sort algorithm implementation"""
        if left < right:
            pivot = self.partition(array, left, right)
            self.quicksort(array, left, pivot-1)
            self.quicksort(array, pivot+1, right)
        return array

class Solution2:
    def quicksort(self, array):
        if len(array) < 2:
            return array # base case, arrays with 0 or 1 element are already "sorted"
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot] # sub-array of all the elements not larger than pivot
            greater = [i for i in array[1:] if i > pivot] # sub-array of all the elements greater than the pivot
            return self.quicksort(less) + [pivot] + self.quicksort(greater)


# Unit Test
import unittest
class selection_sortCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_selection_sort(self):
        func = Solution1().quicksort
        # test 1
        self.assertEqual(func([54,26,93,17,77,31,44,55,20], 0, 8), [17, 20, 26, 31, 44, 54, 55, 77, 93])

        # test 2
        self.assertEqual(func([-99, -12, 3, -1000], 0, 3), [-1000, -99, -12, 3])

        # test 3
        self.assertEqual(func([9,9,8,7,6,5,4,3,2,1,0], 0, 10), [0,1,2,3,4,5,6,7,8,9,9])

        # test 4
        self.assertEqual(func([2], 0, 0), [2])

        # test 5
        self.assertEqual(func([], 0, -1), [])


        func = Solution2().quicksort
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