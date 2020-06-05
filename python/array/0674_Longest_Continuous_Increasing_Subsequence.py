"""
05/06/2020
674. Longest Continuous Increasing Subsequence - Easy
Tag: Array

Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 
Note: Length of the array will not exceed 10,000.
"""

from typing import List


class Solution1:
    '''
    O(N)
    O(1)
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = idx = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]:
                idx = i
            ans = max(ans, i-idx + 1)
        return ans
        

# Unit Test
import unittest
class longestConsecutiveCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_longestConsecutive(self):

        for Sol in [Solution1()]:
            func = Sol.findLengthOfLCIS

            self.assertEqual(func([2,2,2,2,2]), 1)
            self.assertEqual(func([1,3,5,4,7]), 3)
            self.assertEqual(func([1,3,5,7]), 4)









if __name__ == '__main__':
    unittest.main()


