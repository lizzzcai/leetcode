'''
06/01/2020

523. Continuous Subarray Sum - Medium

Tag: Array, Hash Table

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is also an integer.

 

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.

'''

from typing import List
# Solution
class Solution:
    '''
    prefix sum
    https://leetcode.com/problems/continuous-subarray-sum/discuss/99499/Java-O(n)-time-O(k)-space
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        sum_ = 0
        n = len(nums)
        hmap = {0:-1}
        
        for idx, num in enumerate(nums):
            sum_ += num
            if k != 0:
                sum_ = sum_ % k
            if sum_ in hmap:
                prev = hmap[sum_]
                if idx - prev > 1:
                    return True
            else:
                hmap[sum_] = idx
        return False
            

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        func = Solution().checkSubarraySum
        self.assertEqual(func([23, 2, 4, 6, 7], 6), True)
        self.assertEqual(func([23, 2, 6, 4, 7], 6), True)


if __name__ == '__main__':
    unittest.main()