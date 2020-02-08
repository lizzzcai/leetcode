

from typing import List

class Solution1:
    def selection_sort(self, arr: List[int]) -> List[int]:
        '''
        two pointer

        Time complexity : O(N^2)
        Space complexity: O(1)
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

class Solution2:
    def selection_sort(self, arr: List[int]) -> List[int]:
        res = []
        for _ in range(len(arr)):
            smallest_index = self.find_smallest(arr)
            res.append(arr.pop(smallest_index))
        return res
    
    def find_smallest(self, arr: List[int]) -> int:
        # stores the smallest value
        smallest = arr[0]
        # stores the index of smallest value
        smallest_index = 0
        for i in range(1, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        return smallest_index

# Unit Test
import unittest
class selection_sortCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_selection_sort(self):
        func = Solution1().selection_sort
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


        func = Solution2().selection_sort
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