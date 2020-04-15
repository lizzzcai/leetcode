'''
15/04/2020

525. Contiguous Array - Medium

Tag: Hash Table

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.

'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        max_len = 0
        count = 0
        hmap = {0:-1}
        for i in range(n):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            
            if count in hmap:
                max_len = max(max_len, i - hmap[count])
            else:
                hmap[count] = i

        return max_len

class Solution2:
    def findMaxLength(self, nums: List[int]) -> int:
        
        n = len(nums)
        arr = [-2] * (2*n+1)
        arr[n] = -1
        max_len = 0
        count = 0
        
        for i in range(n):
            if nums[i] == 0:
                count += -1
            else:
                count += 1
            if arr[count+n] >= -1:
                max_len = max(max_len, i - arr[count+n])
            else:
                arr[count+n] = i
        
        return max_len


# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1(), Solution2()]:
            func = Sol.findMaxLength
            self.assertEqual(func([0,1]), 2)
            self.assertEqual(func([0,1,0]), 2)

if __name__ == '__main__':
    unittest.main()