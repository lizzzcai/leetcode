'''
07/08/2020

442. Find All Duplicates in an Array - Medium

Tag: Array

Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for x in nums:
            if x < 0:
                x = -x

            idx = x-1
            
            if nums[idx] < 0:
                res.append(idx+1)
                
            nums[idx] = -nums[idx]
        
        return res

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findDuplicates
            self.assertEqual(func([4,3,2,7,8,2,3,1]), [2,3])

if __name__ == '__main__':
    unittest.main()