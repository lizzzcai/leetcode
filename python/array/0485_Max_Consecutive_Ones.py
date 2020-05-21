'''
19/05/2020

485. Max Consecutive Ones - Easy

Tag: Array

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        i = 0
        res = 0
        while i < len(nums):
            
            if nums[i] == 1:
                j = i
                while j < len(nums) and nums[j] == nums[i]:
                    j += 1

                if j-i > res:
                    res = j-i
                i = j
                
            else:
                i += 1
            
        return res
            
import itertools
class Solution2:
    def maxPower(self, s: str) -> int:
        
        return max(len(list(b)) for a, b in itertools.groupby(s))

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findMaxConsecutiveOnes
            self.assertEqual(func([1,1,0,1,1,1]), 3)
            self.assertEqual(func([1,0,1,1,0,1]), 2)




if __name__ == '__main__':
    unittest.main()