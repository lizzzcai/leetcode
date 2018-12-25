'''
25/12/2018

Tag: Binary Search

367. Valid Perfect Square - Easy

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Output: true
Example 2:

Input: 14
Output: false

'''

def binarySearch(arr, target):
    left , right = 0, len(arr) - 1  
    while left <= right:            
        mid = (left+right)//2
        # mid = left + (right-left)//2 # avoid overflow
        if arr[mid] == target:
            return mid
        if target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1 
    return -1


class Solution:
    '''
    Time Complexity: O(logn). 
    Space Complexity: O(1).
    '''
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left, right = 0, num
        while left <= right:
            mid = left + (right -left) // 2
            val = mid ** 2
            if num == val:
                return True
            elif num > val:
                left = mid + 1
            else: # num < val
                right = mid - 1
        return False

# Unit Test
import unittest
class TwoSumCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_twoSum(self):
        func = Solution().isPerfectSquare
        self.assertEqual(func(16), True)
        self.assertEqual(func(14), False)

if __name__ == '__main__':
    unittest.main()