'''
04/02/2019

189. Rotate Array - Easy

Tag: Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
'''

# Solution
class Solution:
    '''
    Approach #4 Using Reverse [Accepted]
    Algorithm

    This approach is based on the fact that when we rotate the array k times, 
    k elements from the back end of the array come to the front and the rest of the elements from the front shift backwards.

    In this approach, we firstly reverse all the elements of the array. 
    Then, reversing the first k elements followed by reversing the rest n-k elements gives us the required result.

    Let n=7 and k=3.

    Original List                   : 1 2 3 4 5 6 7
    After reversing all numbers     : 7 6 5 4 3 2 1
    After reversing first k numbers : 5 6 7 4 3 2 1
    After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n # to avoid negative k
        self._reverse(nums, 0, n-1)
        self._reverse(nums, 0, k-1)
        self._reverse(nums, k, n-1)
        return nums
        
    def _reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


class Solution2:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

# Unit Test
import unittest
class rotateCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rotate(self):
        func = Solution().rotate
        self.assertEqual(func([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])

if __name__ == '__main__':
    unittest.main()