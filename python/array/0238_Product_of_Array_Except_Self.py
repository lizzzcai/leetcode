"""
17/09/2019
238. Product of Array Except Self - Medium
Tag: Array


Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Left and Right product lists


        L is the product from left to the last one
        
        R is the product from R to the next one
        
        res is L * R
        
        Time: O(n)
        Space: O(1)
        
        """
        
        n = len(nums)
        res = [0] * n
        
        res[0] = 1
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]
        
        # calculate R on the fly to reduce space
        R = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * R
            R *= nums[i]
        
        return res

# Unit Test
import unittest
class productExceptSelfCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_productExceptSelf(self):
        func = Solution().productExceptSelf
 

        self.assertEqual(func([1,2,3,4]), [24,12,8,6])








if __name__ == '__main__':
    unittest.main()


