

# Template

class Solution1:
    def binary_search(self, arr, target):
        
        '''
        iterative:

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


class Solution2:
    def binary_search(self, arr, target):
        '''
        recursive:
        
        range [l, r], both side closed, so while loop need
        to include r
        '''

        def helper(l, r):
            if l > r:
                return -1
            
            mid = (l + r) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                return helper(mid+1, r)
            else: # arr[mid] > target
                return helper(l, mid-1)

        l, r = 0, len(arr) - 1
        return helper(l, r)
        

# Unit Test
import unittest
class binary_searchCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_binary_search(self):
        func = Solution1().binary_search
        # test 1
        self.assertEqual(func([1, 3, 5, 7, 9], 3), 1)
        self.assertEqual(func([1, 3, 5, 7, 9], 2), -1)

        func = Solution2().binary_search
        # test 1
        self.assertEqual(func([1, 3, 5, 7, 9], 3), 1)
        self.assertEqual(func([1, 3, 5, 7, 9], 2), -1)


if __name__ == '__main__':
    unittest.main()