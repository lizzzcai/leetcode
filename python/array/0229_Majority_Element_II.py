'''
01/05/2020

229. Majority Element II - Medium

Tag: Array

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]
Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''

from typing import List
# Solution
class Solution1:
    '''
    Boyer-Moore Majority Vote
    https://leetcode.com/problems/majority-element-ii/discuss/63537/My-understanding-of-Boyer-Moore-Majority-Vote
    Time complexity : O(n)
    Space complexity : O(1)
    '''
    def majorityElement(self, nums: List[int]) -> List[int]:
        first_candidate,second_candidate = 0, 0
        first_count, second_count = 0, 0
        n = len(nums)
        
        for x in nums:
            if x == first_candidate:
                first_count += 1
            elif x == second_candidate:
                second_count += 1
            elif first_count == 0:
                first_candidate = x
                first_count += 1
            elif second_count == 0:
                second_candidate = x
                second_count += 1
            else:
                first_count -= 1
                second_count -= 1
        
        return [x for x in set([first_candidate, second_candidate]) if nums.count(x) > n/3]
# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.majorityElement
            self.assertEqual(func([3,2,3]), [3])
            self.assertEqual(func([1,1,1,3,3,2,2,2]), [1,2])
            self.assertEqual(func([0,0,0]), [0])

if __name__ == '__main__':
    unittest.main()