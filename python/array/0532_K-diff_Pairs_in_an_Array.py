'''
03/10/2020

532. K-diff Pairs in an Array - Medium

Tag: Array, Two Pointers


Given an array of integers nums and an integer k, return the number of unique k-diff pairs in the array.

A k-diff pair is an integer pair (nums[i], nums[j]), where the following are true:

0 <= i, j < nums.length
i != j
a <= b
b - a == k
 

Example 1:

Input: nums = [3,1,4,1,5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.
Example 2:

Input: nums = [1,2,3,4,5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).
Example 3:

Input: nums = [1,3,1,5,4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Example 4:

Input: nums = [1,2,4,4,3,3,0,9,2,3], k = 3
Output: 2
Example 5:

Input: nums = [-1,-2,-3], k = 1
Output: 2
 

Constraints:

1 <= nums.length <= 104
-107 <= nums[i] <= 107
0 <= k <= 107
'''

from typing import List
# Solution
class Solution1:
    '''
    Time complexity : O(n)
    Space complexity : O(n)
    '''
    def findPairs(self, nums: List[int], k: int) -> int:
        cnt = dict()
        for x in nums:
            if x not in cnt:
                cnt[x] = 0
            cnt[x] += 1
        
        ans = 0
        for x in cnt.keys():
            if k == 0:
                if x in cnt and cnt[x] > 1:
                    ans += 1
            else:
                if x+k in cnt:
                    ans += 1
                    
        return ans

# Unit Test
import unittest
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_testCase(self):
        for Sol in [Solution1()]:
            func = Sol.findPairs
            self.assertEqual(func([3,1,4,1,5], 2), 2)
            self.assertEqual(func([1,2,3,4,5], 1), 4)
            self.assertEqual(func([1,3,1,5,4], 0), 1)


if __name__ == '__main__':
    unittest.main()